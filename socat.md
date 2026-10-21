http://www.dest-unreach.org/socat/

# The Ultimate Socat Guide: From Multicast Relays to Advanced Networking

`socat` (SOcket CAT) is one of the most powerful and versatile networking utilities available for Linux and Unix-like systems. This guide covers everything from basic multicast forwarding to running `socat` as a production-ready system service.

---

## 1. What is Socat?

`socat` is a command-line utility that establishes **two bidirectional byte streams** and transfers data between them. Think of it as `netcat` on steroids. 

While `netcat` typically links a network socket to standard input/output, `socat` can connect almost anything to anything else. It natively supports a massive array of address types, including:
* **Network Sockets:** TCP4/TCP6, UDP4/UDP6, SCTP, Multicast.
* **Security Layers:** SSL/OpenSSL, SOCKS4/SOCKS5 proxies.
* **System Interfaces:** File descriptors, Named Pipes (FIFOs), UNIX domain sockets.
* **Devices & OS Features:** Serial lines, PTYs (pseudo-terminals), TUN/TAP virtual network interfaces.

Because it handles data bidirectionally by default, it is commonly used for port forwarding, traffic logging, network debugging, and protocol bridging.

---

## 2. How to Forward Multicast to UDP (Unicast)

Forwarding an incoming multicast stream to a specific unicast UDP destination is a classic `socat` use case. The syntax requires configuring the receiving side to join the multicast group.

### The Command:
```bash
socat UDP4-RECVFROM:1234,ip-add-membership=239.1.1.1:0.0.0.0,fork UDP4-SENDTO:192.168.1.50:5678
```

### Breakdown of the Syntax:
* **`UDP4-RECVFROM:1234`**: Opens a local UDP port on `1234` to receive incoming packets.
* **`ip-add-membership=239.1.1.1:0.0.0.0`**: This is the magic flag. It instructs the network stack to send an IGMP join request for the multicast group `239.1.1.1`. The `0.0.0.0` tells the OS to listen for this multicast traffic on **all** available local network interfaces.
* **`fork`**: Keeps the main `socat` process listening. Every time a packet interaction occurs, it forks a child process to handle the stream, allowing it to continuously process traffic.
* **`UDP4-SENDTO:192.168.1.50:5678`**: The second stream address. It packages the bytes received from the multicast stream and outputs them as classic UDP unicast packets to the destination IP `192.168.1.50` on port `5678`.

*Note: For testing private or organizational multicast, stick to the `239.0.0.0/8` administratively scoped range, and avoid using `224.0.0.1` as all sockets are auto-members of that group.*

---

## 3. Listening and Outputting on Different Interfaces

**Yes**, `socat` can easily be pinned to specific network interfaces (NICs). This is critical if your machine acts as a router or gateway and you want to ingest data from an isolated internal network (`eth1`) and send it out over a public or management network (`eth0`).

To achieve this, you replace the wildcard `0.0.0.0` or default routing behaviors with specific IP bounds or socket options.

### Method A: Binding by Local IP Address
If you know the exact IPs assigned to your interfaces, explicitly bind to them:
```bash
socat UDP4-RECVFROM:1234,ip-add-membership=239.1.1.1:192.168.10.15,fork UDP4-SENDTO:10.0.0.50:5678,bind=10.0.0.15
```
* **`ip-add-membership=239.1.1.1:192.168.10.15`**: Forces the IGMP membership join request to go out *only* on the interface with the local IP `192.168.10.15`.
* **`bind=10.0.0.15`**: Forces the outgoing unicast UDP packets to originate explicitly from the network interface assigned to `10.0.0.15`.

### Method B: Binding by Physical Device Name (Linux Only)
If your IPs are dynamic, you can force `socat` to bind directly to the Linux network interface names using the `so-bindtodevice` socket option:
```bash
socat UDP4-RECVFROM:1234,ip-add-membership=239.1.1.1:0.0.0.0,so-bindtodevice=eth1,fork UDP4-SENDTO:192.168.1.50:5678,so-bindtodevice=eth0
```
* **Input side:** Listens and registers multicast exclusively on `eth1`.
* **Output side:** Pushes data out exclusively via `eth0`.

---

## 4. Advanced Configuration & Performance Tuning

`socat` provides low-level control over buffer sizes, socket behaviors, and optimization parameters. Tweaking these options prevents dropped packets and handles system disconnections elegantly.

### Determining and Calculating Optimal Buffer Sizes
When transferring high-throughput data (like high-bitrate video, telemetry bursts, or raw database backups), default system buffers easily overflow. 

1. **Calculate the Bandwidth-Delay Product (BDP):** To determine the optimal buffer size for a network stream, calculate:
   $$\text{Buffer Size (Bytes)} = \frac{\text{Bandwidth (Bits/sec)} \times \text{Round-Trip Time (Latency in Seconds)}}{8}$$
   *Example:* If you are moving data across a **1 Gbps link** with a **20ms (0.02s) latency**, your optimal network socket buffer is:
   $$\frac{1,000,000,000 \times 0.02}{8} = 2,500,000\text{ Bytes (~2.5 MB)}$$

2. **Match the Application Block Size (`-b`):** The global block size option `-b` specifies how many bytes `socat` transfers in a single memory operation. For high-speed networking, match the application block size to standard **UDP payload sizes (e.g., 65536 bytes)** or **TCP window segments** to minimize system call overhead.

