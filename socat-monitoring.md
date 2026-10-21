# Guide: Monitoring and Verifying Socat Multicast-to-UDP Forwarding

When setting up a `socat` stream relay, it is crucial to verify that data is actually arriving on the multicast group and successfully leaving via unicast UDP. Because UDP is a connectionless protocol, standard tools won't throw connection errors if packets go missing. 

This guide covers how to monitor both sides of the stream to confirm your pipeline works perfectly.

---

## 1. Verifying Incoming Multicast Traffic

Before checking `socat`, you must verify that the multicast stream is physically reaching your server's network interface interface.

### Option A: The Quick Check with `tcpdump`
`tcpdump` is the standard tool for packet analysis on Linux. You can filter explicitly for your multicast destination IP address.

Run this command (replace `eth1` with your ingress interface, and `239.1.1.1` with your multicast group IP):
```bash
sudo tcpdump -i eth1 -nn host 239.1.1.1
```
*   **What success looks like:** You should see a continuous scroll of packets showing the source IP hitting your multicast group address:
    ```text
    23:14:02.105432 IP 192.168.10.20.45000 > 239.1.1.1.1234: UDP, length 1316
    ```
*   **If you see nothing:** Your network switches are not routing the multicast traffic to this machine, or a firewall is blocking it. Check your IGMP snooping configuration on the switch.

### Option B: Checking Active IGMP Memberships
To verify if `socat` successfully commanded the network interface to join the multicast group, inspect the kernel's active multicast memberships:
```bash
netstat -g
# OR
ip maddr show
```
Look for your interface (`eth1`) under the group address `239.1.1.1`. If it isn't listed while `socat` is running, the `ip-add-membership` flag was omitted or configured on the wrong interface.

---

## 2. Monitoring Outgoing Unicast UDP Traffic

Once you know multicast is arriving, you need to check if `socat` is processing and emitting the unicast packets.

### Option A: Sniffing the Egress Interface
Run `tcpdump` on your output interface (e.g., `eth0`), filtering for the unicast destination IP and port you specified in your `socat` command:
```bash
sudo tcpdump -i eth0 -nn dst 192.168.1.50 and port 5678
```
*   **What success looks like:** A matching stream of packets showing your server's local IP sending data directly to the destination:
    ```text
    23:14:05.891024 IP 10.0.0.15.38421 > 192.168.1.50.5678: UDP, length 1316
    ```

### Option B: Real-time Bitrate and Data Monitoring (`pv`)
If you want to view the actual data volume or bitrate passing through the system without parsing raw `tcpdump` hex dumps, you can install the Pipe Viewer (`pv`) utility.

1. Install `pv`:
   ```bash
   sudo apt install pv      # Debian/Ubuntu
   sudo dnf install pv      # RHEL
   ```
2. Inspect the stream by placing `pv` in the middle of a `socat` tap command:
   ```bash
   socat UDP4-RECVFROM:1234,ip-add-membership=239.1.1.1:0.0.0.0,fork SYSTEM:"pv | socat - UDP4-SENDTO:192.168.1.50:5678"
   ```
*   **What success looks like:** `pv` will output a live console dashboard showing the exact data speed and total data transferred through `socat` in real time:
    ```text
    4.12 MiB [ 1.02 MiB/s] [  <=>                                                 ]
    ```

---

## 3. Local End-to-End Testing (The Dummy Receiver)

If you don't have access to the final destination machine (`192.168.1.50`) to verify packet arrival, you can temporarily change your `socat` output target to `127.0.0.1:5678` (localhost) and spin up a local dummy listener to print the payload to your terminal.

1. In Terminal A, start a dummy UDP listener that prints incoming bytes as text or a hex dump:
   ```bash
   # View as raw text:
   socat UDP4-LISTEN:5678,reuseaddr -
   
   # Or view as a clean Hex/ASCII dump:
   socat UDP4-LISTEN:5678,reuseaddr - | hexdump -C
   ```
2. In Terminal B, run your relay targeting localhost:
   ```bash
   socat UDP4-RECVFROM:1234,ip-add-membership=239.1.1.1:0.0.0.0,fork UDP4-SENDTO:127.0.0.1:5678
   ```
If data immediately fills Terminal A, your `socat` internal logic is completely sound.

---

## 4. Troubleshooting Firewalls (Debian vs RHEL)

If `tcpdump` shows traffic entering and leaving but your target application still isn't getting data, the OS firewall is likely dropping the packets silently.

### On Debian/Ubuntu (`ufw`):
Allow incoming multicast traffic on the designated port:
```bash
sudo ufw allow 1234/udp
```

### On RHEL (`firewalld`):
RHEL is strict about zones and unprompted UDP traffic. Add the runtime and permanent rules to your active zone:
```bash
sudo firewall-cmd --zone=public --add-port=1234/udp --permanent
sudo firewall-cmd --reload
```