### Applying High-Throughput Options in Socat
```bash
socat -b 65536 UDP4-RECVFROM:1234,rcvbuf=2500000,ip-add-membership=239.1.1.1:0.0.0.0,fork UDP4-SENDTO:192.168.1.50:5678,sndbuf=2500000
```
* **`-b 65536`**: Changes the `socat` internal memory block transfer size to 64KB (matching maximum UDP payload sizes) instead of the default 8192 bytes.
* **`rcvbuf=2500000`**: Overrides the OS `SO_RCVBUF` to 2.5MB, absorbing massive spikes in incoming data.
* **`sndbuf=2500000`**: Overrides the OS `SO_SNDBUF` to 2.5MB, allowing the network stack to buffer outgoing packets cleanly without blocking `socat`.

### Managing Retries and Timeouts
For TCP-based streams or stream redirections that might experience network drops, add recovery logic:
```bash
socat -t 5 TCP4-LISTEN:8080,reuseaddr,fork TCP4:backend-server:8080,intervall=2,retry=10
```
* **`-t 5`**: Closes individual inactive sub-connections after 5 seconds of total inactivity (prevents dangling file descriptors).
* **`reuseaddr`**: Allows immediate rebinding to the local port if the service restarts, bypassing the kernel's `TIME_WAIT` state.
* **`intervall=2,retry=10`**: If the connection to `backend-server` fails, `socat` will attempt to reconnect 10 times, waiting 2 seconds between each attempt before fully giving up.

---

## 5. How to Run Socat as a Systemd Service

To ensure your multicast-to-unicast relay runs continuously in the background, survives crashes, and automatically starts when the machine boots, deploy it as a `systemd` service on Debian or RHEL.

### Step 1: Create the Systemd Unit File
Open a new configuration file with root privileges:
```bash
sudo nano /etc/systemd/system/socat-relay.service
```

### Step 2: Paste the Configuration
Paste the following definition into the file. Adjust the interfaces, IPs, and ports to match your actual environment:
```ini
[Unit]
Description=Socat Multicast to Unicast UDP Relay
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
# Run as an unprivileged user for security (change to your existing user or 'nobody')
User=nobody
Group=nogroup
ExecStart=/usr/bin/socat -b 65536 UDP4-RECVFROM:1234,rcvbuf=1048576,ip-add-membership=239.1.1.1:0.0.0.0,fork UDP4-SENDTO:192.168.1.50:5678,sndbuf=1048576
Restart=always
RestartSec=3
# Prevent systemd from killing the socket abruptly during heavy loads
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```
*(Note: On RHEL systems, change `Group=nogroup` to `Group=nobody` as the group name varies across distributions).*

### Step 3: Enable and Start the Service
Reload the systemd daemon to pick up your new file, enable it to start on boot, and initiate the service immediately:
```bash
sudo systemctl daemon-reload
sudo systemctl enable socat-relay.service
sudo systemctl start socat-relay.service
```

### Step 4: Monitor the Relay
To check if the service is active or to debug error messages, inspect the system logs:
```bash
sudo systemctl status socat-relay.service
sudo journalctl -u socat-relay.service -f
```

---

## 6. Cool and Slick Socat Tricks

`socat` can solve tricky operational problems in a single line of bash. Here are some of the slickest tricks engineers use:

### A. The Instant Encrypted VPN Tunnel (SSL/TLS Wrapping)
Need to send data securely over an untrusted network, but the application doesn't support encryption? You can pipe raw TCP through an on-the-fly SSL/TLS tunnel.

#### 1. Generate a Self-Signed SSL Certificate Structure
Before running the tunnel, the receiver requires a valid key and certificate. Run these commands on the server to create an ad-hoc 2048-bit RSA keypair packaged into a single `.pem` file:
```bash
# Generate private key and self-signed certificate
openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt -subj "/CN=socat-tunnel"

# Combine them into a single file required by socat
cat server.key server.crt > server.pem
chmod 600 server.pem
```

#### 2. Establish the Encrypted Tunnel
* **On the secure receiver server:**
  ```bash
  socat OPENSSL-LISTEN:4443,cert=server.pem,verify=0 TCP4:127.0.0.1:80
  ```
* **On the sending client:**
  ```bash
  socat TCP4-LISTEN:8080,fork OPENSSL:server-ip:4443,verify=0
  ```
*Any data sent locally to port `8080` on the client gets encrypted, zipped across port `4443`, decrypted by the server, and delivered cleanly to the local port `80` web server.*

### B. Serial Port to Network Bridge
If you work with hardware automation, IoT devices, or network switches, you can expose a physical serial port (`/dev/ttyUSB0`) directly over the network:
```bash
socat TCP4-LISTEN:9000,reuseaddr,fork,rawer FILE:/dev/ttyUSB0,b115200,rawer
```

You can now use telnet or a remote script to connect to port 9000 from across the world and interact directly with that physical serial device at 115200 baud.


### C. Live Traffic Logging (The Passive Network Tap)

If you want to forward traffic but also want a transparent peek at exactly what bytes are traveling through the stream, use the SYSTEM address type paired with tee:

```bash
socat UDP4-RECVFROM:1234,fork SYSTEM:"tee -a /tmp/traffic.log | socat - UDP4-SENDTO:192.168.1.50:5678"
```

This accepts the stream, appends a raw byte copy to a local log file, and passes the original stream to the destination without interruption.
