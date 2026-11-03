Red Hat build of MicroShift 4.22
Networking
Configuring and managing cluster networking
Last Updated: 2026-10-29

Red Hat build of MicroShift 4.22 Networking
Configuring and managing cluster networking

Legal Notice
Copyright © Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by
Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you
distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert,
Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of
Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux ® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its
subsidiaries in the United States and other countries.
The OpenStack ® Word Mark and OpenStack logo are trademarks or registered trademarks of the
Linux Foundation, used under license.
All other trademarks are the property of their respective owners.
Abstract
This document provides instructions for configuring and managing your MicroShift cluster network,
including DNS, ingress, and the Pod network.

Table of Contents
Table of Contents
.C . H. .A . P. .T .E . R. . 1.. .A . B. .O . .U . T. . T. H. .E . .O . .V . N. .- .K . U. .B . E. R. .N . .E .T . E. .S . N. . E. T. .W . .O . .R .K . .P . L. .U . G. .I .N . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1. MICROSHIFT DEFAULT NETWORKING PLUGIN 5
1.2. MICROSHIFT NETWORKING CONFIGURATION MATRIX 5
1.2.1. Default settings 7
1.3. NETWORK FEATURES 10
1.3.1. IP forward 10
1.4. NETWORK PERFORMANCE OPTIMIZATIONS 10
1.5. MICROSHIFT NETWORKING COMPONENTS AND SERVICES 11
1.6. BRIDGE MAPPINGS 12
1.7. NETWORK TOPOLOGY 12
1.7.1. Description of the OVN logical components of the virtualized network 13
1.7.2. Description of the connections in the network topology figure 14
1.8. ADDITIONAL RESOURCES 14
.C . H. .A . P. .T .E . R. . 2. .. U. .N . .D . E. .R .S . T. .A . N. .D . I.N . .G . .N . E. .T . W. . O. .R . K. .I N. .G . . S. E. .T . T. .I N. .G . S. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1. 5. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1. CREATE AN OVN-KUBERNETES CONFIGURATION FILE 15
2.2. RESTART THE OVNKUBE-MASTER POD 16
2.3. DEPLOY MICROSHIFT BEHIND AN HTTP OR HTTPS PROXY 16
2.4. USE THE RPM-OSTREE HTTP OR HTTPS PROXY 17
2.5. USING A PROXY IN THE CRI-O CONTAINER RUNTIME 17
2.6. GETTING A SNAPSHOT OF OVS INTERFACES FROM A RUNNING NODE 18
2.7. THE MICROSHIFT LOADBALANCER SERVICE FOR WORKLOADS 19
2.7.1. Deploying a load balancer for an application 19
2.8. BLOCKING EXTERNAL ACCESS TO THE NODEPORT SERVICE ON A SPECIFIC HOST INTERFACE 23
2.9. THE MULTICAST DNS PROTOCOL 24
2.10. AUDITING EXPOSED NETWORK PORTS 24
2.10.1. hostNetwork 24
2.10.2. hostPort 25
2.10.3. NodePort and LoadBalancer services 25
.C . H. .A . P. .T .E . R. . 3. .. U. . N. .D . E. .R . S. T. .A . N. .D . I. N. .G . .A . N. .D . . C. .O . N. .F . I.G . .U . R. .I N. .G . .T . H. .E . .R . O. .U . T. .E . R. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2 . 7. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1. ABOUT CONFIGURING THE ROUTER 27
3.1.1. Router settings and valid values 27
3.2. DISABLE THE ROUTER 28
3.3. CONFIGURE ROUTER INGRESS 29
3.3.1. Configure router ports 29
3.3.2. Configure router IP addresses 30
3.4. ADDITIONAL RESOURCES 32
3.5. CONFIGURE THE ROUTE ADMISSION POLICY 32
.C . H. .A . P. .T .E . R. . 4. .. .U . S. .I N. .G . .T . H. .E . .S . R. -. I. O. .V . .N . E. .T . W. . O. .R . K. . O. .P . E. .R . A. .T .O . .R . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3 .4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1. UNDERSTAND THE SR-IOV NETWORK OPERATOR 34
4.2. INSTALL THE SR-IOV NETWORK OPERATOR 34
4.3. SR-IOV NETWORK OPERATOR SUPPORTED DEVICES 39
4.4. ADDITIONAL RESOURCES 40
.C . H. .A . P. .T .E . R. . 5. .. N. . E. T. .W . .O . .R .K . .P . O. . L. I.C . .I E. S. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4. .1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1. ABOUT NETWORK POLICIES 41
5.1.1. How network policy works in MicroShift 41
5.1.2. Optimizations for network policy with OVN-Kubernetes network plugin 43
5.1.2.1. NetworkPolicy CR and external IPs in OVN-Kubernetes 45
5.2. CREATING NETWORK POLICIES 46
1

Red Hat build of MicroShift 4.22 Networking
5.2.1. Example NetworkPolicy object 46
5.2.2. Create a network policy using the CLI 47
5.2.3. Create a default deny all network policy 49
5.2.4. Create a network policy to allow traffic from external clients 50
5.2.5. Create a network policy allowing traffic to an application from all namespaces 50
5.2.5.1. Create a network policy allowing traffic to an application from a namespace 52
5.3. EDITING A NETWORK POLICY 55
5.3.1. Edit a network policy 55
5.3.2. Example NetworkPolicy object 56
5.4. DELETING A NETWORK POLICY 57
5.4.1. Delete a network policy using the CLI 57
5.5. VIEWING A NETWORK POLICY 57
5.5.1. View network policies using the CLI 58
.C . H. .A . P. .T .E . R. . 6. .. .M . U. .L . T. .I P. .L . E. .N . .E .T . W. . O. .R . K. .S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5 . 9. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1. ABOUT USING MULTIPLE NETWORKS 59
6.1.1. Secondary networks in MicroShift 59
6.1.1.1. Supported secondary networks for network isolation 59
6.1.1.2. Use case: Secondary networks for network isolation 59
6.1.1.3. How secondary networks are implemented 60
6.1.1.4. How to attach secondary networks to pods 60
6.1.1.5. Configurations for secondary network types 60
6.1.2. Install the Multus CNI plugin on a running node 60
6.1.3. Configuration for a bridge secondary network 61
6.1.3.1. Bridge CNI plugin configuration example 63
6.1.4. Configuration for an IPVLAN secondary network 63
6.1.4.1. IPVLAN CNI plugin configuration example 64
6.1.5. Configuration for a MACVLAN secondary network 65
6.1.5.1. MACVLAN CNI plugin configuration example 66
6.1.6. Additional resources 66
6.2. CONFIGURING AND USING MULTIPLE NETWORKS 66
6.2.1. IP address management types and additional networks 66
6.2.1.1. bridge interface specifics 66
6.2.1.2. macvlan interface specifics 67
6.2.1.3. ipvlan interface specifics 67
6.2.2. Create a NetworkAttachmentDefinition for an additional network 67
6.2.3. Add a pod to an additional network 69
6.2.4. Configure an additional network 72
6.2.5. Remove a pod from a secondary network 74
6.2.6. Troubleshoot Multus networking 75
6.2.6.1. Pod networking cannot be configured 75
6.2.6.2. Missing configuration file 75
6.2.7. Additional resources 76
.C . H. .A . P. .T .E . R. . 7. .. C. .O . .N . F. .I G. .U . .R .I .N . G. . R. .O . .U . T. E. .S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7 . 7. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1. CREATE AN HTTP-BASED ROUTE 77
7.2. HTTP STRICT TRANSPORT SECURITY 78
7.3. ENABLE HTTP STRICT TRANSPORT SECURITY PER-ROUTE 79
7.3.1. Disable HTTP Strict Transport Security per-route 80
7.3.2. Enforce HTTP Strict Transport Security per-domain 81
7.4. THROUGHPUT ISSUE TROUBLESHOOTING METHODS 81
7.5. USE COOKIES TO KEEP ROUTE STATEFULNESS 82
7.5.1. Annotate a route with a cookie 83
2

Table of Contents
7.6. PATH-BASED ROUTES 84
7.7. HTTP HEADER CONFIGURATION 84
7.8. SET OR DELETE HTTP REQUEST AND RESPONSE HEADERS IN A ROUTE 86
7.9. CREATE A ROUTE THROUGH AN INGRESS OBJECT 88
7.10. CREATE A ROUTE USING THE DEFAULT CERTIFICATE THROUGH AN INGRESS OBJECT 90
7.11. CREATE A ROUTE USING THE DESTINATION CA CERTIFICATE IN THE INGRESS ANNOTATION 92
.C . H. .A . P. .T .E . R. . 8. .. .U . S. I. N. .G . .A . .F . I.R . E. .W . .A . L. L. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9 .4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.1. ABOUT NETWORK TRAFFIC THROUGH THE FIREWALL 94
8.2. INSTALL THE FIREWALLD SERVICE 94
8.3. REQUIRED FIREWALL SETTINGS 95
8.3.1. Example commands 95
8.4. USE OPTIONAL PORT SETTINGS 95
8.4.1. Optional ports 96
8.5. ADD SERVICES TO OPEN PORTS 96
8.6. ALLOWING NETWORK TRAFFIC THROUGH THE FIREWALL 97
8.7. APPLYING FIREWALL SETTINGS 97
8.8. VERIFY FIREWALL SETTINGS 97
8.9. OVERVIEW OF FIREWALL PORTS WHEN A SERVICE IS EXPOSED 98
8.10. ADDITIONAL RESOURCES 98
8.11. KNOWN FIREWALL ISSUE 98
.C . H. .A . P. .T .E . R. . 9. .. .C . O. .N . F. .I G. . U. .R . I.N . G. . N. . E. T. .W . .O . .R .K . .S . E. .T .T . I.N . .G . S. . F. O. . R. . F. U. .L . L. .Y . .D . I.S . C. .O . N. . N. .E .C . .T .E . D. . H. .O . .S . T. S. . . . . . . . . . . . . . . . . . .1 0. .0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9.1. PREPARING NETWORKING FOR FULLY DISCONNECTED HOSTS 100
9.1.1. Procedure summary 100
9.2. RESTORING MICROSHIFT NETWORKING SETTINGS TO DEFAULT 101
9.3. CONFIGURING THE NETWORKING SETTINGS FOR FULLY DISCONNECTED HOSTS 101
3

Red Hat build of MicroShift 4.22 Networking
4

CHAPTER 1. ABOUT THE OVN-KUBERNETES NETWORK PLUGIN
CHAPTER 1. ABOUT THE OVN-KUBERNETES NETWORK
PLUGIN
You can use the OVN-Kubernetes Network Interface to create and manage network connections for
internet-connected nodes.
1.1. MICROSHIFT DEFAULT NETWORKING PLUGIN
The OVN-Kubernetes Container Network Interface (CNI) plugin is the default networking solution for a
MicroShift node. OVN-Kubernetes is a virtualized network for pods and services that is based on Open
Virtual Network (OVN).
Changing the CNI is not supported on MicroShift.
Default network configuration and connections are applied automatically in MicroShift with the
microshift-networking RPM during installation.
A node that uses the OVN-Kubernetes network plugin also runs Open vSwitch (OVS) on the
node.
OVN-K configures OVS on the node to implement the declared network configuration.
Host physical interfaces are not bound by default to the OVN-K gateway bridge, br-ex. You can
use standard tools on the host for managing the default gateway, such as the Network Manager
CLI (nmcli).
Using configuration files or custom scripts, you can configure the following networking settings:
You can use subnet CIDR ranges to allocate IP addresses to pods.
You can change the maximum transmission unit (MTU) value.
You can configure firewall ingress and egress.
You can define network policies in the MicroShift, including ingress and egress rules.
You can use the MicroShift Multus plugin to chain other CNI plugins.
You can configure or remove the ingress router.
1.2. MICROSHIFT NETWORKING CONFIGURATION MATRIX
The following table summarizes the status of networking features and capabilities that are either
present as defaults, supported for configuration, or not available with the MicroShift service:
Table 1.1. MicroShift networking features and capabilities overview
Network capability Availability Configuration supported
Advertise address Yes Yes
Kubernetes network policy Yes Yes
5

Red Hat build of MicroShift 4.22 Networking
| Network capability             | Availability  | Configuration supported |
| ------------------------------ | ------------- | ----------------------- |
| Kubernetes network policy logs | Not available | N/A                     |
| Load balancing                 | Yes           | Yes                     |
| Multicast DNS                  | Yes           | Yes                     |
| Network proxies                | Yes           | CRI-O                   |
| Network performance            | Yes           | MTU configuration       |
| Egress IPs                     | Not available | N/A                     |
| Egress firewall                | Not available | N/A                     |
| Egress router                  | Not available | N/A                     |
| Firewall                       | No            | Yes                     |
| Hardware offloading            | Not available | N/A                     |
| Hybrid networking              | Not available | N/A                     |
IPsec encryption for intra-cluster communication Not available N/A
| IPv6                     | Supported | N/A |
| ------------------------ | --------- | --- |
| Ingress router           | Yes       | Yes |
| Multiple networks plugin | Yes       | Yes |
Additional details about networking capabilities
Advertise address: If unset, the default value is set to the next immediate subnet after the
service network. For example, when the service network is 10.43.0.0/16, the
advertiseAddress is set to 10.44.0.0/32.
Multicast DNS: You can use the multicast DNS protocol (mDNS) to allow name resolution
and service discovery within a Local Area Network (LAN) using multicast exposed on the
5353/UDP port.
Network proxies: There is no built-in transparent proxying of egress traffic in MicroShift.
Egress must be manually configured.
Firewall: Setting up the firewalld service is supported by RHEL for Edge.
IPv6: Is supported in both single-stack and dual-stack networks with the OVN-Kubernetes
6

CHAPTER 1. ABOUT THE OVN-KUBERNETES NETWORK PLUGIN
IPv6: Is supported in both single-stack and dual-stack networks with the OVN-Kubernetes
network plugin. You can also use IPv6 by connecting to other networks with the MicroShift
Multus CNI plugin.
Ingress router: Configure by using the MicroShift config.yaml file.
1.2.1. Default settings
IMPORTANT
Technology Preview features are not supported with Red Hat production service level
agreements (SLAs) and might not be functionally complete. Red Hat does not
recommend using them in production. These features provide early access to upcoming
product features, enabling customers to test functionality and provide feedback during
the development process.
For more information about the support scope of Red Hat Technology Preview features,
see Technology Preview Features Support Scope.
When no config.yaml or configuration snippet exists, MicroShift uses built-in default values. To view
these defaults, run microshift show-config.
The following example shows the default configuration settings.
Procedure
To see the default values, run the following command:
$ microshift show-config
Default values example output in YAML form
apiServer:
advertiseAddress: 10.44.0.0/32
auditLog:
maxFileAge: 0
maxFileSize: 200
maxFiles: 10
profile: Default
namedCertificates:
- certPath: ""
keyPath: ""
names:
- ""
subjectAltNames: []
tls:
cipherSuites:
minVersion: VersionTLS12
debugging:
logLevel: "Normal"
dns:
baseDomain: microshift.example.com
etcd:
7

Red Hat build of MicroShift 4.22 Networking
memoryLimitMB: 0
genericDevicePlugin:
devices:
- groups:
- count: 1
paths:
- limit: 1
mountPath: /dev/ttyACM0
path: /dev/ttyACM0
permissions: mrw
readOnly: false
type: Device
usbs:
- product: ""
serial: ""
vendor: ""
name: serial
domain: device.microshift.io
status: Disabled
ingress:
accessLogging:
destination:
type:
container:
maxLength: 1024
syslog:
address: ""
facility: ""
maxLength: 1024
port: 0
type: ""
httpCaptureCookies:
- matchType: ""
maxLength: 0
name: ""
namePrefix: ""
httpCaptureHeaders:
request:
- maxLength: 0
name: ""
response:
- maxLength: 0
name: ""
httpLogFormat: ""
status: Disabled
certificateSecret: router-certs-default
clientTLS:
allowedSubjectPatterns:
clientCA:
name: ""
clientCertificatePolicy: ""
defaultHTTPVersion: 1
forwardedHeaderPolicy: ""
httpCompression:
mimeTypes:
- ""
8

CHAPTER 1. ABOUT THE OVN-KUBERNETES NETWORK PLUGIN
httpEmptyRequestsPolicy: Respond
httpErrorCodePages:
name: ""
listenAddress: []
logEmptyRequests: Log
ports:
http: 80
https: 443
routeAdmissionPolicy:
namespaceOwnership: InterNamespaceAllowed
wildcardPolicy: WildcardPolicyAllowed
status: Managed
tlsSecurityProfile:
type: Intermediate
tuningOptions:
clientFinTimeout: "1s"
clientTimeout: "30s"
headerBufferBytes: 0
headerBufferMaxRewriteBytes: 0
healthCheckInterval: "5s"
maxConnections: 0
serverFinTimeout: "1s"
serverTimeout: "30s"
threadCount: 0
tlsInspectDelay: "5s"
tunnelTimeout: "1h"
kubelet:
manifests:
kustomizePaths:
- /usr/lib/microshift/manifests
- /usr/lib/microshift/manifests.d/*
- /etc/microshift/manifests
- /etc/microshift/manifests.d/*
network:
clusterNetwork:
- 10.42.0.0/16
cniPlugin: ""
multus:
status: Disabled
serviceNetwork:
- 10.43.0.0/16
serviceNodePortRange: 30000-32767
node:
hostnameOverride: ""
nodeIP: ""
nodeIPv6: ""
storage:
driver: ""
optionalCsiComponents:
- ""
telemetry:
endpoint: https://infogw.api.openshift.com
proxy: ""
status: Enabled
where:
9

Red Hat build of MicroShift 4.22 Networking
apiserver.advertiseAddress
Specifies the address of the service network.
network.multus.status
Specifies the status of the Multus Container Network Interface (CNI).
node.nodeIP
Specifies the IP address of the default route.
storage.driver
Specifies the storage driver to use. Default null value deploys Logical Volume Managed
Storage (LVMS).
storage.optionalCsiComponents
Specifies the CSI components to deploy. Default null value deploys snapshot-controller.
1.3. NETWORK FEATURES
Understand which networking feature are available and which are not for your MicroShift deployments.
Networking features available with MicroShift 4.22 include:
Kubernetes network policy
Dynamic node IP
Custom gateway interface
Second gateway interface
Node network on specified host interface
Blocking external access to NodePort service on specific host interfaces
Networking features not available with MicroShift 4.22:
Egress IP/firewall/QoS: disabled
Hybrid networking: not supported
IPsec: not supported
Hardware offload: not supported
1.3.1. IP forward
You must use ip_forward to access network connectivity.
The host network sysctl net.ipv4.ip_forward kernel parameter is automatically enabled by the
ovnkube-master container when started. This is required to forward incoming traffic to the CNI. For
example, accessing the NodePort service from outside of a node fails if ip_forward is disabled.
1.4. NETWORK PERFORMANCE OPTIMIZATIONS
By default, three performance optimizations are applied to OVS services to minimize resource
consumption:
10

CHAPTER 1. ABOUT THE OVN-KUBERNETES NETWORK PLUGIN
CPU affinity to ovs-vswitchd.service and ovsdb-server.service
no-mlockall to openvswitch.service
Limit handler and revalidator threads to ovs-vswitchd.service
1.5. MICROSHIFT NETWORKING COMPONENTS AND SERVICES
Understand networking components and services and their operation in MicroShift.
NOTE
The microshift-networking RPM is a package that automatically pulls in any networking-
related dependencies and systemd services to initialize networking, for example, the
microshift-ovs-init systemd service.
NetworkManager
NetworkManager is required to set up the initial gateway bridge on the MicroShift node. The
NetworkManager and NetworkManager-ovs RPM packages are installed as dependencies to the
microshift-networking RPM package, which contains the necessary configuration files.
NetworkManager in MicroShift uses the keyfile plugin and is restarted after installation of the
microshift-networking RPM package.
microshift-ovs-init
The microshift-ovs-init.service is installed by the microshift-networking RPM package as a
dependent systemd service to microshift.service. It is responsible for setting up the OVS gateway
bridge.
OVN containers
Two OVN-Kubernetes daemon sets are rendered and applied by MicroShift.
ovnkube-master Includes the northd, nbdb, sbdb and ovnkube-master containers.
ovnkube-node The ovnkube-node includes the OVN-Controller container.
After MicroShift starts, the OVN-Kubernetes daemon sets are deployed in the openshift-
ovn-kubernetes namespace.
Packaging
OVN-Kubernetes manifests and startup logic are built into MicroShift. The systemd services and
configurations included in the microshift-networking RPM are:
/etc/NetworkManager/conf.d/microshift-nm.conf for NetworkManager.service
/etc/systemd/system/ovs-vswitchd.service.d/microshift-cpuaffinity.conf for ovs-
vswitchd.service
/etc/systemd/system/ovsdb-server.service.d/microshift-cpuaffinity.conf for ovs-
server.service
/usr/bin/configure-ovs-microshift.sh for microshift-ovs-init.service
/usr/bin/configure-ovs.sh for microshift-ovs-init.service
/etc/crio/crio.conf.d/microshift-ovn.conf for the CRI-O service
11

Red Hat build of MicroShift 4.22 Networking
1.6. BRIDGE MAPPINGS
Understand how provider network traffic reaches the physical network through bridge mappings. The
following concepts apply:
Traffic leaves the provider network and arrives at the br-int bridge.
A patch port between br-int and br-ex then allows the traffic to traverse to and from the
provider network and the edge network.
Kubernetes pods are connected to the br-int bridge through a virtual ethernet pair. One end of
the virtual ethernet pair is attached to the pod namespace, and the other end is attached to the
br-int bridge.
1.7. NETWORK TOPOLOGY
OVN-Kubernetes provides an overlay-based networking implementation. This overlay includes an OVS-
based implementation of Service and NetworkPolicy resources.
The overlay network uses the Geneve (Generic Network Virtualization Encapsulation) tunnel protocol.
The pod maximum transmission unit (MTU) for the Geneve tunnel is set to the default route MTU if it is
not configured.
To configure the MTU, you must set an equal-to or less-than value than the MTU of the physical
interface on the host. A less-than value for the MTU makes room for the required information that is
added to the tunnel header before it is transmitted.
IMPORTANT
The MTU value of the OVN overlay networking in MicroShift must be 100 bytes smaller
than the MTU value of the base network. If no MTU value is configured, MicroShift
autoconfigures the value using the MTU value of the default gateway (Internet Protocol
version 4 (IPv4) or Internet Protocol version 6 (IPv6)) of the host. If the auto-
configuration does not work correctly, the MTU value can be configured manually. For
example, if the MTU value of the network is 9000, the OVN MTU size must be set to 8900.
OVS runs as a systemd service on the MicroShift node. The OVS RPM package is installed as a
dependency to the microshift-networking RPM package. OVS starts immediately when the microshift-
networking RPM is installed.
12

CHAPTER 1. ABOUT THE OVN-KUBERNETES NETWORK PLUGIN
1.7.1. Description of the OVN logical components of the virtualized network
OVN node switch
A virtual switch named <node-name>. The OVN node switch is named according to the hostname of
the node.
In this example, the node-name is microshift-dev.
OVN cluster router
A virtual router named ovn_cluster_router, also known as the distributed router.
In this example, the node network is 10.42.0.0/16.
OVN join switch
A virtual switch named join.
13

Red Hat build of MicroShift 4.22 Networking
OVN gateway router
A virtual router named GR_<node-name>, also known as the external gateway router.
OVN external switch
A virtual switch named ext_<node-name>.
1.7.2. Description of the connections in the network topology figure
The north-south traffic between the network service and the OVN external switch
ext_microshift-dev is provided through the host kernel by the gateway bridge br-ex.
The OVN gateway router GR_microshift-dev is connected to the external network switch
ext_microshift-dev through the logical router port 4. Port 4 is attached with the node IP
address 192.168.122.14.
The join switch join connects the OVN gateway router GR_microshift-dev to the OVN cluster
router ovn_cluster_router. The IP address range is 100.62.0.0/16.
The OVN gateway router GR_microshift-dev connects to the OVN join switch join through
the logical router port 3. Port 3 attaches with the internal IP address 100.64.0.2.
The OVN cluster router ovn_cluster_router connects to the join switch join through the
logical router port 2. Port 2 attaches with the internal IP address 100.64.0.1.
The OVN cluster router ovn_cluster_router connects to the node switch microshift-dev
through the logical router port 1. Port 1 is attached with the OVN cluster network IP address
10.42.0.1.
The east-west traffic between the pods and the network service is provided by the OVN cluster
router ovn_cluster_router and the node switch microshift-dev. The IP address range is
10.42.0.0/24.
The east-west traffic between pods is provided by the node switch microshift-dev without
network address translation (NAT).
The north-south traffic between the pods and the external network is provided by the OVN
cluster router ovn_cluster_router and the host network. This router is connected through the
ovn-kubernetes management port ovn-k8s-mp0, with the IP address 10.42.0.2.
All the pods are connected to the OVN node switch through their interfaces.
In this example, Pod 1 and Pod 2 are connected to the node switch through Interface 1 and
Interface 2.
1.8. ADDITIONAL RESOURCES
Customizing MicroShift by using the configuration file
Understanding networking settings
About using multiple networks
About network policies
14

CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
Learn how to apply networking customization and default settings to MicroShift deployments. Each
node is contained to a single machine and single MicroShift, so each deployment requires individual
configuration, pods, and settings.
MicroShift administrators have several options for exposing applications that run inside a node to
external traffic and securing network connections:
A service such as NodePort
API resources, such as Ingress and Route
By default, Kubernetes allocates each pod an internal IP address for applications running within the pod.
Pods and their containers can have traffic between them, but clients outside the node do not have
direct network access to pods except when exposed with a service such as NodePort.
2.1. CREATE AN OVN-KUBERNETES CONFIGURATION FILE
MicroShift uses built-in default OVN-Kubernetes values if an OVN-Kubernetes configuration file is not
created. To apply custom OVN-Kubernetes values such as pod mtu instead of using built-in defaults,
you can copy ovn.yaml.default to /etc/microshift/ovn.yaml and edit the file.
Procedure
1. To create your ovn.yaml file, run the following command:
$ sudo cp /etc/microshift/ovn.yaml.default /etc/microshift/ovn.yaml
2. To list the contents of the configuration file you created, run the following command:
$ cat /etc/microshift/ovn.yaml
Example YAML file with default maximum transmission unit (MTU) value
mtu: 1400
3. To customize your configuration, you can change the MTU value. The table that follows
provides details:
Table 2.1. Supported optional OVN-Kubernetes configurations for MicroShift
Field Type Default Description Example
mtu uint32 auto MTU value used 1300
for the pods
IMPORTANT
If you change the mtu configuration value in the ovn.yaml file, you must restart
the host that Red Hat build of MicroShift is running on to apply the updated
setting.
15

Red Hat build of MicroShift 4.22 Networking
Example custom ovn.yaml configuration file
mtu: 1300
2.2. RESTART THE OVNKUBE-MASTER POD
To replace the ovnkube-master pod with a new instance on MicroShift, you can delete the existing pod
in the openshift-ovn-kubernetes namespace. Confirm that a new pod appears when you list pods in
that namespace.
Prerequisites
The OpenShift CLI (oc) is installed.
You have root access to the node.
A node installed on infrastructure configured with the OVN-Kubernetes network plugin.
The KUBECONFIG environment variable is set.
Procedure
1. Access the remote node by running the following command:
$ export KUBECONFIG=$PWD/kubeconfig
2. Find the name of the ovnkube-master pod that you want to restart by running the following
command:
$ pod=$(oc get pods -n openshift-ovn-kubernetes | awk -F " " '/ovnkube-master/{print $1}')
3. Delete the ovnkube-master pod by running the following command:
$ oc -n openshift-ovn-kubernetes delete pod $pod
4. Confirm that a new ovnkube-master pod is running by using the following command:
$ oc get pods -n openshift-ovn-kubernetes
The listing of the running pods shows a new ovnkube-master pod name and age.
2.3. DEPLOY MICROSHIFT BEHIND AN HTTP OR HTTPS PROXY
To add basic anonymity and security measures to your pods, you can deploy MicroShift behind an HTTP
or HTTPS proxy.
You must configure the host operating system to use the proxy service with all components initiating
HTTP or HTTPS requests when deploying MicroShift behind a proxy.
All the user-specific workloads or pods with egress traffic, such as accessing cloud services, must be
configured to use the proxy. There is no built-in transparent proxying of egress traffic in MicroShift.
16

CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
2.4. USE THE RPM-OSTREE HTTP OR HTTPS PROXY
To use the HTTP or HTTPS proxy in RPM-OStree, add a Service section to the configuration file and
set the http_proxy environment variable for the rpm-ostreed service.
Procedure
1. Add this setting to the /etc/systemd/system/rpm-ostreed.service.d/00-proxy.conf file:
[Service]
Environment="http_proxy=http://$PROXY_USER:$PROXY_PASSWORD@$PROXY_SERVE
R:$PROXY_PORT/"
2. Next, reload the configuration settings and restart the service to apply your changes.
a. Reload the configuration settings by running the following command:
$ sudo systemctl daemon-reload
b. Restart the rpm-ostreed service by running the following command:
$ sudo systemctl restart rpm-ostreed.service
2.5. USING A PROXY IN THE CRI-O CONTAINER RUNTIME
To use an HTTP or HTTPS proxy in CRI-O, you can add a systemd Service drop-in file that defines the
HTTP_PROXY, HTTPS_PROXY, and optional NO_PROXY environment variables. You can reload
systemd, restart crio, and restart the MicroShift service so the proxy settings apply.
Procedure
1. Create the directory for the configuration file if it does not exist:
$ sudo mkdir /etc/systemd/system/crio.service.d/
2. Add the following settings to the /etc/systemd/system/crio.service.d/00-proxy.conf file:
[Service]
Environment=NO_PROXY="localhost,127.0.0.1"
Environment=HTTP_PROXY="http://$PROXY_USER:$PROXY_PASSWORD@$PROXY_SE
RVER:$PROXY_PORT/"
Environment=HTTPS_PROXY="http://$PROXY_USER:$PROXY_PASSWORD@$PROXY_S
ERVER:$PROXY_PORT/"
IMPORTANT
You must define the Service section of the configuration file for the
environment variables or the proxy settings fail to apply.
3. Reload the configuration settings:
17

Red Hat build of MicroShift 4.22 Networking
$ sudo systemctl daemon-reload
4. Restart the CRI-O service:
$ sudo systemctl restart crio
5. Restart the MicroShift service to apply the settings:
$ sudo systemctl restart microshift
Verification
1. Verify that pods are started by running the following command and examining the output:
$ oc get all -A
2. Verify that MicroShift is able to pull container images by running the following command and
examining the output:
$ sudo crictl images
2.6. GETTING A SNAPSHOT OF OVS INTERFACES FROM A RUNNING
NODE
To capture the current state of OVS interface and data from a running MicroShift node, you can run
sudo ovs-vsctl show on the node.
Procedure
To see a snapshot of OVS interfaces from a running MicroShift node, enter the following
command:
$ sudo ovs-vsctl show
Example OVS interfaces in a running node
9d9f5ea2-9d9d-4e34-bbd2-dbac154fdc93
Bridge br-ex
Port br-ex
Interface br-ex
type: internal
Port patch-br-ex_localhost.localdomain-to-br-int
Interface patch-br-ex_localhost.localdomain-to-br-int
type: patch
options: {peer=patch-br-int-to-br-ex_localhost.localdomain}
Bridge br-int
fail_mode: secure
datapath_type: system
Port patch-br-int-to-br-ex_localhost.localdomain
Interface patch-br-int-to-br-ex_localhost.localdomain
type: patch
options: {peer=patch-br-ex_localhost.localdomain-to-br-int}
18

CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
Port eebee1ce5568761
Interface eebee1ce5568761
Port b47b1995ada84f4
Interface b47b1995ada84f4
Port "3031f43d67c167f"
Interface "3031f43d67c167f"
Port br-int
Interface br-int
type: internal
Port ovn-k8s-mp0
Interface ovn-k8s-mp0
type: internal
ovs_version: "2.17.3"
where:
patch-br-ex_localhost.localdomain-to-br-int
Specifies OVS patch ports that connects br-int.
patch-br-int-to-br-ex_localhost.localdomain
Specifies OVS patch ports that connects br-ex.
eebee1ce5568761
Specifies the pod interface named with the first 15 bits of the pod sandbox ID and is plugged
into the br-int bridge.
b47b1995ada84f4
Specifies the pod interface named with the first 15 bits of the pod sandbox ID and is plugged
into the br-int bridge.
3031f43d67c167f
Specifies the pod interface named with the first 15 bits of the pod sandbox ID and is plugged
into the br-int bridge.
ovn-k8s-mp0
Specifies OVS internal port for hairpin traffic,ovn-k8s-mp0 is created by the ovnkube-
master container.
2.7. THE MICROSHIFT LOADBALANCER SERVICE FOR WORKLOADS
MicroShift has a built-in implementation of network load balancers that you can use for your workloads
and applications within the node. You can create a LoadBalancer service by configuring a pod to
interpret ingress rules and serve as an ingress controller.
2.7.1. Deploying a load balancer for an application
To expose an application through a LoadBalancer service that uses the node IP as the external IP in
MicroShift, you can create a namespace, deploy the example workload, and apply the service manifest.
Prerequisites
The OpenShift CLI (oc) is installed.
You installed a node on an infrastructure configured with the OVN-Kubernetes network plugin.
19

Red Hat build of MicroShift 4.22 Networking
The KUBECONFIG environment variable is set.
Procedure
1. Verify that your pods are running by entering the following command:
$ oc get pods -A
Example output
NAMESPACE NAME READY STATUS
RESTARTS AGE
default i-06166fbb376f14a8bus-west-2computeinternal-debug-qtwcr 1/1
Running 0 46m
kube-system csi-snapshot-controller-5c6586d546-lprv4 1/1
Running 0 51m
openshift-dns dns-default-45jl7 2/2 Running 0
50m
openshift-dns node-resolver-7wmzf 1/1 Running 0
51m
openshift-ingress router-default-78b86fbf9d-qvj9s 1/1 Running
0 51m
openshift-multus dhcp-daemon-j7qnf 1/1 Running 0
51m
openshift-multus multus-r758z 1/1 Running 0
51m
openshift-operator-lifecycle-manager catalog-operator-85fb86fcb9-t6zm7 1/1
Running 0 51m
openshift-operator-lifecycle-manager olm-operator-87656d995-fvz84 1/1
Running 0 51m
openshift-ovn-kubernetes ovnkube-master-5rfhh 4/4 Running
0 51m
openshift-ovn-kubernetes ovnkube-node-gcnt6 1/1 Running
0 51m
openshift-service-ca service-ca-bf5b7c9f8-pn6rk 1/1 Running
0 51m
openshift-storage topolvm-controller-549f7fbdd5-7vrmv 5/5
Running 0 51m
openshift-storage topolvm-node-rht2m 3/3 Running 0
50m
2. Create a namespace by running the following commands:
$ NAMESPACE=_<nginx_lb_test>_
Replace <nginx_lb_test> with the application namespace that you want to create.
$ oc create ns $NAMESPACE
The following example deploys three replicas of the test nginx application in the created
namespace:
oc apply -n $NAMESPACE -f - <<EOF
apiVersion: v1
20

CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
kind: ConfigMap
metadata:
name: nginx
data:
headers.conf: |
add_header X-Server-IP \$server_addr always;
---
apiVersion: apps/v1
kind: Deployment
metadata:
name: nginx
spec:
replicas: 3
selector:
matchLabels:
app: nginx
template:
metadata:
labels:
app: nginx
spec:
containers:
- image: quay.io/packit/nginx-unprivileged
imagePullPolicy: Always
name: nginx
ports:
- containerPort: 8080
volumeMounts:
- name: nginx-configs
subPath: headers.conf
mountPath: /etc/nginx/conf.d/headers.conf
securityContext:
allowPrivilegeEscalation: false
seccompProfile:
type: RuntimeDefault
capabilities:
drop: ["ALL"]
runAsNonRoot: true
volumes:
- name: nginx-configs
configMap:
name: nginx
items:
- key: headers.conf
path: headers.conf
EOF
3. You can verify that the three sample replicas started successfully by running the following
command:
$ oc get pods -n $NAMESPACE
4. Create a LoadBalancer service for the nginx test application by running the following
command:
21

Red Hat build of MicroShift 4.22 Networking
oc create -n $NAMESPACE -f - <<EOF
apiVersion: v1
kind: Service
metadata:
name: nginx
spec:
ports:
- port: 81
targetPort: 8080
selector:
app: nginx
type: LoadBalancer
EOF
NOTE
You must ensure that the port parameter is a host port that is not occupied by
other LoadBalancer services or MicroShift components.
5. Verify that the service file exists, that the external IP address is properly assigned, and that the
external IP is identical to the node IP by running the following command:
$ oc get svc -n $NAMESPACE
Example output
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
nginx LoadBalancer 10.43.183.104 192.168.1.241 81:32434/TCP 2m
Verification
The following command forms five connections to the example nginx application by using the external
IP address of the LoadBalancer service configuration. The result of the command is a list of those
server IP addresses.
Verify that the load balancer sends requests to all the running applications by running the
following command:
EXTERNAL_IP=192.168.1.241
seq 5 | xargs -Iz curl -s -I http://$EXTERNAL_IP:81 | grep X-Server-IP
The output of the previous command contains different IP addresses if the LoadBalancer
service is successfully distributing the traffic to the applications, for example:
Example output
X-Server-IP: 10.42.0.41
X-Server-IP: 10.42.0.41
X-Server-IP: 10.42.0.43
X-Server-IP: 10.42.0.41
X-Server-IP: 10.42.0.43
2.8. BLOCKING EXTERNAL ACCESS TO THE NODEPORT SERVICE ON
22

CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
2.8. BLOCKING EXTERNAL ACCESS TO THE NODEPORT SERVICE ON
A SPECIFIC HOST INTERFACE
OVN-Kubernetes does not restrict the host interface where a NodePort service can be accessed from
outside a Red Hat build of MicroShift node. To block the NodePort service on a specific host interface
and restrict external access, you can insert a drop rule for the port and IP on the node.
Prerequisites
You must have an account with root privileges.
Procedure
1. Change the NODEPORT variable to the host port number assigned to your Kubernetes
NodePort service by running the following command:
# export NODEPORT=30700
2. Change the INTERFACE_IP value to the IP address from the host interface that you want to
block. For example:
# export INTERFACE_IP=192.168.150.33
3. Insert a new rule in the nat table PREROUTING chain to drop all packets that match the
destination port and IP address. For example:
$ sudo nft -a insert rule ip nat PREROUTING tcp dport $NODEPORT ip daddr
$INTERFACE_IP drop
4. List the new rule by running the following command:
$ sudo nft -a list chain ip nat PREROUTING
table ip nat {
chain PREROUTING { # handle 1
type nat hook prerouting priority dstnat; policy accept;
tcp dport 30700 ip daddr 192.168.150.33 drop # handle 134
counter packets 108 bytes 18074 jump OVN-KUBE-ETP # handle 116
counter packets 108 bytes 18074 jump OVN-KUBE-EXTERNALIP # handle 114
counter packets 108 bytes 18074 jump OVN-KUBE-NODEPORT # handle 112
}
}
NOTE
Note the handle number of the newly added rule. You need to remove the
handle number in the following step.
5. Remove the custom rule with the following sample command:
$ sudo nft -a delete rule ip nat PREROUTING handle 134
23

Red Hat build of MicroShift 4.22 Networking
2.9. THE MULTICAST DNS PROTOCOL
To allow name resolution and service discovery within a Local Area Network (LAN) using multicast
exposed on the 5353/UDP port, you can use the multicast DNS protocol (mDNS).
MicroShift includes an embedded mDNS server for deployment scenarios in which the authoritative
DNS server cannot be reconfigured to point clients to services on MicroShift. The embedded DNS
server allows .local domains exposed by MicroShift to be discovered by other elements on the LAN.
2.10. AUDITING EXPOSED NETWORK PORTS
On MicroShift, the host port can be opened by a workload in the following cases. You can check logs to
view the network services.
2.10.1. hostNetwork
When a pod is configured with the hostNetwork:true setting, the pod is running in the host network
namespace. This configuration can independently open host ports. MicroShift component logs cannot
be used to track this case, the ports are subject to firewalld rules.
If the port opens in firewalld, you can view the port opening in the firewalld debug log.
Prerequisites
You have root user access to your build host.
Procedure
1. Optional: You can check that the hostNetwork:true parameter is set in your ovnkube-node pod
by using the following example command:
$ sudo oc get pod -n openshift-ovn-kubernetes <ovnkube-node-pod-name> -o json | jq -r
'.spec.hostNetwork' true
2. Enable debug in the firewalld log by running the following command:
$ sudo vi /etc/sysconfig/firewalld
FIREWALLD_ARGS=--debug=10
3. Restart the firewalld service:
$ sudo systemctl restart firewalld.service
4. To verify that the debug option was added properly, run the following command:
$ sudo systemd-cgls -u firewalld.service
The firewalld debug log is stored in the /var/log/firewalld path.
Example logs for when the port open rule is added
2023-06-28 10:46:37 DEBUG1: config.getZoneByName('public')
2023-06-28 10:46:37 DEBUG1: config.zone.7.addPort('8080', 'tcp')
24

CHAPTER 2. UNDERSTANDING NETWORKING SETTINGS
2023-06-28 10:46:37 DEBUG1: config.zone.7.getSettings()
2023-06-28 10:46:37 DEBUG1: config.zone.7.update('...')
2023-06-28 10:46:37 DEBUG1: config.zone.7.Updated('public')
Example logs for when the port open rule is removed
2023-06-28 10:47:57 DEBUG1: config.getZoneByName('public')
2023-06-28 10:47:57 DEBUG2: config.zone.7.Introspect()
2023-06-28 10:47:57 DEBUG1: config.zone.7.removePort('8080', 'tcp')
2023-06-28 10:47:57 DEBUG1: config.zone.7.getSettings()
2023-06-28 10:47:57 DEBUG1: config.zone.7.update('...')
2023-06-28 10:47:57 DEBUG1: config.zone.7.Updated('public')
2.10.2. hostPort
To access host port open and close activity for workloads that use hostPort on MicroShift, you can run
journalctl -u crio and filter for lines that contain local port.
Procedure
You can access the logs by running the following command:
$ journalctl -u crio | grep "local port"
Example CRI-O logs when the host port is opened
$ Jun 25 16:27:37 rhel92 crio[77216]: time="2023-06-25 16:27:37.033003098+08:00"
level=info msg="Opened local port tcp:443"
Example CRI-O logs when the host port is closed
$ Jun 25 16:24:11 rhel92 crio[77216]: time="2023-06-25 16:24:11.342088450+08:00"
level=info msg="Closing host port tcp:443"
2.10.3. NodePort and LoadBalancer services
OVN-Kubernetes opens host ports for NodePort and LoadBalancer service types. These services add
iptables rules that take the ingress traffic from the host port and forwards it to the node IP address.
Logs for the NodePort and LoadBalancer services are presented in the following examples.
Procedure
1. To access the name of your ovnkube-master pods, run the following command:
$ oc get pods -n openshift-ovn-kubernetes | awk '/ovnkube-master/{print $1}'
Example ovnkube-master pod name
ovnkube-master-n2shv
2. You can access the NodePort and LoadBalancer services logs using your ovnkube-master
25

Red Hat build of MicroShift 4.22 Networking
2. You can access the NodePort and LoadBalancer services logs using your ovnkube-master
pod and running the following example command:
$ oc logs -n openshift-ovn-kubernetes <ovnkube_master_podname> ovnkube-master | grep -
E "OVN-KUBE-NODEPORT|OVN-KUBE-EXTERNALIP"
Example NodePort service logs in the ovnkube-master container of the ovnkube-
master pod when a host port is open
$ I0625 09:07:00.992980 2118395 iptables.go:27] Adding rule in table: nat, chain: OVN-
KUBE-NODEPORT with args: "-p TCP -m addrtype --dst-type LOCAL --dport 32718 -j DNAT
--to-destination 10.96.178.142:8081" for protocol: 0
Example NodePort service logs in the ovnkube-master container of the ovnkube-
master pod when a host port is closed
$ Deleting rule in table: nat, chain: OVN-KUBE-NODEPORT with args: "-p TCP -m addrtype -
-dst-type LOCAL --dport 32718 -j DNAT --to-destination 10.96.178.142:8081" for protocol: 0
Example LoadBalancer service logs in the ovnkube-master container of the ovnkube-
master pod when a host port is open
$ I0625 09:34:10.406067 128902 iptables.go:27] Adding rule in table: nat, chain: OVN-
KUBE-EXTERNALIP with args: "-p TCP -d 172.16.47.129 --dport 8081 -j DNAT --to-
destination 10.43.114.94:8081" for protocol: 0
Example LoadBalancer service logs in the ovnkube-master container of the ovnkube-
master pod when a host port is closed
$ I0625 09:37:00.976953 128902 iptables.go:63] Deleting rule in table: nat, chain: OVN-
KUBE-EXTERNALIP with args: "-p TCP -d 172.16.47.129 --dport 8081 -j DNAT --to-
destination 10.43.114.94:8081" for protocol: 0
26

CHAPTER 3. UNDERSTANDING AND CONFIGURING THE ROUTER
CHAPTER 3. UNDERSTANDING AND CONFIGURING THE
ROUTER
To control how external traffic reaches your applications and limit ingress exposure in MicroShift, you
can configure router listen addresses, ports, IP bindings, and route admission policy.
3.1. ABOUT CONFIGURING THE ROUTER
To make ingress optional, you can configure MicroShift ingress router settings to manage which ports, if
any, are exposed to network traffic. Specified routing is an example of ingress load balancing.
The default ingress router is always on, running on all IP addresses on the http: 80 and https:
443 ports.
Default router settings allow access to any namespace.
Some applications running on top of MicroShift might not require the default router and instead create
their own. You can configure the router to control both ingress and namespace access.
TIP
You can check for the presence of the default router in your MicroShift installation before you begin
configurations by using the oc get deployment -n openshift-ingress command, which returns the
following output:
NAME READY UP-TO-DATE AVAILABLE AGE
router-default 1/1 1 1 2d23h
3.1.1. Router settings and valid values
Valid values and defaults for ingress router fields in the config.yaml file on MicroShift cover
listenAddress, ports, routeAdmissionPolicy, and status.
Example config.yaml router settings
# ...
ingress:
listenAddress:
- ""
ports:
http: 80
https: 443
routeAdmissionPolicy:
namespaceOwnership: InterNamespaceAllowed
status: Managed
# ...
where:
ingress.listenAddress
Specifies the single IP address or host name or a list of IP addresses or host names. The default
value is the entire network of the host.
27

Red Hat build of MicroShift 4.22 Networking
ingress.ports
Specifies a single, unique port in the 1 to 65535 range. The values of the ports.http and ports.https
fields cannot be the same.
ingress.routeAdmissionPolicy.namespaceOwnership
Specifies whether routes can claim different paths of the same host name across namespaces. The
default value is InterNamespaceAllowed.
ingress.status
Specifies whether the ingress ports remain open. The default value is Managed.
IMPORTANT
The firewalld service is bypassed by the default MicroShift router and by configurations
that enable the router. Ingress and egress must be controlled by setting network policies
when the router is active.
3.2. DISABLE THE ROUTER
To disable the router in MicroShift when inbound services are not required, including in industrial IoT
environments where pods connect only to southbound operational systems and northbound cloud-data
systems, set ingress.status to Removed in the config.yaml file and restart the service.
Prerequisites
You installed MicroShift.
You created a MicroShift config.yaml file.
The OpenShift CLI (oc) is installed.
TIP
If you complete all the configurations that you need to make in the MicroShift config.yaml file at the
same time, you can minimize system restarts.
Procedure
1. Update the value of ingress.status field to Removed in the MicroShift config.yaml file as
shown in the following example:
Example config.yaml ingress stanza
# ...
ingress:
ports:
http: 80
https: 443
routeAdmissionPolicy:
namespaceOwnership: InterNamespaceAllowed
status: Removed
# ...
28

CHAPTER 3. UNDERSTANDING AND CONFIGURING THE ROUTER
where:
ingress.status
Specifies whether the ingress ports remain open. When the value is set to Removed, the
ports listed in ingress.ports are automatically closed. Any other settings in the ingress
stanza are ignored, for example, any values in the
routeAdmissionPolicy.namespaceOwnership field.
2. Restart the MicroShift service by running the following command:
$ sudo systemctl restart microshift
NOTE
The MicroShift service outputs current configurations during restarts.
Verification
After the system restarts, verify that the router has been removed and that ingress is stopped
by running the following command:
$ oc -n openshift-ingress get svc
Expected output
No resources found in openshift-ingress namespace.
3.3. CONFIGURE ROUTER INGRESS
Configure the listenAddress setting if your MicroShift applications need to listen only for data traffic.
You can also configure specific ports and IP addresses for network connections. Use the combination
required to customize the endpoint configuration for your use case.
3.3.1. Configure router ports
To bind the ingress router to specific HTTP and HTTPS port numbers in MicroShift, you can edit the
ingress.ports.http and ingress.ports.https settings in config.yaml file.
Prerequisites
You installed MicroShift.
You created a MicroShift config.yaml file.
The OpenShift CLI (oc) is installed.
TIP
If you complete all the configurations that you need to make in the MicroShift config.yaml file at the
same time, you can minimize system restarts.
29

Red Hat build of MicroShift 4.22 Networking
Procedure
1. Update the MicroShift config.yaml port values in the ingress.ports.http and
ingress.ports.https fields to the ports you want to use:
Example config.yaml router settings
# ...
ingress:
ports:
http: 80
https: 443
routeAdmissionPolicy:
namespaceOwnership: InterNamespaceAllowed
status: Managed
# ...
where:
ingress.ports
Specifies the HTTP and HTTPS port numbers to bind the ingress router to. This field is
customizable. Valid values for both port entries are a single, unique port in the 1-65535 range.
The values of the ports.http and ports.https fields cannot be the same.
status
Specifies the status of the ingress ports. The default value is Managed. Managed is required
for the ingress ports to remain open.
2. Restart the MicroShift service by running the following command:
$ sudo systemctl restart microshift
3.3.2. Configure router IP addresses
To limit ingress to selected host IP addresses or network interfaces in MicroShift, you can set the
ingress.listenAddress list in your config.yaml file.
You can restrict the network traffic to the router by configuring specific IP addresses. For example:
Use cases where the router is reachable only on internal networks, but not on northbound public
networks
Use cases where the router is reachable only by northbound public networks, but not on internal
networks
Use cases where the router is reachable by both internal networks and northbound public
networks, but on separate IP addresses
Prerequisites
You installed MicroShift.
You created a MicroShift config.yaml file.
30

CHAPTER 3. UNDERSTANDING AND CONFIGURING THE ROUTER
The OpenShift CLI (oc) is installed.
TIP
If you complete all the configurations that you need to make in the MicroShift config.yaml file at the
same time, you can minimize system restarts.
Procedure
1. Update the list in the ingress.listenAddress field in the MicroShift config.yaml according to
your requirements and as shown in the following examples:
Default router IP address list
# ...
ingress:
listenAddress:
- "<host_network>"
# ...
where:
ingress.listenAddress
Specifies the IP addresses or network interfaces to limit ingress to. The default value is the
entire network of the host. To continue to use the default list, remove the listen.Address
field from the MicroShift config.yaml file. To customize this parameter, use a list. The list
can contain either a single IP address or NIC name or multiple IP addresses and NIC names.
IMPORTANT
You must either remove the listenAddress parameter or add values to it in the
form of a list when using the config.yaml file. Do not leave the field empty or
MicroShift crashes on restart.
Example router setting with a single host IP address
# ...
ingress:
listenAddress:
- 10.2.1.100
# ...
Example router setting with a combination of IP addresses and NIC names
# ...
ingress:
listenAddress:
- 10.2.1.100
- 10.2.2.10
- ens3
# ...
31

Red Hat build of MicroShift 4.22 Networking
2. Restart the MicroShift service by running the following command:
$ sudo systemctl restart microshift
Verification
To verify that your settings are applied, make sure that the ingress.listenAddress IP addresses
are reachable, then you can curl the route with the destination to one of these load balancer IP
address.
3.4. ADDITIONAL RESOURCES
About the default MicroShift configuration file
About network policies
3.5. CONFIGURE THE ROUTE ADMISSION POLICY
By default, MicroShift allows routes in multiple namespaces to use the same hostname. To prevent
routes from claiming the same hostname in different namespaces, you can configure the route
admission policy.
Prerequisites
You installed MicroShift.
You created a MicroShift config.yaml file.
You installed the OpenShift CLI (oc).
TIP
If you complete all the configurations that you need to make in the MicroShift config.yaml file
at the same time, you can minimize system restarts.
Procedure
1. To prevent routes in different namespaces from claiming the same hostname, update the
namespaceOwnership field value to Strict in the MicroShift config.yaml file. See the following
example:
Example config.yaml route admission policy
# ...
ingress:
routeAdmissionPolicy:
namespaceOwnership: Strict
# ...
where:
ingress.routeAdmissionPolicy.namespaceOwnership
Specifies the route admission policy. Prevents routes in different namespaces from claiming
32

CHAPTER 3. UNDERSTANDING AND CONFIGURING THE ROUTER
Specifies the route admission policy. Prevents routes in different namespaces from claiming
the same host. Valid values are Strict and InterNamespaceAllowed. If you delete the value
in a customized config.yaml, the InterNamespaceAllowed value is set automatically.
2. To apply the configuration, restart the MicroShift service by running the following command:
$ sudo systemctl restart microshift
33

Red Hat build of MicroShift 4.22 Networking
CHAPTER 4. USING THE SR-IOV NETWORK OPERATOR
When you run network-intensive workloads on MicroShift, you need a simplified and declarative method
to configure and access high-performance networking interfaces. You can optionally install the SR-IOV
Network Operator so that you can expose SR-IOV devices as resources and use
NetworkAttachmentDefinitions to access Virtual Functions (VFs).
4.1. UNDERSTAND THE SR-IOV NETWORK OPERATOR
SR-IOV (Single Root I/O Virtualization) is a specification that allows a single physical Peripheral
Component Interconnect Express (PCIe) device that supports SR-IOV, for example, a Physical Function
(PF), to appear as multiple separate physical devices known as Virtual Functions (VFs).
You can directly assign VFs to pods, which bypasses the host operating system network stack, improves
throughput, and reduces latency for network intensive workloads.
The integration of the SR-IOV Network Operator and CNI provider into MicroShift enables declarative
access to VFs. As a result, you can expose supported SR-IOV devices as specialized resources within
your MicroShift pod for more predictable high-speed networking for demanding workloads. The
deployed SR-IOV resources operate in the sriov-network-operator namespace.
You do not need to manually configure SR-IOV through the operating system. You can also treat VFs as
resources that can be reliably mapped to your containerized applications. These resources reduce
manual error and ensure consistent, low-latency networking for critical applications.
Here are the components of SR-IOV functionality:
SR-IOV Network Operator: The SR-IOV Network Operator is a Kubernetes component that
detects and manages SR-IOV devices. This component exposes the SR-IOV devices as
schedulable resources within MicroShift.
SR-IOV CNI Provider: This Container Network Interface (CNI) provider works with Multus to
assign the exposed VFs to the application pods.
Virtual Functions (VFs): VFs are lightweight PCIe functions exposed by the PF that are assigned
to pods.
NetworkAttachment Definitions: NetworkAttachmentDefinitions are custom resources (CRs)
that are used to define the specific network configuration so that application developers can
specify the VFs they need access. NetworkAttachmentDefinitions provide the declarative
method for accessing VFs.
4.2. INSTALL THE SR-IOV NETWORK OPERATOR
Install the necessary SR-IOV components to enable MicroShift to discover SR-IOV devices and expose
them as resources for scheduling.
Prerequisites
You have the required RPM package containing the SR-IOV Network Operator.
Procedure
1. If provided as an optional RPM, install the required microshift-sriov RPM package.
2. Restart the MicroShift service to deploy the SR-IOV resources in the sriov-network-operator
34

CHAPTER 4. USING THE SR-IOV NETWORK OPERATOR
2. Restart the MicroShift service to deploy the SR-IOV resources in the sriov-network-operator
namespace.
3. To specify the required VF configuration based on the available hardware, create an
SriovNetworkNodePolicy custom resource (CR). For example, save the following YAML as the
file policyoneflag-sriov-node-network.yaml:
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
name: policyoneflag
namespace: sriov-network-operator
spec:
resourceName: policyoneflag
nodeSelector:
node.kubernetes.io/instance-type: rhde
priority: 10
numVfs: 5
nicSelector:
pfNames: ["ens5"]
deviceType: "netdevice"
isRdma: false
The metadata.name parameter specifies the name for the custom resource object.
The metadata.namespace parameter specifies the namespace where the SR-IOV Network
Operator is installed.
The spec.resourceName parameter specifies the resource name of the SR-IOV network
device plugin. You can create multiple SR-IOV network node policies for a resource name.
(Optional) The spec.priority parameter specifies a priority value. The priority is an integer
value between 0 and 99. A smaller value receives higher priority. For example, a priority of
10 is a higher priority than 99. The default value is 99.
The spec.numVfs parameter specifies the number of the virtual functions (VFs) to create
for the SR-IOV physical network device. For an Intel network interface controller (NIC), the
number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox
NIC, the number of VFs cannot be larger than 127.
The spec.nicSelector parameter identifies the device for the Operator to configure. You
do not have to specify values for all the parameters. It is recommended to identify the
network device with enough precision to avoid selecting a device unintentionally. If you
specify rootDevices, you must also specify a value for vendor, deviceID, or pfNames. If you
specify both pfNames and rootDevices at the same time, ensure that they refer to the
same device. If you specify a value for netFilter, then you do not need to specify any other
parameter because a network ID is unique.
(Optional) The spec.nicSelector.pfNames parameter specifies an array of one or more
physical function (PF) names for the device.
(Optional) The spec.deviceType parameter specifies the driver type for the virtual
functions. The only allowed value is netdevice.
(Optional) The spec.isRDMA parameter configures whether to enable remote direct
35

Red Hat build of MicroShift 4.22 Networking
memory access (RDMA) mode. The default value is false. If the spec.isRdma parameter is
set to true, you can continue to use the RDMA-enabled VF as a normal network device. A
device can be used in either mode. To configure a Mellanox NIC for use with DPDK
applications that require a fast data path, set spec.isRdma to true and additionally set the
needVhostNet parameter to true.
NOTE
The vfio-pci driver type is not supported.
4. Create the SriovNetworkNodePolicy object by entering the following command:
$ oc create -f policyoneflag-sriov-node-network.yaml
After applying the configuration update, the workload contains the required resources and
dependencies for VF access.
5. To verify that the SR-IOV network device is configured, enter the following command. Replace
<node_name> with the name of a node with the SR-IOV network device that you just
configured. Expected output shows Succeeded.
$ oc get sriovnetworknodestates -n sriov-network-operator <node_name> -o
jsonpath='{.status.syncStatus}'
6. Deploy an SriovNetwork custom resource (CR) which references the
SriovNetworkNodePolicy CR and insert the metaPlugins configuration, as in the following
example CR. The Operator generates a NetworkAttachmentDefinition CR and the VFs
become available to the pods. Save the YAML as the file sriov-network-interface-sysctl.yaml.
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
name: onevalidflag
namespace: sriov-network-operator
spec:
resourceName: policyoneflag
networkNamespace: sysctl-tuning-test
ipam: '{ "type": "static" }'
capabilities: '{ "mac": true, "ips": true }'
metaPlugins : |
{
"type": "tuning",
"capabilities":{
"mac":true
},
"sysctl":{
"net.ipv4.conf.IFNAME.accept_redirects": "1"
}
}
The metadata.name parameter specifies the name for the object. The SR-IOV Network
Operator creates a NetworkAttachmentDefinition object with the same name.
36

CHAPTER 4. USING THE SR-IOV NETWORK OPERATOR
The metadata.namespace parameter specifies the namespace where the SR-IOV Network
Operator is installed.
The spec.resourceName parameter displays the value from the SriovNetworkNodePolicy
object that defines the SR-IOV hardware for this additional network.
The spec.networkNamespace parameter specifies the target namespace for the
SriovNetwork object. Only pods in the target namespace can attach to the additional
network.
The spec.ipam parameter specifies a configuration object for the IPAM CNI plugin as a
YAML block scalar. The plugin manages IP address assignment for the attachment
definition.
(Optional) The spec.capabilities parameter sets capabilities for the additional network.
You can specify "{ "ips": true }" to enable IP address support or "{ "mac": true }" to
enable MAC address support.
(Optional) The spec.metaPlugins parameter is used to add additional capabilities to the
device. In this use case set the type field to tuning. Specify the interface-level network
sysctl you want to set in the sysctl field.
7. Create the SriovNetwork resource by entering the following command:
$ oc create -f sriov-network-interface-sysctl.yaml
Verification
1. Confirm that the SR-IOV Network Operator created the NetworkAttachmentDefinition CR by
running the following command:
$ oc get network-attachment-definitions -n <namespace>
Replace <namespace> with the value for networkNamespace parameter that you specified in
the SriovNetwork object, for example, sysctl-tuning-test. The expected output shows the
name of the NAD CRD and the creation age in minutes.
NOTE
There might be a delay before the SR-IOV Network Operator creates the CR.
2. Verify that the tuning CNI is correctly configured and the additional SR-IOV network is
attached:
a. Create a Pod CR. Save the following YAML as the file examplepod.yaml:
apiVersion: v1
kind: Pod
metadata:
name: tunepod
namespace: sysctl-tuning-test
annotations:
k8s.v1.cni.cncf.io/networks: |-
[
37

Red Hat build of MicroShift 4.22 Networking
{
"name": "onevalidflag",
"mac": "0a:56:0a:83:04:0c",
"ips": ["10.100.100.200/24"]
}
]
spec:
containers:
- name: podexample
image: centos
command: ["/bin/bash", "-c", "sleep INF"]
securityContext:
runAsUser: 2000
runAsGroup: 3000
allowPrivilegeEscalation: false
capabilities:
drop: ["ALL"]
securityContext:
runAsNonRoot: true
seccompProfile:
type: RuntimeDefault
The annotations.name parameter specifies the name of the SR-IOV network
attachment definition CR.
(Optional) The annotations.mac parameter specifies the MAC address for the SR-IOV
device that is allocated from the resource type defined in the SR-IOV network
attachment definition CR. To use this feature, you also must specify { "mac": true } in
the SriovNetwork object.
(Optional) The annotations.ips parameter specifies the IP addresses for the SR-IOV
device that are allocated from the resource type defined in the SR-IOV network
attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this
feature, you also must specify { "ips": true } in the SriovNetwork object.
b. Create the Pod CR by entering the following command:
$ oc apply -f examplepod.yaml
c. Verify that the pod is created by running the following command:
$ oc get pod -n sysctl-tuning-test
Example output:
NAME READY STATUS RESTARTS AGE
tunepod 1/1 Running 0 47s
d. Log in to the pod by running the following command:
$ oc rsh -n sysctl-tuning-test tunepod
e. Verify the values of the configured sysctl flag. Find the value
net.ipv4.conf.IFNAME.accept_redirects by running the following command:
38

CHAPTER 4. USING THE SR-IOV NETWORK OPERATOR
$ sysctl net.ipv4.conf.net1.accept_redirects
4.3. SR-IOV NETWORK OPERATOR SUPPORTED DEVICES
The config.yaml file lists the supported network devices for the SR-IOV Network Operator.
SR-IOV Network Operator configuration file
apiVersion: v1
kind: ConfigMap
metadata:
name: supported-nic-ids
data:
Intel_i40e_XXV710: "8086 158a 154c"
Intel_i40e_25G_SFP28: "8086 158b 154c"
Intel_i40e_10G_X710_SFP: "8086 1572 154c"
Intel_ixgbe_10G_X550: "8086 1563 1565"
Intel_ixgbe_82576: "8086 10c9 10ca"
Intel_i40e_X710_X557_AT_10G: "8086 1589 154c"
Intel_i40e_10G_X710_BACKPLANE: "8086 1581 154c"
Intel_i40e_10G_X710_BASE_T: "8086 15ff 154c"
Intel_i40e_XXV710_N3000: "8086 0d58 154c"
Intel_i40e_40G_XL710_QSFP: "8086 1583 154c"
Intel_ice_Columbiaville_E810-CQDA2_2CQDA2: "8086 1592 1889"
Intel_ice_Columbiaville_E810-XXVDA4: "8086 1593 1889"
Intel_ice_Columbiaville_E810-XXVDA2: "8086 159b 1889"
Intel_ice_Columbiaville_E810-XXV_BACKPLANE: "8086 1599 1889"
Intel_ice_Columbiaville_E810: "8086 1591 1889"
Intel_ice_Columbiapark_E823C: "8086 188a 1889"
Intel_ice_Columbiapark_E823L_SFP: "8086 124d 1889"
Intel_ice_Columbiapark_E823L_BACKPLANE: "8086 124c 1889"
Intel_ice_Columbiapark_E825C_BACKPLANE: "8086 579c 1889"
Intel_ice_Columbiapark_E825C_QSFP: "8086 579d 1889"
Intel_ice_Columbiapark_E825C_SFP: "8086 579e 1889"
Intel_ice_Connorsville_E830_QSFP: "8086 12d2 1889"
Intel_ice_Connorsville_E830_SFP: "8086 12d3 1889"
Intel_ice_Connorsville_E835CC_QSFP: "8086 1249 1889"
Intel_ice_Connorsville_E835CC_SFP: "8086 124a 1889"
Nvidia_mlx5_ConnectX-4: "15b3 1013 1014"
Nvidia_mlx5_ConnectX-4LX: "15b3 1015 1016"
Nvidia_mlx5_ConnectX-5: "15b3 1017 1018"
Nvidia_mlx5_ConnectX-5_Ex: "15b3 1019 101a"
Nvidia_mlx5_ConnectX-6: "15b3 101b 101c"
Nvidia_mlx5_ConnectX-6_Dx: "15b3 101d 101e"
Nvidia_mlx5_ConnectX-6_Lx: "15b3 101f 101e"
Nvidia_mlx5_ConnectX-7: "15b3 1021 101e"
Nvidia_mlx5_ConnectX-8: "15b3 1023 101e"
Nvidia_mlx5_MT42822_BlueField-2_integrated_ConnectX-6_Dx: "15b3 a2d6 101e"
Nvidia_mlx5_MT43244_BlueField-3_integrated_ConnectX-7_Dx: "15b3 a2dc 101e"
Broadcom_bnxt_BCM57414_2x25G: "14e4 16d7 16dc"
Broadcom_bnxt_BCM75508_2x100G: "14e4 1750 1806"
Qlogic_qede_QL45000_50G: "1077 1654 1664"
Red_Hat_Virtio_network_device: "1af4 1000 1000"
Red_Hat_Virtio_1_0_network_device: "1af4 1041 1041"
Marvell_OCTEON_TX2_CN96XX: "177d b200 b203"
39

Red Hat build of MicroShift 4.22 Networking
Marvell_OCTEON_TX2_CN98XX: "177d b100 b103"
Marvell_OCTEON_Fusion_CNF95XX: "177d b600 b603"
Marvell_OCTEON10_CN10XXX: "177d b900 b903"
Marvell_OCTEON_Fusion_CNF105XX: "177d ba00 ba03"
Amazon_Elastic_Network_Adapter: "1d0f ec20 ec20"
NOTE
For the most up-to-date list of supported cards and compatible Red Hat build of
MicroShift versions available, see Openshift Single Root I/O Virtualization (SR-IOV) and
PTP hardware networks Support Matrix.
4.4. ADDITIONAL RESOURCES
Understanding networking settings
About using multiple networks
About network policies
40

CHAPTER 5. NETWORK POLICIES
CHAPTER 5. NETWORK POLICIES
5.1. ABOUT NETWORK POLICIES
Learn how network policies work for MicroShift to restrict or allow network traffic to pods in your node.
5.1.1. How network policy works in MicroShift
In a node that is using the default OVN-Kubernetes Container Network Interface (CNI) plugin for
MicroShift, network isolation is controlled by both firewalld, which is configured on the host, and by
NetworkPolicy objects created within MicroShift.
Simultaneous use of firewalld and NetworkPolicy is supported.
Network policies work only within boundaries of OVN-Kubernetes-controlled traffic, so they can
apply to every situation except for hostPort/hostNetwork enabled pods.
Firewalld settings also do not apply to hostPort/hostNetwork enabled pods.
Firewalld rules run before any NetworkPolicy is enforced.

WARNING
Network policy does not apply to the host network namespace. Pods with host
networking enabled are unaffected by network policy rules. However, pods
connecting to the host-networked pods might be affected by the network policy
rules.
Network policies cannot block traffic from localhost.
By default, all pods in a MicroShift node are accessible from other pods and network endpoints. To
isolate one or more pods in a node, you can create NetworkPolicy objects to indicate allowed incoming
connections. You can create and delete NetworkPolicy objects.
If a pod is matched by selectors in one or more NetworkPolicy objects, then the pod accepts only
connections that are allowed by at least one of those NetworkPolicy objects. A pod that is not selected
by any NetworkPolicy objects is fully accessible.
A network policy applies to only the TCP, UDP, ICMP, and SCTP protocols. Other protocols are not
affected.
The following example NetworkPolicy objects demonstrate supporting different scenarios:
Deny all traffic:
To make a project deny by default, add a NetworkPolicy object that matches all pods but
accepts no traffic:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
41

Red Hat build of MicroShift 4.22 Networking
metadata:
name: deny-by-default
spec:
podSelector: {}
ingress: []
Allow connections from the default router, which is the ingress in MicroShift:
To allow connections from the MicroShift default router, add the following NetworkPolicy
object:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: allow-from-openshift-ingress
spec:
ingress:
- from:
- namespaceSelector:
matchLabels:
ingresscontroller.operator.openshift.io/deployment-ingresscontroller: default
podSelector: {}
policyTypes:
- Ingress
Only accept connections from pods within the same namespace:
To make pods accept connections from other pods in the same namespace, but reject all other
connections from pods in other namespaces, add the following NetworkPolicy object:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: allow-same-namespace
spec:
podSelector: {}
ingress:
- from:
- podSelector: {}
Only allow HTTP and HTTPS traffic based on pod labels:
To enable only HTTP and HTTPS access to the pods with a specific label (role=frontend in
following example), add a NetworkPolicy object similar to the following:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: allow-http-and-https
spec:
podSelector:
matchLabels:
role: frontend
ingress:
- ports:
- protocol: TCP
42

CHAPTER 5. NETWORK POLICIES
port: 80
- protocol: TCP
port: 443
Accept connections by using both namespace and pod selectors:
To match network traffic by combining namespace and pod selectors, you can use a
NetworkPolicy object similar to the following:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: allow-pod-and-namespace-both
spec:
podSelector:
matchLabels:
name: test-pods
ingress:
- from:
- namespaceSelector:
matchLabels:
project: project_name
podSelector:
matchLabels:
name: test-pods
NetworkPolicy objects are additive, which means you can combine multiple NetworkPolicy objects
together to satisfy complex network requirements.
For example, for the NetworkPolicy objects defined in previous examples, you can define both allow-
same-namespace and allow-http-and-https policies. That configuration allows the pods with the label
role=frontend to accept any connection allowed by each policy. That is, connections on any port from
pods in the same namespace, and connections on ports 80 and 443 from pods in any namespace.
5.1.2. Optimizations for network policy with OVN-Kubernetes network plugin
Learn how to optimize OVN-Kubernetes network policies to reduce flow count and ensure external IP
traffic is allowed when needed.
When designing your network policy, refer to the following guidelines:
For network policies with the same spec.podSelector spec, it is more efficient to use one
network policy with multiple ingress or egress rules, than multiple network policies with subsets
of ingress or egress rules.
Every ingress or egress rule based on the podSelector or namespaceSelector spec
generates the number of OVS flows proportional to number of pods selected by network
policy + number of pods selected by ingress or egress rule. Therefore, it is preferable to use
the podSelector or namespaceSelector spec that can select as many pods as you need in one
rule, instead of creating individual rules for every pod.
For example, the following policy contains two rules:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
43

Red Hat build of MicroShift 4.22 Networking
name: test-network-policy
spec:
podSelector: {}
ingress:
- from:
- podSelector:
matchLabels:
role: frontend
- from:
- podSelector:
matchLabels:
role: backend
The following policy expresses those same two rules as one:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: test-network-policy
spec:
podSelector: {}
ingress:
- from:
- podSelector:
matchExpressions:
- {key: role, operator: In, values: [frontend, backend]}
The same guideline applies to the spec.podSelector spec. If you have the same ingress or
egress rules for different network policies, it might be more efficient to create one network
policy with a common spec.podSelector spec. For example, the following two policies have
different rules:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: policy1
spec:
podSelector:
matchLabels:
role: db
ingress:
- from:
- podSelector:
matchLabels:
role: frontend
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: policy2
spec:
podSelector:
matchLabels:
role: client
ingress:
44

CHAPTER 5. NETWORK POLICIES
- from:
- podSelector:
matchLabels:
role: frontend
The following network policy expresses those same two rules as one:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: policy3
spec:
podSelector:
matchExpressions:
- {key: role, operator: In, values: [db, client]}
ingress:
- from:
- podSelector:
matchLabels:
role: frontend
You can apply this optimization when only multiple selectors are expressed as one. In cases
where selectors are based on different labels, it may not be possible to apply this optimization. In
those cases, consider applying some new labels for network policy optimization specifically.
5.1.2.1. NetworkPolicy CR and external IPs in OVN-Kubernetes
In OVN-Kubernetes, the NetworkPolicy custom resource (CR) enforces strict isolation rules. If a service
is exposed using an external IP, a network policy can block access from other namespaces unless
explicitly configured to allow traffic.
To allow access to external IPs across namespaces, create a NetworkPolicy CR that explicitly permits
ingress from the required namespaces and ensures traffic is allowed to the designated service ports.
Without allowing traffic to the required ports, access might still be restricted.
Example output
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
annotations:
name: <policy_name>
namespace: openshift-ingress
spec:
ingress:
- ports:
- port: 80
protocol: TCP
- ports:
- port: 443
protocol: TCP
- from:
- namespaceSelector:
matchLabels:
kubernetes.io/metadata.name: <my_namespace>
45

Red Hat build of MicroShift 4.22 Networking
podSelector: {}
policyTypes:
- Ingress
where:
<policy_name>
Specifies your name for the policy.
<my_namespace>
Specifies the name of the namespace where the policy is deployed.
For more details, see "About network policy".
5.2. CREATING NETWORK POLICIES
You can create a network policy for a namespace.
5.2.1. Example NetworkPolicy object
Reference the example NetworkPolicy object to understand how to configure this object.
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: allow-27107
spec:
podSelector:
matchLabels:
app: mongodb
ingress:
- from:
- podSelector:
matchLabels:
app: app
ports:
- protocol: TCP
port: 27017
where:
name
The name of the NetworkPolicy object.
spec.podSelector
A selector that describes the pods to which the policy applies.
ingress.from.podSelector
A selector that matches the pods from which the policy object allows ingress traffic. The selector
matches pods in the same namespace as the NetworkPolicy.
ingress.ports
A list of one or more destination ports on which to accept traffic.
46

CHAPTER 5. NETWORK POLICIES
5.2.2. Create a network policy using the CLI
To define granular rules describing ingress or egress network traffic allowed for namespaces in your
cluster, you can create a network policy.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace that the network policy applies to.
Procedure
1. Create a policy rule.
a. Create a <policy_name>.yaml file:
$ touch <policy_name>.yaml
where:
<policy_name>
Specifies the network policy file name.
b. Define a network policy in the created file. The following example denies ingress traffic from
all pods in all namespaces. This is a fundamental policy, blocking all cross-pod networking
other than cross-pod traffic allowed by the configuration of other Network Policies.
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
spec:
podSelector: {}
policyTypes:
- Ingress
ingress: []
The following example configuration allows ingress traffic from all pods in the same
namespace:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: allow-same-namespace
spec:
podSelector:
ingress:
- from:
- podSelector: {}
# ...
The following example allows ingress traffic to one pod from a particular namespace. This
policy allows traffic to pods that have the pod-a label from pods running in namespace-y.
kind: NetworkPolicy
47

Red Hat build of MicroShift 4.22 Networking
apiVersion: networking.k8s.io/v1
metadata:
name: allow-traffic-pod
spec:
podSelector:
matchLabels:
pod: pod-a
policyTypes:
- Ingress
ingress:
- from:
- namespaceSelector:
matchLabels:
kubernetes.io/metadata.name: namespace-y
# ...
The following example configuration restricts traffic to a service. This policy when applied
ensures every pod with both labels app=bookstore and role=api can only be accessed by
pods with label app=bookstore. In this example the application could be a REST API server,
marked with labels app=bookstore and role=api.
This example configuration addresses the following use cases:
Restricting the traffic to a service to only the other microservices that need to use it.
Restricting the connections to a database to only permit the application using it.
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: api-allow
spec:
podSelector:
matchLabels:
app: bookstore
role: api
ingress:
- from:
- podSelector:
matchLabels:
app: bookstore
# ...
2. To create the network policy object, enter the following command. Successful output lists the
name of the policy object and the created status.
$ oc apply -f <policy_name>.yaml -n <namespace>
where:
<policy_name>
Specifies the network policy file name.
<namespace>
Optional parameter. If you defined the object in a different namespace than the current
48

CHAPTER 5. NETWORK POLICIES
Optional parameter. If you defined the object in a different namespace than the current
namespace, the parameter specifices the namespace.
Successful output lists the name of the policy object and the created status.
5.2.3. Create a default deny all network policy
The default deny all network policy blocks all cross-pod networking other than network traffic allowed by
the configuration of other deployed network policies and traffic between host-networked pods.
The steps in the procedure enforces a strong deny policy by applying a deny-by-default policy in the
my-project namespace.

WARNING
Without configuring a NetworkPolicy custom resource (CR) that allows traffic
communication, the following policy might cause communication problems across
your cluster.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace that the network policy applies to.
Procedure
1. Create the following YAML that defines a deny-by-default policy to deny ingress from all pods
in all namespaces. Save the YAML in the deny-by-default.yaml file:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: deny-by-default
namespace: my-project
spec:
podSelector: {}
ingress: []
where:
namespace
Specifies the namespace in which to deploy the policy. For example, the my-project
namespace.
podSelector
If this field is empty, the configuration matches all the pods. Therefore, the policy applies to
all pods in the my-project namespace.
ingress
49

Red Hat build of MicroShift 4.22 Networking
Where [] indicates that no ingress rules are specified. This causes incoming traffic to be
dropped to all pods.
2. Apply the policy by entering the following command. Successful output lists the name of the
policy object and the created status.
$ oc apply -f deny-by-default.yaml
5.2.4. Create a network policy to allow traffic from external clients
With the deny-by-default policy in place you can proceed to configure a policy that allows traffic from
external clients to a pod with the label app=web.
NOTE
Firewalled rules run before any NetworkPolicy is enforced.
Follow this procedure to configure a policy that allows external service from the public Internet directly
or by using a Load Balancer to access the pod. Traffic is only allowed to a pod with the label app=web.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace that the network policy applies to.
Procedure
1. Create a policy that allows traffic from the public Internet directly or by using a load balancer to
access the pod. Save the YAML in the web-allow-external.yaml file:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
spec:
policyTypes:
- Ingress
podSelector:
matchLabels:
app: web
ingress:
- {}
2. Apply the policy by entering the following command. Successful output lists the name of the
policy object and the created status.
$ oc apply -f web-allow-external.yaml
5.2.5. Create a network policy allowing traffic to an application from all namespaces
You can configure a policy that allows traffic from all pods in all namespaces to a particular application.
Prerequisites
50

CHAPTER 5. NETWORK POLICIES
You installed the OpenShift CLI (oc).
You are working in the namespace that the network policy applies to.
Procedure
1. Create a policy that allows traffic from all pods in all namespaces to a particular application.
Save the YAML in the web-allow-all-namespaces.yaml file:
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: web-allow-all-namespaces
namespace: default
spec:
podSelector:
matchLabels:
app: web
policyTypes:
- Ingress
ingress:
- from:
- namespaceSelector: {}
where:
app
Applies the policy only to app:web pods in default namespace.
namespaceSelector
Selects all pods in all namespaces.
NOTE
By default, if you do not specify a namespaceSelector parameter in the
policy object, no namespaces get selected. This means the policy allows
traffic only from the namespace where the network policy deployes.
2. Apply the policy by entering the following command. Successful output lists the name of the
policy object and the created status.
$ oc apply -f web-allow-all-namespaces.yaml
Verification
1. Start a web service in the default namespace by entering the following command:
$ oc run web --namespace=default --image=nginx --labels="app=web" --expose --port=80
2. Run the following command to deploy an alpine image in the secondary namespace and to
start a shell:
51

Red Hat build of MicroShift 4.22 Networking
$ oc run test-$RANDOM --namespace=secondary --rm -i -t --image=alpine -- sh
3. Run the following command in the shell and observe that the service allows the request:
# wget -qO- --timeout=2 http://web.default
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>
<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>
<p><em>Thank you for using nginx.</em></p>
</body>
</html>
5.2.5.1. Create a network policy allowing traffic to an application from a namespace
You can configure a policy that allows traffic to a pod with the label app=web from a particular
namespace.
This configuration is useful in the following use cases:
Restrict traffic to a production database only to namespaces that have production workloads
deployed.
Enable monitoring tools deployed to a particular namespace to scrape metrics from the current
namespace.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace that the network policy applies to.
52

CHAPTER 5. NETWORK POLICIES

WARNING
Do not apply the network.openshift.io/policy-group: ingress label to custom
namespace or projects. This label is Operator-managed and reserved for Red Hat
build of MicroShift networking functions. It should not be altered on system-created
namespaces.
Using this label can result in intermittent network connectivity drops, unintended
application of system NetworkPolicies resource, or configuration drift as the
operator attempts to reconcile the state. For custom traffic grouping, always use
unique, user-defined labels as shown in the following procedure.
Procedure
1. Create a policy that allows traffic from all pods in a particular namespaces with a label
purpose=production. Save the YAML in the web-allow-prod.yaml file:
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: web-allow-prod
namespace: default
spec:
podSelector:
matchLabels:
app: web
policyTypes:
- Ingress
ingress:
- from:
- namespaceSelector:
matchLabels:
purpose: production
where:
app
Applies the policy only to app:web pods in the default namespace.
purpose
Restricts traffic to only pods in namespaces that have the label purpose=production.
2. Apply the policy by entering the following command. Successful output lists the name of the
policy object and the created status.
$ oc apply -f web-allow-prod.yaml
Verification
1. Start a web service in the default namespace by entering the following command:
53

Red Hat build of MicroShift 4.22 Networking
$ oc run web --namespace=default --image=nginx --labels="app=web" --expose --port=80
2. Run the following command to create the prod namespace:
$ oc create namespace prod
3. Run the following command to label the prod namespace:
$ oc label namespace/prod purpose=production
4. Run the following command to create the dev namespace:
$ oc create namespace dev
5. Run the following command to label the dev namespace:
$ oc label namespace/dev purpose=testing
6. Run the following command to deploy an alpine image in the dev namespace and to start a
shell:
$ oc run test-$RANDOM --namespace=dev --rm -i -t --image=alpine -- sh
7. Run the following command in the shell and observe the reason for the blocked request. For
example, expected output states wget: download timed out.
# wget -qO- --timeout=2 http://web.default
8. Run the following command to deploy an alpine image in the prod namespace and start a shell:
$ oc run test-$RANDOM --namespace=prod --rm -i -t --image=alpine -- sh
9. Run the following command in the shell and observe that the request is allowed:
# wget -qO- --timeout=2 http://web.default
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>
<p>For online documentation and support please refer to
54

CHAPTER 5. NETWORK POLICIES
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>
<p><em>Thank you for using nginx.</em></p>
</body>
</html>
5.3. EDITING A NETWORK POLICY
You can edit an existing network policy for a namespace.
Typical edits might include changes to the pods to which the policy applies, allowed ingress traffic, and
the destination ports on which to accept traffic. The apiVersion, kind, and name fields must not be
changed when editing NetworkPolicy objects, as these define the resource itself.
5.3.1. Edit a network policy
To modify existing policy configurations, you can edit a network policy in a namespace. Edit policies by
modifying the policy file and applying it with oc apply, or by using the oc edit command directly.
NOTE
If you log in with cluster-admin privileges, you can edit network policies in any
namespace in the cluster.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace where the network policy exists.
Procedure
1. Optional: To list the network policy objects in a namespace, enter the following command:
$ oc get network policy -n <namespace>
where:
<namespace>
Optional: Specifies the namespace if the object is defined in a different namespace than the
current namespace.
2. Edit the network policy object.
a. If you saved the network policy definition in a file, edit the file and make any necessary
changes, and then enter the following command.
$ oc apply -n <namespace> -f <policy_file>.yaml
where:
55

Red Hat build of MicroShift 4.22 Networking
<namespace>
Optional: Specifies the namespace if the object is defined in a different namespace than
the current namespace.
<policy_file>
Specifies the name of the file containing the network policy.
b. If you need to update the network policy object directly, enter the following command:
$ oc edit network policy <policy_name> -n <namespace>
where:
<policy_name>
Specifies the name of the network policy.
<namespace>
Optional: Specifies the namespace if the object is defined in a different namespace than
the current namespace.
3. Confirm that the network policy object is updated.
$ oc describe networkpolicy <policy_name> -n <namespace>
where:
<policy_name>
Specifies the name of the network policy.
<namespace>
Optional: Specifies the namespace if the object is defined in a different namespace than the
current namespace.
5.3.2. Example NetworkPolicy object
Reference the example NetworkPolicy object to understand how to configure this object.
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
name: allow-27107
spec:
podSelector:
matchLabels:
app: mongodb
ingress:
- from:
- podSelector:
matchLabels:
app: app
ports:
- protocol: TCP
port: 27017
56

CHAPTER 5. NETWORK POLICIES
where:
name
The name of the NetworkPolicy object.
spec.podSelector
A selector that describes the pods to which the policy applies.
ingress.from.podSelector
A selector that matches the pods from which the policy object allows ingress traffic. The selector
matches pods in the same namespace as the NetworkPolicy.
ingress.ports
A list of one or more destination ports on which to accept traffic.
5.4. DELETING A NETWORK POLICY
You can delete a network policy from a namespace.
5.4.1. Delete a network policy using the CLI
You can delete a network policy in a namespace by using the CLI.
NOTE
If you log in with cluster-admin privileges, you can delete network policies in any
namespace in the cluster.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace where the network policy exists.
Procedure
To delete a network policy object, enter the following command. Successful output lists the
name of the policy object and the deleted status.
$ oc delete networkpolicy <policy_name> -n <namespace>
where:
<policy_name>
Specifies the name of the network policy.
<namespace>
Optional parameter. If you defined the object in a different namespace than the current
namespace, the parameter specifices the namespace.
5.5. VIEWING A NETWORK POLICY
Use the following procedure to view a network policy for a namespace.
57

Red Hat build of MicroShift 4.22 Networking
5.5.1. View network policies using the CLI
You can examine the network policies in a namespace.
NOTE
If you log in with cluster-admin privileges, you can edit network policies in any
namespace in the cluster.
Prerequisites
You installed the OpenShift CLI (oc).
You are working in the namespace where the network policy exists.
Procedure
1. List network policies in a namespace.
a. To view network policy objects defined in a namespace enter the following command:
$ oc get networkpolicy
b. Optional: To examine a specific network policy enter the following command:
$ oc describe networkpolicy <policy_name> -n <namespace>
where:
<policy_name>
Specifies the name of the network policy to inspect.
<namespace>
Optional: Specifies the namespace if the object is defined in a different namespace than
the current namespace.
$ oc describe networkpolicy allow-same-namespace
Name: allow-same-namespace
Namespace: ns1
Created on: 2021-05-24 22:28:56 -0400 EDT
Labels: <none>
Annotations: <none>
Spec:
PodSelector: <none> (Allowing the specific traffic to all pods in this namespace)
Allowing ingress traffic:
To Port: <any> (traffic allowed to all ports)
From:
PodSelector: <none>
Not affecting egress traffic
Policy Types: Ingress
58

CHAPTER 6. MULTIPLE NETWORKS
CHAPTER 6. MULTIPLE NETWORKS
6.1. ABOUT USING MULTIPLE NETWORKS
In addition to the default OVN-Kubernetes Container Network Interface (CNI) plugin, the MicroShift
Multus CNI is available to chain other CNI plugins. Installing and using MicroShift Multus is optional.
6.1.1. Secondary networks in MicroShift
Using the MicroShift Multus CNI plugin, you can add additional interfaces to pods from other networks.
With this configuration, you have flexibility when you configure pods that deliver network functionality,
such as switching or routing.
During node installation, the default pod network is configured with default values unless you customize
the configuration. The default network handles all ordinary network traffic for the node.
6.1.1.1. Supported secondary networks for network isolation
The following secondary networks are supported in MicroShift 4.22:
Bridge: Allows pods on the same host to communicate with each other and the host.
IPVLAN: Allows pods on a host to communicate with other hosts.
This is similar to a MACVLAN-based secondary network.
Each pod shares the same MAC address as the parent physical network interface, unlike a
MACVLAN-based secondary network.
MACVLAN: Allows pods on a host to communicate with other hosts and the pods on those other
hosts by using a physical network interface. Each pod that is attached to a MACVLAN-based
secondary network is provided with a unique MAC address.
NOTE
Setting network policies for secondary networks is not supported.
6.1.1.2. Use case: Secondary networks for network isolation
You can use an secondary network in situations where network isolation is needed, including control
plane and data plane separation. For example, you can configure an secondary interface if you want
pods to access a network on the host and also communicate with devices deployed to the edge. These
edge devices might be on an isolated operator network or are periodically disconnected.
Isolating network traffic is useful for the following performance and security reasons:
Performance
You can send traffic on two different planes to manage the amount of traffic on each plane.
Security
You can send sensitive traffic onto a network plane that is managed specifically for security
considerations, and you can separate private data that must not be shared between tenants or
customers.
IMPORTANT
59

Red Hat build of MicroShift 4.22 Networking
IMPORTANT
The Multus CNI plugin is deployed when the MicroShift service starts up. Therefore, a host
restart is required if the microshift-multus RPM package is added after MicroShift has
started. Restarting ensures that all containers are re-created with Multus annotations.
6.1.1.3. How secondary networks are implemented
All of the pods in the node still use the node-wide default network to maintain connectivity across the
node. Every pod has an eth0 interface that is attached to the node-wide pod network.
You can view the interfaces for a pod by using the oc get pod <pod_name> -o=jsonpath='{
.metadata.annotations.k8s\.v1\.cni\.cncf\.io/network-status }' command.
If you add secondary network interfaces that use the MicroShift Multus CNI, they are named
net1, net2, …​, netN.
The CNI configuration is created when the MicroShift Multus DaemonSet starts. This
configuration is autogenerated and includes the primary CNI that is the default delegate. For
MicroShift, the default CNI is OVN-Kubernetes.
6.1.1.4. How to attach secondary networks to pods
To attach secondary network interfaces to a pod, you must create and apply configurations that define
how the interfaces are attached.
You must configure any secondary networks you want to use. Because of individual differences
in networks, no default configuration is provided.
You must apply YAML manifest to specify each interface by using a
NetworkAttachmentDefinition custom resource (CR). A configuration inside each of these CRs
defines how that interface is created.
CRI-O must be configured to use Multus. A default configuration is included in the microshift-
multus RPM.
If the Multus CNI is installed on an existing MicroShift instance, the host must be restarted.
If the Multus CNI is installed alongside MicroShift, you can add CRs and pods and then start
the MicroShift service. Restarting the host in this scenario is not needed.
6.1.1.5. Configurations for secondary network types
The specific configuration fields for secondary networks is described in the following sections.
6.1.2. Install the Multus CNI plugin on a running node
If you want to attach additional networks to a pod for high-performance network configurations, you can
install the MicroShift Multus RPM package. After installation, a host restart is required to re-create all
the pods with the Multus annotation.
IMPORTANT
Uninstalling the Multus CNI plugin is not supported.
60

CHAPTER 6. MULTIPLE NETWORKS
Prerequisites
You have root access to the host.
Procedure
1. Install the Multus RPM package by running the following command:
$ sudo dnf install microshift-multus
TIP
If you create your custom resources (CRs) for additional networks now, you can complete your
installation and apply configurations with one restart.
2. To apply the package manifest to an active node, restart the host by running the following
command:
$ sudo systemctl restart
Verification
After restarting, ensure that the Multus CNI plugin components are created by running the
following command:
$ oc get pod -A | grep multus
Example output
openshift-multus dhcp-daemon-ktzqf 1/1 Running 0 45h
openshift-multus multus-4frf4 1/1 Running 0 45h
Next steps
1. If you have not done so, configure and apply the additional networks you want to use.
2. Deploy your applications that use the created CRs.
6.1.3. Configuration for a bridge secondary network
The Bridge CNI plugin JSON configuration object describes the configuration parameters for the Bridge
CNI plugin.
The following table details the configuration parameters:
Field Type Description
cniVersion string The CNI specification version. The 0.4.0 value is required.
type string The name of the CNI plugin to configure: bridge.
61

Red Hat build of MicroShift 4.22 Networking
Field Type Description
ipam object The configuration object for the IPAM CNI plugin. The plugin
manages IP address assignment for the attachment definition.
bridge string Optional: Specify the name of the virtual bridge to use. If the
bridge interface does not exist on the host, the bridge interface
gets created. The default value is cni0.
ipMasq boolean Optional: Set to true to enable IP masquerading for traffic that
leaves the virtual network. The source IP address for all traffic is
rewritten to the bridge’s IP address. If the bridge does not have
an IP address, this setting has no effect. The default value is
false.
disableContaine boolean Optional: Controls the container interface (veth peer inside the
rInterface netns container). When set to true, the container interface link-
state is set to down, you cannot use the IPAM CNI plugin. The
default value is false.
isGateway boolean Optional: Set to true to assign an IP address to the bridge. The
default value is false.
isDefaultGatewa boolean Optional: Set to true to configure the bridge as the default
y gateway for the virtual network. The assigned IP address of the
bridge is used as the default route. If isDefaultGateway is set
to true, isGateway is also set to true automatically. The
default value is false.
forceAddress boolean Optional: Set to true to allow assignment of a previously
assigned IP address to the virtual bridge. When set to false, if an
IPv4 address or an IPv6 address from overlapping subsets is
assigned to the virtual bridge, an error occurs. The default value
is false.
hairpinMode boolean Optional: Set to true to allow the virtual bridge to send an
Ethernet frame back through the virtual port it was received on.
This mode is also known as reflective relay. The default value is
false.
promiscMode boolean Optional: Set to true to enable promiscuous mode on the
bridge. The default value is false.
mtu integer Optional: Set the maximum transmission unit (MTU) to the
specified value. The default value is automatically set by the
kernel.
enabledad boolean Optional: Enables duplicate address detection for the container
side veth. The default value is false.
62

CHAPTER 6. MULTIPLE NETWORKS
Field Type Description
macspoofchk boolean Optional: Enables mac spoof check, limiting the traffic
originating from the container to the mac address of the
interface. The default value is false.
6.1.3.1. Bridge CNI plugin configuration example
The following example configures a secondary network named bridge-conf for use with the MicroShift
Multus CNI:
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
name: bridge-conf
spec:
config: '{
"cniVersion": "0.4.0",
"type": "bridge",
"bridge": "test-bridge",
"mode": "bridge",
"ipam": {
"type": "host-local",
"ranges": [
[
{
"subnet": "10.10.0.0/16",
"rangeStart": "10.10.1.20",
"rangeEnd": "10.10.3.50",
"gateway": "10.10.0.254"
}
]
],
"dataDir": "/var/lib/cni/test-bridge"
}
}'
6.1.4. Configuration for an IPVLAN secondary network
The IPVLAN CNI plugin JSON configuration object describes the configuration parameters for the
IPVLAN, ipvlan, CNI plugin. The following table details these parameters:
Field Type Description
cniVersion string The CNI specification version. A minimum version of 0.3.1 is
required.
63

Red Hat build of MicroShift 4.22 Networking
Field Type Description
name string The mandatory, unique identifier assigned to this CNI network
attachment definition. It is used by the container runtime to
select the correct network configuration and serves as the key
for persistent resource state management, such as IP address
allocations.
type string The name of the CNI plugin to configure: ipvlan.
ipam object The configuration object for the IPAM CNI plugin. The plugin
manages IP address assignment for the attachment definition.
This is required unless the plugin is chained.
mode string Optional: The operating mode for the virtual network. The value
must be l2, l3, or l3s. The default value is l2.
master string Optional: The Ethernet interface to associate with the network
attachment. If a master is not specified, the interface for the
default network route is used.
mtu integer Optional: Set the maximum transmission unit (MTU) to the
specified value. The default value is automatically set by the
kernel.
linkInContainer boolean Optional: Specifies whether the master interface is in the
container network namespace or the main network namespace.
Set the value to true to request the use of a container
namespace master interface.
IMPORTANT
The ipvlan object does not allow virtual interfaces to communicate with the
master interface. Therefore the container is not able to reach the host by using
the ipvlan interface. Be sure that the container joins a network that provides
connectivity to the host, such as a network supporting the Precision Time
Protocol (PTP).
A single master interface cannot simultaneously be configured to use both
macvlan and ipvlan.
For IP allocation schemes that cannot be interface agnostic, the ipvlan plugin
can be chained with an earlier plugin that handles this logic. If the master is
omitted, then the previous result must contain a single interface name for the
ipvlan plugin to enslave. If ipam is omitted, then the previous result is used to
configure the ipvlan interface.
6.1.4.1. IPVLAN CNI plugin configuration example
The following example configures a secondary network named ipvlan-net:
64

CHAPTER 6. MULTIPLE NETWORKS
{
"cniVersion": "0.3.1",
"name": "ipvlan-net",
"type": "ipvlan",
"master": "eth1",
"linkInContainer": false,
"mode": "l3",
"ipam": {
"type": "static",
"addresses": [
{
"address": "192.168.10.10/24"
}
]
}
}
6.1.5. Configuration for a MACVLAN secondary network
The MACVLAN CNI plugin JSON configuration object describes the configuration parameters for the
MAC Virtual LAN (MACVLAN) Container Network Interface (CNI) plugin. The following table describes
these parameters:
Field Type Description
cniVersion string The CNI specification version. A minimum version of 0.3.1 is
required.
name string The mandatory, unique identifier assigned to this CNI network
attachment definition. It is used by the container runtime to
select the correct network configuration and serves as the key
for persistent resource state management, such as IP address
allocations.
type string The name of the CNI plugin to configure: macvlan.
ipam object The configuration object for the IPAM CNI plugin. The plugin
manages IP address assignment for the attachment definition.
mode string Optional: Configures traffic visibility on the virtual network.
Must be either bridge, passthru, private, or vepa. If a value is
not provided, the default value is bridge.
master string Optional: The host network interface to associate with the newly
created macvlan interface. If a value is not specified, then the
default route interface is used.
mtu integer Optional: The maximum transmission unit (MTU) to the specified
value. The default value is automatically set by the kernel.
65

Red Hat build of MicroShift 4.22 Networking
Field Type Description
linkInContainer boolean Optional: Specifies whether the master interface is in the
container network namespace or the main network namespace.
Set the value to true to request the use of a container
namespace master interface.
NOTE
If you specify the master key for the plugin configuration, use a different physical
network interface than the one that is associated with your primary network plugin to
avoid possible conflicts.
6.1.5.1. MACVLAN CNI plugin configuration example
The following example configures a secondary network named macvlan-net:
{
"cniVersion": "0.3.1",
"name": "macvlan-net",
"type": "macvlan",
"master": "eth1",
"linkInContainer": false,
"mode": "bridge",
"ipam": {
"type": "dhcp"
}
}
6.1.6. Additional resources
Configuring and using multiple networks
6.2. CONFIGURING AND USING MULTIPLE NETWORKS
After you have installed the MicroShift Multus Container Network Interface (CNI), you can use other
networking plugins by using configurations.
6.2.1. IP address management types and additional networks
IP addresses are provisioned for an additional network through an IP Address Management (IPAM) CNI
plugin that you configure. Supported IP address provisioning types in MicroShift are host-local, static,
and dhcp.
6.2.1.1. bridge interface specifics
When using the bridge type interface and the dhcp IPAM, a DHCP server listening on the bridged
66

CHAPTER 6. MULTIPLE NETWORKS
When using the bridge type interface and the dhcp IPAM, a DHCP server listening on the bridged
network is required. If you are using a firewall, configuring the firewalld service by running the firewall-
cmd --remove-service=dhcp command to allow DHCP traffic on the network zone is also required.
6.2.1.2. macvlan interface specifics
The macvlan type interface accesses the network that the host is connected to. This means that the
interface can receive an IP address from the DHCP server on the host network if the dhcp IPAM plugin
is used.
6.2.1.3. ipvlan interface specifics
The ipvlan interface also has direct access to the host network, but shares a MAC address with the host
interface. The ipvlan type interface cannot be used with the dhcp plugin because of the shared MAC
address. The IPAM plugin does not support the DHCP protocol with ClientID.
6.2.2. Create a NetworkAttachmentDefinition for an additional network
You can create a NetworkAttachmentDefinition configuration file for an additional network in order to
use other CNI plugins.
In this example, a bridge-type interface is used. You can also use the example workflow here that uses
host-local IP address management (IPAM) to configure other supported additional network types.
IMPORTANT
If you use bridge and the dhcp IPAM, a DHCP server listening on the bridged network is
required. If you are also using a firewall, configuring the firewalld service to allow DHCP
traffic on the network zone is also required. You can run the firewall-cmd --remove-
service=dhcp command in this case.
Prerequisites
The MicroShift Multus CNI is installed.
The OpenShift CLI (oc) is installed.
MicroShift is running.
Procedure
1. Optional: Verify that the MicroShift node is running with the Multus CNI by running the
following command:
$ oc get pods -n openshift-multus
Example output
NAME READY STATUS RESTARTS AGE
dhcp-daemon-dfbzw 1/1 Running 0 5h
multus-rz8xc 1/1 Running 0 5h
2. Create a NetworkAttachmentDefinition configuration file by running the following command
67

Red Hat build of MicroShift 4.22 Networking
2. Create a NetworkAttachmentDefinition configuration file by running the following command
and using the following example file for reference:
$ oc apply -f network-attachment-definition.yaml
Example NetworkAttachmentDefinition file
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
name: bridge-conf
spec:
config: '{
"cniVersion": "0.4.0",
"type": "bridge",
"bridge": "br-test",
"mode": "bridge",
"ipam": {
"type": "host-local",
"ranges": [
[
{
"subnet": "10.10.0.0/24",
"rangeStart": "10.10.0.20",
"rangeEnd": "10.10.0.50",
"gateway": "10.10.0.254"
}
],
[
{
"subnet": "fd00:IJKL:MNOP:10::0/64",
"rangeStart": "fd00:IJKL:MNOP:10::1",
"rangeEnd": "fd00:IJKL:MNOP:10::9"
"dataDir": "/var/lib/cni/br-test"
}
}'
where:
type
Specifies a name of the CNI plugin. This example uses the bridge type.
bridge
Specifies the name of the bridge on the MicroShift host that is used. The additional
interface of the pod is connected to that bridge. If the interface does not exist on the host,
the Bridge CNI creates it. If the interface already exists, it is reused. In this example, the name
of the interface is br-test.
ipam
Specifies the IPAM type.
ipam.ranges.
Specifies the IP address range for the additional network. IPv6 addresses can be added to
the secondary interface.
NOTE
68

CHAPTER 6. MULTIPLE NETWORKS
NOTE
Using the name of the bridge is specific to the bridge type of plugin. Other
plugins use different fields in their NetworkAttachmentDefinitions. For
example, the macvlan and ipvlan configurations use master to specify the
host interface to attach.
6.2.3. Add a pod to an additional network
You can add a pod to an additional network. At the time a pod is created, additional networks are
attached to it. The pod continues to send normal node-related network traffic over the default network.
If you want to attach additional networks to a pod that is already running, you must restart the pod.
Prerequisites
The OpenShift CLI (oc) is installed.
The node is running.
A network defined by a NetworkAttachmentDefinition object that you want to attach the pod
to exists.
Procedure
1. Add an annotation to a Pod YAML file. Only one of the following annotation formats can be
used:
a. To attach an additional network without any customization, add an annotation with the
following format. Replace <network> with the name of the additional network to associate
with the pod:
apiVersion: v1
kind: Pod
metadata:
annotations:
k8s.v1.cni.cncf.io/networks: <network>[,<network>,...]
# ...
Replace <network> with the name of each additional network to associate with the pod. To
specify more than one additional network, separate each network with a comma. Do not
include whitespaces between the commas. If you specify the same additional network
multiple times, that pod has multiple network interfaces attached to that network.
The following example annotation specifies a bridge-type additional network:
apiVersion: v1
kind: Pod
metadata:
annotations:
k8s.v1.cni.cncf.io/networks: bridge-conf
# ...
b. To attach an additional network with customizations, add an annotation with the following
69

Red Hat build of MicroShift 4.22 Networking
b. To attach an additional network with customizations, add an annotation with the following
format:
apiVersion: v1
kind: Pod
metadata:
annotations:
k8s.v1.cni.cncf.io/networks: |-
[
{
"name": "<network>",
"namespace": "<namespace>",
"default-route": ["<default-route>"]
}
]
# ...
where:
name
Specifies the name of the additional network defined by a
NetworkAttachmentDefinition object.
namespace
Specifies the namespace where the NetworkAttachmentDefinition object is defined.
default-route
Specifies an optional field to provide an override for the default route, such as
192.168.17.1.
2. To create a Pod YAML file and add the NetworkAttachmentDefinition annotation for an
additional network, run the following command and use the example YAML:
$ oc apply -f ./<test_bridge>.yaml
Replace <test_bridge> with the pod name that you want to use.
The following example output shows that the test_bridge pod has been created:
pod/test_bridge created
Example test_bridge pod YAML
apiVersion: v1
kind: Pod
metadata:
name: test_bridge
annotations:
k8s.v1.cni.cncf.io/networks: bridge-conf
labels:
app: test_bridge
spec:
terminationGracePeriodSeconds: 0
containers:
- name: hello-microshift
70

CHAPTER 6. MULTIPLE NETWORKS
image: quay.io/microshift/busybox:1.36
command: ["/bin/sh"]
args: ["-c", "while true; do echo -ne \"HTTP/1.0 200 OK\r\nContent-Length: 16\r\n\r\nHello
MicroShift\" | nc -l -p 8080 ; done"]
ports:
- containerPort: 8080
protocol: TCP
securityContext:
allowPrivilegeEscalation: false
capabilities:
drop:
- ALL
runAsNonRoot: true
runAsUser: 1001
runAsGroup: 1001
seccompProfile:
type: RuntimeDefault
3. Make sure that the NetworkAttachmentDefinition annotation is correct:
The following example NetworkAttachmentDefinition annotation specifies a bridge-type
additional network:
apiVersion: v1
kind: Pod
metadata:
annotations:
k8s.v1.cni.cncf.io/networks: bridge-conf
# ...
4. Optional: To confirm that the NetworkAttachmentDefinition annotation exists in a Pod YAML,
run the following command, replacing <name> with the name of the pod.
$ oc get pod <name> -o yaml
Replace <name> with the pod name you want to use. In the following example, <test_bridge> is
used.
In the following example, the test_bridge is attached to the net1 additional network:
$ oc get pod <test_bridge> -o yaml
Replace <test_bridge> with the name of the bridge you want to use.
The following example output shows that the test_bridge pod is attached to the net1
additional network:
apiVersion: v1
kind: Pod
metadata:
annotations:
k8s.v1.cni.cncf.io/networks: bridge-conf
k8s.v1.cni.cncf.io/network-status: |-
[{
"name": "ovn-kubernetes",
71

Red Hat build of MicroShift 4.22 Networking
"interface": "eth0",
"ips": [
"10.42.0.18"
],
"default": true,
"dns": {}
},{
"name": "bridge-conf",
"interface": "net1",
"ips": [
"20.2.2.100"
],
"mac": "22:2f:60:a5:f8:00",
"dns": {}
}]
name: pod
namespace: default
spec:
# ...
status:
# ...
The k8s.v1.cni.cncf.io/network-status parameter is a JSON array of objects. Each object
describes the status of an additional network attached to the pod. The annotation value is
stored as a plain text value.
5. Verify that the pod is running by running the following command:
$ oc get pod
Example output
NAME READY STATUS RESTARTS AGE
test_bridge 1/1 Running 0 81s
6.2.4. Configure an additional network
After you have created the NetworkAttachmentDefinition object and applied it, you can configure an
additional network.
In this example, the bridge type additional network is used. You can also use this workflow for other
network types.
Prerequisites
You created and applied the NetworkAttachmentDefinition object configuration.
Procedure
1. Verify that the bridge was created on the host by running the following command:
$ ip a show br-test
Example output
72

CHAPTER 6. MULTIPLE NETWORKS
22: br-test: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
group default qlen 1000
link/ether 96:bf:ca:be:1d:15 brd ff:ff:ff:ff:ff:ff
inet6 fe80::34e2:bbff:fed2:31f2/64 scope link
valid_lft forever preferred_lft forever
2. Configure an IP address for the bridge by running the following command:
$ sudo ip addr add 10.10.0.10/24 dev br-test
3. Verify that the IP address configuration is added to the bridge by running the following
command:
$ ip a show br-test
Example output
22: br-test: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
group default qlen 1000
link/ether 96:bf:ca:be:1d:15 brd ff:ff:ff:ff:ff:ff
inet 10.10.0.10/24 scope global br-test
valid_lft forever preferred_lft forever
inet6 fe80::34e2:bbff:fed2:31f2/64 scope link
valid_lft forever preferred_lft forever
Confirm that the IP address is configured as expected.
4. Verify the IP address of the pod by running the following command:
$ oc get pod test-bridge --
output=jsonpath='{.metadata.annotations.k8s\.v1\.cni\.cncf\.io/network-status}'
Example output
[{
"name": "ovn-kubernetes",
"interface": "eth0",
"ips": [
"10.42.0.17"
],
"mac": "0a:58:0a:2a:00:11",
"default": true,
"dns": {}
},{
"name": "default/bridge-conf",
"interface": "net1",
"ips": [
"10.10.0.20"
],
"mac": "82:01:98:e5:0c:b7",
"dns": {}
Confirm that the bridge additional network is attached as expected-"default/bridge-conf".
73

Red Hat build of MicroShift 4.22 Networking
5. Optional: You can use oc exec to access the pod and confirm its interfaces by using the ip
command:
$ oc exec -ti test-bridge -- ip a
Example output
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue qlen 1000
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo
valid_lft forever preferred_lft forever
inet6 ::1/128 scope host
valid_lft forever preferred_lft forever
2: eth0@if21: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc
noqueue
link/ether 0a:58:0a:2a:00:11 brd ff:ff:ff:ff:ff:ff
inet 10.42.0.17/24 brd 10.42.0.255 scope global eth0
valid_lft forever preferred_lft forever
inet6 fe80::858:aff:fe2a:11/64 scope link
valid_lft forever preferred_lft forever
3: net1@if23: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc
noqueue
link/ether 82:01:98:e5:0c:b7 brd ff:ff:ff:ff:ff:ff
inet 10.10.0.20/24 brd 10.10.0.255 scope global net1
valid_lft forever preferred_lft forever
inet6 fe80::8001:98ff:fee5:cb7/64 scope link
valid_lft forever preferred_lft forever
In the example the pod is attached to the 10.10.0.20 IP address on the net1 interface as
expected.
6. Confirm that the connection is working as expected by accessing the HTTP server in the pod
from the MicroShift host. Use the following command:
$ curl 10.10.0.20:8080
Example output
Hello MicroShift
6.2.5. Remove a pod from a secondary network
To disconnect a pod from specific network configurations in Red Hat build of MicroShift, you can remove
the pod from a secondary network. Delete the pod using the oc delete pod command to remove its
connection to the secondary network.
Prerequisites
A secondary network is attached to the pod.
Install the OpenShift CLI (oc).
Log in to the cluster.
74

CHAPTER 6. MULTIPLE NETWORKS
Procedure
Delete the pod by entering the following command:
$ oc delete pod <name> -n <namespace>
where:
<name>
Specifies the name of the pod.
<namespace>
Specifies the namespace that contains the pod.
6.2.6. Troubleshoot Multus networking
If the settings for multiple networks are not configured properly, pods can fail to start. You can check
pod network status and the configuration to help you solve a couple common scenarios.
6.2.6.1. Pod networking cannot be configured
If the Multus CNI plugin cannot apply networking annotations to a pod, the pod does not start. Pods can
also fail to start if any of the additional network CNIs fail.
Example error
Warning NoNetworkFound 0s multus cannot find a network-attachment-definitio (asdasd) in
namespace (default): network-attachment-definitions.k8s.cni.cncf.io "bad-ref-doesnt-exist" not found
In this case, you can take the following steps to trouble CNI failures:
Verify the values in both the NetworkAttachmentDefinitions and the annotations.
Remove the annotation to verify whether the pod is created successfully with just the default
network. If not, this might indicate a networking problem other than the Multus configuration.
If you are a device administrator, you can inspect the crio.service or microshift.service logs,
paying special attention to those that are generated by the kubelet.
For example, the following error from the kubelet shows that the primary CNI is not running.
This situation can be caused by pods not starting or because of a CRI-O misconfiguration such
as an incorrect cni_default_network setting.
Example kubelet-generated error
Feb 06 13:47:31 dev microshift[1494]: kubelet E0206 13:47:31.163290 1494
pod_workers.go:1298] "Error syncing pod, skipping" err="network is not ready: container
runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady
message:Network plugin returns error: No CNI configuration file in /etc/cni/net.d/. Has your
network provider started?" pod="default/samplepod" podUID="fe0f7f7a-8c47-4488-952b-
8abc0d8e2602"
6.2.6.2. Missing configuration file
Sometimes a pod cannot be created because the annotations reference a
75

Red Hat build of MicroShift 4.22 Networking
Sometimes a pod cannot be created because the annotations reference a
NetworkAttachmentDefinition configuration YAML that does not exist. In this case an error such as the
following is usually produced:
Example log
cannot find a network-attachment-definition (bad-conf) in namespace (default): network-attachment-
definitions.k8s.cni.cncf.io "bad-conf" not found" pod="default/samplepod"`
Example error output
"CreatePodSandbox for pod failed" err="rpc error: code = Unknown desc = failed to create pod
network sandbox k8s_samplepod_default_5fa13105-1bfb-4c6b-aee7-
3437cfb50e25_0(7517818bd8e85f07b551f749c7529be88b4e7daef0dd572d049aa636950c76c6):
error adding pod default_samplepod to CNI network \"multus-cni-network\": plugin type=\"multus\"
name=\"multus-cni-network\" failed (add): Multus: [default/samplepod/5fa13105-1bfb-4c6b-aee7-
3437cfb50e25]: error loading k8s delegates k8s args: TryLoadPodDelegates: error in getting k8s
network for pod: GetNetworkDelegates: failed getting the delegate: getKubernetesDelegate: cannot
find a network-attachment-definition (bad-conf) in namespace (default): network-attachment-
definitions.k8s.cni.cncf.io \"bad-conf\" not found" pod="default/samplepod"
To fix this error, create and apply the NetworkAttachmentDefinitions YAML.
6.2.7. Additional resources
About using multiple networks
Configuration of IP address assignment for a network attachment
76

CHAPTER 7. CONFIGURING ROUTES
CHAPTER 7. CONFIGURING ROUTES
To enable MicroShift node access for services, configure the cluster routes. By using this configuration,
you can expose specific applications directly through the network interface of the node.
Secure routes provide the ability to use several types of TLS termination to serve certificates to the
client. See the Additional resources section for links to the OpenShift Container Platform
documentation that describe how to create re-encrypt, edge, and passthrough routes with custom
certificates.
7.1. CREATE AN HTTP-BASED ROUTE
To host your application at a public URL by using the basic HTTP routing protocol, create an HTTP-
based route. This configuration exposes a service on an unsecured application port, allowing external
access without TLS encryption.
A route can either be secure or unsecured, depending on the network security configuration of your
application.
The following procedure describes how to create a simple HTTP-based route to a web application, using
the hello-microshift application as an example.
Prerequisites
You installed the OpenShift CLI (oc).
You have access to your MicroShift node.
You have a web application that exposes a port and a TCP endpoint listening for traffic on the
port.
Procedure
1. Create a service called hello-microshift by running the following command:
$ oc expose pod hello-microshift -n $namespace
2. Create an unsecured route to the hello-microshift application by running the following
command:
$ oc expose svc/hello-microshift --hostname=microshift.com $namespace
Verification
Verify that the route resource was created by running the following command:
$ oc get routes -o yaml <name of resource> -n $namespace
namespace: Specifies the route that is named hello-microshift and the namespace is named
hello-microshift.
Sample YAML definition for the created unsecured route
77

Red Hat build of MicroShift 4.22 Networking
apiVersion: route.openshift.io/v1
kind: Route
metadata:
name: hello-microshift
namespace: hello-microshift
spec:
host: microshift.com
port:
targetPort: 8080
to:
kind: Service
name: hello-microshift
where:
spec.host
Specifies the hostname.
port.targetPort
Specifies the target port for the router to map the endpoint port in the service.
NOTE
MicroShift does not use an API that creates a default ingress domain, but
instead provides a wildcard for automatically generated domains. Each route
can also define a separate hostname.
7.2. HTTP STRICT TRANSPORT SECURITY
To enhance security and optimize website performance, use the HTTP Strict Transport Security (HSTS)
policy. This mechanism signals browsers to use only HTTPS traffic on the route host, eliminating the
need for HTTP redirects and speeding up user interactions.
When HSTS policy is enforced, HSTS adds a Strict Transport Security header to HTTP and HTTPS
responses from the site. You can use the insecureEdgeTerminationPolicy value in a route to redirect
HTTP to HTTPS. When HSTS is enforced, the client changes all requests from the HTTP URL to HTTPS
before the request is sent, eliminating the need for a redirect.
Cluster administrators can configure HSTS to do the following:
Enable HSTS per-route
Disable HSTS per-route
Enforce HSTS per-domain, for a set of domains, or use namespace labels in combination with
domains
IMPORTANT
HSTS works only with secure routes, either edge-terminated or re-encrypt. The
configuration is ineffective on HTTP or passthrough routes.
78

CHAPTER 7. CONFIGURING ROUTES
7.3. ENABLE HTTP STRICT TRANSPORT SECURITY PER-ROUTE
To enforce secure HTTPS connections for specific applications, enable HTTP Strict Transport Security
(HSTS) on a per-route basis. Applying the haproxy.router.openshift.io/hsts_header annotation to
edge and re-encrypt routes ensures that browsers reject unencrypted traffic.
Prerequisites
You have root access to the cluster.
You installed the OpenShift CLI (oc).
Procedure
To enable HSTS on a route, add the haproxy.router.openshift.io/hsts_header value to the
edge-terminated or re-encrypt route. You can use the oc annotate tool to do this by running
the following command. To properly run the command, ensure that the semicolon (;) in the
haproxy.router.openshift.io/hsts_header route annotation is also surrounded by double
quotation marks ("").
Example annotate command that sets the maximum age to 31536000 ms
(approximately 8.5 hours)
$ oc annotate route <route_name> -n <namespace> --overwrite=true
"haproxy.router.openshift.io/hsts_header=max-age=31536000;\
includeSubDomains;preload"
Example route configured with an annotation
apiVersion: route.openshift.io/v1
kind: Route
metadata:
annotations:
haproxy.router.openshift.io/hsts_header: max-age=31536000;includeSubDomains;preload
# ...
spec:
host: def.abc.com
tls:
termination: "reencrypt"
...
wildcardPolicy: "Subdomain"
# ...
where:
max-age
Specifies the measurement of the length of time, in seconds, for the HSTS policy. If set to 0,
it negates the policy.
includeSubDomains
Specifies that all subdomains of the host must have the same HSTS policy as the host.
Optional parameter.
preload
79

Red Hat build of MicroShift 4.22 Networking
Specifies that the site is included in the HSTS preload list when max-age is greater than 0.
For example, sites such as Google can construct a list of sites that have preload set.
Browsers can then use these lists to determine which sites they can communicate with over
HTTPS, even before they have interacted with the site. Without preload set, browsers must
have interacted with the site over HTTPS, at least once, to get the header. Optional
parameter.
7.3.1. Disable HTTP Strict Transport Security per-route
To allow unencrypted connections or troubleshoot access issues, disable HTTP Strict Transport Security
(HSTS) for a specific route. Setting the max-age route annotation to 0 instructs browsers to stop
enforcing HTTPS requirements on the route host.
Prerequisites
You have root access to the cluster.
You installed the OpenShift CLI (oc).
Procedure
To disable HSTS, enter the following to set the max-age value in the route annotation to 0:
$ oc annotate route <route_name> -n <namespace> --overwrite=true
"haproxy.router.openshift.io/hsts_header"="max-age=0"
TIP
You can alternatively apply the following YAML to create the config map for disabling HSTS
per-route:
kind: Route
apiVersion: route.openshift.io/v1
metadata:
annotations:
haproxy.router.openshift.io/hsts_header: max-age=0
To disable HSTS for every route in a namespace, enter the following command:
$ oc annotate route --all -n <namespace> --overwrite=true
"haproxy.router.openshift.io/hsts_header"="max-age=0"
Verification
To query the annotation for all routes, enter the following command:
$ oc get route --all-namespaces -o go-template='{{range .items}}{{if .metadata.annotations}}
{{$a := index .metadata.annotations "haproxy.router.openshift.io/hsts_header"}}{{$n :=
.metadata.name}}{{with $a}}Name: {{$n}} HSTS: {{$a}}{{"\n"}}{{else}}{{""}}{{end}}{{end}}
{{end}}'
Example output
80

CHAPTER 7. CONFIGURING ROUTES
Name: routename HSTS: max-age=0
7.3.2. Enforce HTTP Strict Transport Security per-domain
To enforce secure communication per-domain, configure routes with a compliant HSTS policy
annotation. For upgraded nodes with non-compliant routes, ensure consistent enforcement by updating
the source manifests to apply the new security policies.
You cannot use oc expose route or oc create route commands to add a route in a domain that
enforces HSTS because the API for these commands does not accept annotations.
IMPORTANT
HSTS cannot be applied to insecure, or non-TLS, routes.
Prerequisites
You have root access to the node.
You installed the OpenShift CLI (oc).
Procedure
Apply HSTS to all routes in the node by running the following command:
$ oc annotate route --all --all-namespaces --overwrite=true
"haproxy.router.openshift.io/hsts_header"="max-
age=31536000;preload;includeSubDomains"
Apply HSTS to all routes in a particular namespace by running the following command:
$ oc annotate route --all -n <my_namespace> --overwrite=true
"haproxy.router.openshift.io/hsts_header"="max-
age=31536000;preload;includeSubDomains"
<my_namespace>: Specify the namespace that you want to use.
Verification
Review the HSTS annotations on all routes by running the following command:
$ oc get route --all-namespaces -o go-template='{{range .items}}{{if .metadata.annotations}}
{{$a := index .metadata.annotations "haproxy.router.openshift.io/hsts_header"}}{{$n :=
.metadata.name}}{{with $a}}Name: {{$n}} HSTS: {{$a}}{{"\n"}}{{else}}{{""}}{{end}}{{end}}
{{end}}'
Example output
Name: <_routename_> HSTS: max-age=31536000;preload;includeSubDomains
7.4. THROUGHPUT ISSUE TROUBLESHOOTING METHODS
81

Red Hat build of MicroShift 4.22 Networking
To diagnose and resolve network throughput issues, such as unusually high latency between specific
services, apply troubleshooting methods. Identifying connectivity bottlenecks helps ensure stable
application performance within Red Hat build of MicroShift.
If pod logs do not reveal any cause of the problem, use the following methods to analyze performance
issues:
Use a packet analyzer, such as ping or tcpdump to analyze traffic between a pod and its node.
For example, run the tcpdump tool on each pod while reproducing the behavior that led to the
issue. Review the captures on both sides to compare send and receive timestamps to analyze
the latency of traffic to and from a pod. Latency can occur in Red Hat build of MicroShift if a
node interface is overloaded with traffic from other pods, storage devices, or the data plane.
$ tcpdump -s 0 -i any -w /tmp/dump.pcap host <podip 1> && host <podip 2> 1
where:
podip
Specifies the IP address for the pod. Run the oc get pod <pod_name> -o wide command
to get the IP address of a pod.
The tcpdump command generates a file at /tmp/dump.pcap containing all traffic between
these two pods. You can run the analyzer shortly before the issue is reproduced and stop the
analyzer shortly after the issue is finished reproducing to minimize the size of the file. You
can also run a packet analyzer between the nodes with:
$ tcpdump -s 0 -i any -w /tmp/dump.pcap port 4789
Use a bandwidth measuring tool, such as iperf, to measure streaming throughput and UDP
throughput. Locate any bottlenecks by running the tool from the pods first, and then running it
from the nodes.
Additional resources
Running tcpdump inside an OpenShift pod to capture network traffic (Red Hat
Knowledgebase)
Running tcpdump from a RHEL CoreOS OpenShift node (Red Hat Knowledgebase)
How to run iPerf network performance tests in OpenShift Container Platform 4 (Red Hat
Knowledgebase)
How to test network bandwidth? (Red Hat Knowledgebase)
7.5. USE COOKIES TO KEEP ROUTE STATEFULNESS
To maintain stateful application traffic during pod restarts or scaling events, configure sticky sessions by
using cookies. By using this method, you ensure that all incoming traffic reaches the same endpoint,
preventing state loss even if the specific endpoint pod changes.
Red Hat build of MicroShift can use cookies to configure session persistence. The Ingress Controller
selects an endpoint to handle any user requests, and creates a cookie for the session. The cookie is
passed back in the response to the request and the user sends the cookie back with the next request in
82

CHAPTER 7. CONFIGURING ROUTES
the session. The cookie tells the Ingress Controller which endpoint is handling the session, ensuring that
client requests use the cookie so that they are routed to the same pod.
NOTE
Cookies cannot be set on passthrough routes, because the HTTP traffic cannot be seen.
Instead, a number is calculated based on the source IP address, which determines the
backend.
If backends change, the traffic can be directed to the wrong server, making it less sticky.
If you are using a load balancer, which hides source IP, the same number is set for all
connections and traffic is sent to the same pod.
7.5.1. Annotate a route with a cookie
To enable applications to manage session persistence and load distribution, annotate the route with a
custom cookie name. Overwriting the default cookie allows the backend application to identify and
delete the specific cookie, forcing endpoint re-selection when necessary.
When a server is overloaded, the server tries to remove the requests from the client and redistribute the
requests to other endpoints.
Procedure
1. Annotate the route with the specified cookie name:
$ oc annotate route <route_name> router.openshift.io/cookie_name="<cookie_name>"
where:
<route_name>
Specifies the name of the route.
<cookie_name>
Specifies the name for the cookie.
For example, to annotate the route my_route with the cookie name my_cookie:
$ oc annotate route my_route router.openshift.io/cookie_name="my_cookie"
2. Capture the route hostname in a variable:
$ ROUTE_NAME=$(oc get route <route_name> -o jsonpath='{.spec.host}')
where:
<route_name>
Specifies the name of the route.
3. Save the cookie, and then access the route:
$ curl $ROUTE_NAME -k -c /tmp/cookie_jar
Use the cookie saved by the previous command when connecting to the route:
83

Red Hat build of MicroShift 4.22 Networking
$ curl $ROUTE_NAME -k -b /tmp/cookie_jar
7.6. PATH-BASED ROUTES
To serve multiple applications by using a single hostname, configure path-based routes. This HTTP-
based configuration directs traffic to specific services by comparing the URL path component, ensuring
requests match the most specific route defined.
The following table shows example routes and their accessibility:
Table 7.1. Route availability
Route When compared to Accessible
www.example.com/test www.example.com/test Yes
www.example.com No
www.example.com/test and www.example.com/test Yes
www.example.com
www.example.com Yes
www.example.com www.example.com/text Yes (Matched by the host, not the
route)
www.example.com Yes
Example of an unsecured route with a path
apiVersion: route.openshift.io/v1
kind: Route
metadata:
name: route-unsecured
spec:
host: www.example.com
path: "/test"
to:
kind: Service
name: service-name
spec.host: Specifies the path attribute for a path-based route.
NOTE
Path-based routing is not available when using passthrough TLS, as the router does not
terminate TLS in that case and cannot read the contents of the request.
7.7. HTTP HEADER CONFIGURATION
To customize request and response headers, modify individual route configurations or apply route
84

CHAPTER 7. CONFIGURING ROUTES
To customize request and response headers, modify individual route configurations or apply route
annotations. Understanding the interaction between these methods ensures you effectively manage
header policies and resolve potential configuration conflicts.
The various ways of configuring headers can present challenges when working together.
NOTE
You can only set or delete headers within a Route CR. You cannot append headers. If an
HTTP header is set with a value, that value must be complete and not require appending
in the future. In situations where it makes sense to append a header, such as the X-
Forwarded-For header, use the spec.httpHeaders.forwardedHeaderPolicy field,
instead of spec.httpHeaders.actions.
Example Route spec
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
httpHeaders:
actions:
response:
- name: X-Frame-Options
action:
type: Set
set:
value: SAMEORIGIN
Any actions defined in a route override values set using route annotations.
Special case headers
The following headers are either prevented entirely from being set or deleted, or allowed under
specific circumstances:
Header name Configurable using Reason for Configurable using
Route spec disallowment another method
proxy No The proxy HTTP No
request header can be
used to exploit
vulnerable CGI
applications by injecting
the header value into
the HTTP_PROXY
environment variable.
The proxy HTTP
request header is also
non-standard and prone
to error during
configuration.
85

Red Hat build of MicroShift 4.22 Networking
Header name Configurable using  Reason for Configurable using
|      | Route spec | disallowment       | another method |
| ---- | ---------- | ------------------ | -------------- |
| host | Yes        | When the host HTTP | No             |
request header is set
using the
IngressController CR,
HAProxy can fail when
looking up the correct
route.
| strict-transport- |     | The strict-transport- |                      |
| ----------------- | --- | --------------------- | -------------------- |
|                   | No  |                       | Yes: the             |
| security          |     | security HTTP         | haproxy.router.open  |
|                   |     | response header is    | shift.io/hsts_header |
|                   |     | already handled using | route annotation     |
route annotations and
does not need a
separate
implementation.
| cookie and set- | No  | The cookies that      | Yes: |
| --------------- | --- | --------------------- | ---- |
| cookie          |     | HAProxy sets are used |      |
* the
for session tracking to
|     |     | map client connections | haproxy.router.open   |
| --- | --- | ---------------------- | --------------------- |
|     |     | to particular back-end | shift.io/disable_cook |
ie route annotation * the
servers. Allowing these
|     |     | headers to be set could  | haproxy.router.open  |
| --- | --- | ------------------------ | -------------------- |
|     |     | interfere with HAProxy’s | shift.io/cookie_name |
|     |     | session affinity and     | route annotation     |
restrict HAProxy’s
ownership of a cookie.
7.8. SET OR DELETE HTTP REQUEST AND RESPONSE HEADERS IN A
ROUTE
You can set or delete certain HTTP request and response headers for compliance purposes or other
reasons. You can set or delete these headers either for all routes served by an Ingress Controller or for
specific routes.
For example, you might want to enable a web application to serve content in alternate locations for
specific routes if that content is written in multiple languages, even if there is a default global location
specified by the Ingress Controller serving the routes.
The following procedure creates a route that sets the Content-Location HTTP request header so that
the URL associated with the application, https://app.example.com, directs to the location
https://app.example.com/lang/en-us. Directing application traffic to this location means that anyone
using that specific route is accessing web content written in American English.
Prerequisites
You have installed the OpenShift CLI (oc).
86

CHAPTER 7. CONFIGURING ROUTES
You are logged into an Red Hat build of MicroShift cluster as a project administrator.
You have a web application that exposes a port and an HTTP or TLS endpoint listening for
traffic on the port.
Procedure
1. Create a route definition and save it in a file called app-example-route.yaml:
YAML definition of the created route with HTTP header directives
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
host: app.example.com
tls:
termination: edge
to:
kind: Service
name: app-example
httpHeaders:
actions:
response:
- name: Content-Location
action:
type: Set
set:
value: /lang/en-us
# ...
where:
actions
Specifies the list of actions you want to perform on the HTTP headers.
response
Specifies the type of header you want to change. In this case, a response header.
response.name
Specifies the name of the header you want to change. For a list of available headers you can
set or delete, see HTTP header configuration.
action.type
Specifies the type of action being taken on the header. This field can have the value Set or
Delete.
set.value
When setting HTTP headers, you must provide a value. The value can be a string from a list
of available directives for that header, for example DENY, or it can be a dynamic value that
will be interpreted using HAProxy’s dynamic value syntax. In this case, the value is set to the
relative location of the content.
2. Create a route to your existing web application using the newly created route definition:
$ oc -n app-example create -f app-example-route.yaml
87

Red Hat build of MicroShift 4.22 Networking
For HTTP request headers, the actions specified in the route definitions are executed after any
actions performed on HTTP request headers in the Ingress Controller. This means that any
values set for those request headers in a route will take precedence over the ones set in the
Ingress Controller. For more information on the processing order of HTTP headers, see HTTP
header configuration.
7.9. CREATE A ROUTE THROUGH AN INGRESS OBJECT
To integrate ecosystem components that require Ingress resources, configure an Ingress object. Red
Hat build of MicroShift automatically manages the lifecycle of the corresponding route objects, creating
and deleting them to ensure seamless connectivity.
Prerequisites
If clients must receive a full certificate chain, you must combine the PEM-encoded leaf
certificate and intermediates into a single file. Place the leaf certificate first, followed by each
issuer in chain order.
You confirmed the private key matches the leaf certificate in the tls.crt key.
You confirmed the tls.key key has only the private key for the leaf certificate.
The certificate Subject Alternative Name (SAN), or the subject CN if no SAN is present, covers
every hostname set in spec.rules[].host and spec.tls[].hosts. These values must match for the
same host.
The private key is not password-encrypted. You must decrypt the key before you create the
TLS secret so that Red Hat build of MicroShift can read the key material.
You created a Secret of type kubernetes.io/tls in the same namespace as the Ingress. The
secretName must match the spec.tls[].secretName field. If you have not created the secret,
you must do so before you apply the Ingress object.
Procedure
1. Define an Ingress object in the Red Hat build of MicroShift console or by entering the oc create
command:
YAML Definition of an Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
name: frontend
annotations:
route.openshift.io/termination: "reencrypt"
route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
spec:
rules:
- host: www.example.com
http:
paths:
- backend:
service:
88

CHAPTER 7. CONFIGURING ROUTES
name: frontend
port:
number: 443
path: /
pathType: Prefix
tls:
- hosts:
- www.example.com
secretName: example-com-tls-certificate
# ...
where:
route.openshift.io/termination
Specifies the route.openshift.io/termination annotation. You can configure the
spec.tls.termination parameter of the Route because Ingress does not have this
parameter. The accepted values are edge, passthrough, and reencrypt. All other values are
silently ignored. When the annotation value is unset, edge is the default route. The TLS
certificate details must be defined in the template file to implement the default edge route.
rules.host
Specifies an explicit hostname for the Ingress object. Mandatory parameter. You can use
the <host_name>.<cluster_ingress_domain> syntax, for example
apps.openshiftdemos.com, to take advantage of the *.<cluster_ingress_domain>
wildcard DNS record and serving certificate for the cluster. Otherwise, you must ensure that
there is a DNS record for the chosen hostname.
destination-ca-certificate-secret
Specifies the route.openshift.io/destination-ca-certificate-secret annotation. The
annotation can be used on an Ingress object to define a route with a custom destination
certificate (CA). The annotation references a kubernetes secret, secret-ca-cert that will be
inserted into the generated route.
a. If you specify the passthrough value in the route.openshift.io/termination annotation,
set path to '' and pathType to ImplementationSpecific in the spec:
apiVersion: networking.k8s.io/v1
kind: Ingress
# ...
spec:
rules:
- host: www.example.com
http:
paths:
- path: ''
pathType: ImplementationSpecific
backend:
service:
name: frontend
port:
number: 443
# ...
$ oc apply -f ingress.yaml
b. To specify a route object with a destination CA from an ingress object, you must create a
89

Red Hat build of MicroShift 4.22 Networking
b. To specify a route object with a destination CA from an ingress object, you must create a
kubernetes.io/tls or Opaque type secret with a certificate in PEM-encoded format in
the data.tls.crt specifier of the secret.
2. List your routes:
$ oc get routes
The result includes an autogenerated route whose name starts with frontend-:
NAME HOST/PORT PATH SERVICES PORT TERMINATION
WILDCARD
frontend-gnztq www.example.com frontend 443 reencrypt/Redirect None
YAML definition example of an autogenerated route
apiVersion: route.openshift.io/v1
kind: Route
metadata:
name: frontend-gnztq
ownerReferences:
- apiVersion: networking.k8s.io/v1
controller: true
kind: Ingress
name: frontend
uid: 4e6c59cc-704d-4f44-b390-617d879033b6
spec:
host: www.example.com
path: /
port:
targetPort: https
tls:
certificate: |
-----BEGIN CERTIFICATE-----
[...]
-----END CERTIFICATE-----
insecureEdgeTerminationPolicy: Redirect
key: |
-----BEGIN RSA PRIVATE KEY-----
[...]
-----END RSA PRIVATE KEY-----
termination: reencrypt
destinationCACertificate: |
-----BEGIN CERTIFICATE-----
[...]
-----END CERTIFICATE-----
to:
kind: Service
name: frontend
7.10. CREATE A ROUTE USING THE DEFAULT CERTIFICATE THROUGH
AN INGRESS OBJECT
90

CHAPTER 7. CONFIGURING ROUTES
To generate a secure, edge-terminated route that uses the default ingress certificate, specify an empty
TLS configuration in the Ingress object. This configuration overrides the default behavior, preventing
the creation of an insecure route.
Prerequisites
You have a service that you want to expose.
You have access to the OpenShift CLI (oc).
Procedure
1. Create a YAML file for the Ingress object. In the following example, the file is called example-
ingress.yaml:
YAML definition of an Ingress object
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
name: frontend
...
spec:
rules:
...
tls:
- {}
where:
spec.tls
Specifies the TLS configuration. Use the exact syntax shown to specify TLS without
specifying a custom certificate.
2. Create the Ingress object by running the following command:
$ oc create -f example-ingress.yaml
Verification
Verify that Red Hat build of MicroShift has created the expected route for the Ingress object by
running the following command:
$ oc get routes -o yaml
Example output
apiVersion: v1
items:
- apiVersion: route.openshift.io/v1
kind: Route
metadata:
name: frontend-j9sdd
91

Red Hat build of MicroShift 4.22 Networking
# ...
spec:
...
tls:
insecureEdgeTerminationPolicy: Redirect
termination: edge
# ...
where:
metadata.name
Specifies the name of the route, which includes the name of the Ingress object followed by a
random suffix.
spec.tls
To use the default certificate, the route should not specify spec.certificate.
tls.termination
Specifies the termination policy for the route. The route should specify the edge termination
policy.
7.11. CREATE A ROUTE USING THE DESTINATION CA CERTIFICATE IN
THE INGRESS ANNOTATION
To define a route with a custom destination CA certificate, apply the route.openshift.io/destination-
ca-certificate-secret annotation to an Ingress object. This configuration ensures the Ingress Controller
uses the specified secret to verify the identity of the destination service.
Prerequisites
You have a certificate/key pair in PEM-encoded files, where the certificate is valid for the route
host.
You have a separate CA certificate in a PEM-encoded file that completes the certificate chain.
You have a separate destination CA certificate in a PEM-encoded file.
You have a service that you want to expose.
Procedure
1. Create a secret for the destination CA certificate by entering the following command:
$ oc create secret generic dest-ca-cert --from-file=tls.crt=<file_path>
For example:
$ oc -n test-ns create secret generic dest-ca-cert --from-file=tls.crt=tls.crt
Example output
secret/dest-ca-cert created
92

CHAPTER 7. CONFIGURING ROUTES
2. Add the route.openshift.io/destination-ca-certificate-secret to the Ingress annotations:
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
name: frontend
annotations:
route.openshift.io/termination: "reencrypt"
route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
...
where:
destination-ca-certificate-secret
Specifies the route.openshift.io/destination-ca-certificate-secret annotation. The
annotation references a Kubernetes secret.
The Ingress Controller inserts a secret that is referenced in the annotation into the
generated route.
Example output
apiVersion: route.openshift.io/v1
kind: Route
metadata:
name: frontend
annotations:
route.openshift.io/termination: reencrypt
route.openshift.io/destination-ca-certificate-secret: secret-ca-cert
spec:
...
tls:
insecureEdgeTerminationPolicy: Redirect
termination: reencrypt
destinationCACertificate: |
-----BEGIN CERTIFICATE-----
[...]
-----END CERTIFICATE-----
...
Additional resources
Creating a re-encrypt route with a custom certificate
Creating an edge route with a custom certificate
Creating a passthrough route
93

Red Hat build of MicroShift 4.22 Networking
CHAPTER 8. USING A FIREWALL
Firewalls are not required in MicroShift, but using a firewall can prevent undesired access to the
MicroShift API.
8.1. ABOUT NETWORK TRAFFIC THROUGH THE FIREWALL
Firewalld is a networking service that runs in the background and responds to connection requests,
creating a dynamic customizable host-based firewall. If you are using Red Hat Enterprise Linux for Edge
(RHEL for Edge) with MicroShift, firewalld should be installed and you only need to configure it.
Details are provided in procedures that follow. Overall, you must explicitly allow the following OVN-
Kubernetes traffic when the firewalld service is running.
CNI pod to CNI pod
CNI pod to Host-Network pod Host-Network pod to Host-Network pod
CNI pod
The Kubernetes pod that uses the CNI network
Host-Network pod
The Kubernetes pod that uses host network You can configure the firewalld service by using the
following procedures. In most cases, firewalld is part of RHEL for Edge installations. If you do not have
firewalld, you can install it with the simple procedure in this section.
IMPORTANT
MicroShift pods must have access to the internal CoreDNS component and API servers.
Additional resources
Required firewall settings
Allowing network traffic through the firewall
8.2. INSTALL THE FIREWALLD SERVICE
To install and enable firewalld on your RHEL for Edge host when the package is missing, you can use dnf
to install the package and systemctl to enable and start the service. Optionally check for the package
with rpm -q firewalld before you install.
Procedure
1. Optional: Check for firewalld on your system by running the following command:
$ rpm -q firewalld
2. If the firewalld service is not installed, run the following command:
$ sudo dnf install -y firewalld
3. To start the firewall, run the following command:
94

CHAPTER 8. USING A FIREWALL
$ sudo systemctl enable firewalld --now
8.3. REQUIRED FIREWALL SETTINGS
An IP address range for the node network must be enabled during firewall configuration. You can use
the default values or customize the IP address range.
If you choose to customize the node network IP address range from the default 10.42.0.0/16 setting,
you must also use the same custom range in the firewall configuration.
Table 8.1. Firewall IP address settings
IP Range Firewall rule required Description
10.42.0.0/16 No Host network pod access to other
pods
169.254.169.1 Yes Host network pod access to Red
Hat build of MicroShift API server
8.3.1. Example commands
The following are examples of commands for settings that are mandatory for firewall configuration:
Configure host network pod access to other pods:
$ sudo firewall-cmd --permanent --zone=trusted --add-source=10.42.0.0/16
Configure host network pod access to services backed by Host endpoints, such as the Red Hat
build of MicroShift API:
$ sudo firewall-cmd --permanent --zone=trusted --add-source=169.254.169.1
8.4. USE OPTIONAL PORT SETTINGS
To allow external access to services and APIs in MicroShift, you can add custom ports to your firewall
configuration. Use the listed ports and protocols as a guide for HTTP, HTTPS, NodePort, mDNS, and
API access.
For a complete list of ports and protocols, see "Optional ports".
The following examples show commands to open firewall access for services running on MicroShift.
Procedure
To add customized ports to your firewall configuration, use the following command syntax:
$ sudo firewall-cmd --permanent --zone=public --add-port=<port number>/<port protocol>
For example, to configure a port for the MicroShift API server, enter the following command:
95

Red Hat build of MicroShift 4.22 Networking
$ sudo firewall-cmd --permanent --zone=public --add-port=6443/tcp
To close unnecessary ports in your MicroShift instance, follow the procedure in "Closing unused
or unnecessary ports to enhance network security".
8.4.1. Optional ports
The following table lists the optional ports that are available for use with the MicroShift firewall service.
Table 8.2. Optional ports
| Port(s) | Protocol(s) | Description             |
| ------- | ----------- | ----------------------- |
| 80      | TCP         | HTTP port used to serve |
applications through the
OpenShift Container Platform
router.
| 443 | TCP | HTTPS port used to serve |
| --- | --- | ------------------------ |
applications through the
OpenShift Container Platform
router.
| 5353 | UDP | mDNS service to respond for |
| ---- | --- | --------------------------- |
OpenShift Container Platform
route mDNS hosts.
| 30000-32767 | TCP | Port range reserved for NodePort |
| ----------- | --- | -------------------------------- |
services; can be used to expose
applications on the LAN.
| 30000-32767 | UDP | Port range reserved for NodePort |
| ----------- | --- | -------------------------------- |
services; can be used to expose
applications on the LAN.
| 6443 | TCP | HTTPS API port for the Red Hat |
| ---- | --- | ------------------------------ |
build of MicroShift API.
Additional resources
Closing unused or unnecessary ports to enhance network security
8.5. ADD SERVICES TO OPEN PORTS
To open default ports for predefined services through firewalld on your MicroShift instance, you can use
the firewall-cmd command. Add each service with the --add-service option.
Procedure
1.  Optional: You can view all predefined services in firewalld by running the following command
96

CHAPTER 8. USING A FIREWALL
$ sudo firewall-cmd --get-services
2. To open a service that you want on a default port, run the following example command:
$ sudo firewall-cmd --add-service=mdns
8.6. ALLOWING NETWORK TRAFFIC THROUGH THE FIREWALL
You can allow network traffic through the firewall by configuring the IP address range and inserting the
DNS server to allow internal traffic from pods through the network gateway.
Procedure
1. Use one of the following commands to set the IP address range:
a. Configure the IP address range with default values by running the following command:
$ sudo firewall-offline-cmd --permanent --zone=trusted --add-source=10.42.0.0/16
b. Configure the IP address range with custom values by running the following command:
$ sudo firewall-offline-cmd --permanent --zone=trusted --add-source=<custom IP range>
2. To allow internal traffic from pods through the network gateway, run the following command:
$ sudo firewall-offline-cmd --permanent --zone=trusted --add-source=169.254.169.1
3. If you are using a load balancer, allow the IPv6 traffic through the firewall by running the
following command:
$ sudo firewall-cmd --permanent --zone=trusted --add-source=fd01::/48
8.7. APPLYING FIREWALL SETTINGS
To apply firewall settings after you have finished configuring network access through the firewall, you
can reload the firewall service.
Procedure
Restart the firewall and apply the settings by running the following command:
$ sudo firewall-cmd --reload
8.8. VERIFY FIREWALL SETTINGS
After you have restarted the firewall, you can verify your settings by listing them with the firewall-cmd
command.
Procedure
To verify rules added in the default public zone, such as ports-related rules, run the following
97

Red Hat build of MicroShift 4.22 Networking
To verify rules added in the default public zone, such as ports-related rules, run the following
command:
$ sudo firewall-cmd --list-all
To verify rules added in the trusted zone, such as IP-range related rules, run the following
command:
$ sudo firewall-cmd --zone=trusted --list-all
8.9. OVERVIEW OF FIREWALL PORTS WHEN A SERVICE IS EXPOSED
Firewalld is often active when you run services on MicroShift. This can disrupt certain services on
MicroShift because traffic to the ports might be blocked by the firewall.
You must ensure that the necessary firewall ports are open if you want certain services to be accessible
from outside the host.
There are several options for opening your ports:
Services of the NodePort and LoadBalancer type are automatically available with OVN-
Kubernetes.
In these cases, OVN-Kubernetes adds iptables rules so the traffic to the node IP address is
delivered to the relevant ports. This is done using the PREROUTING rule chain and is then
forwarded to the OVN-K to bypass the firewalld rules for local host ports and services. Iptables
and firewalld are backed by nftables in Red Hat Enterprise Linux (RHEL) 9. The nftables rules,
which the iptables generates, always have priority over the rules that the firewalld generates.
Pods with the HostPort parameter settings are automatically available. This also includes the
router-default pod, which uses ports 80 and 443.
For HostPort pods, the CRI-O config sets up iptables DNAT (Destination Network Address
Translation) to the pod’s IP address and port.
These methods function for clients whether they are on the same host or on a remote host. The iptables
rules, which are added by OVN-Kubernetes and CRI-O, attach to the PREROUTING and OUTPUT
chains. The local traffic goes through the OUTPUT chain with the interface set to the lo type. The
DNAT runs before it hits filler rules in the INPUT chain.
Because the MicroShift API server does not run in CRI-O, it is subject to the firewall configurations. You
can open port 6443 in the firewall to access the API server in your MicroShift node.
8.10. ADDITIONAL RESOURCES
RHEL: Using and configuring firewalld
RHEL: Viewing the current status of firewalld
8.11. KNOWN FIREWALL ISSUE
To avoid traffic failures after a firewalld reload or restart on MicroShift, run firewall commands before
you start Red Hat Enterprise Linux (RHEL).
If you must run firewall commands later, restart the ovnkube-master pod in openshift-ovn-kubernetes
to restore iptable rules that OVN-Kubernetes manages.
98

CHAPTER 8. USING A FIREWALL
The CNI driver in MicroShift makes use of iptable rules for some traffic flows, such as those using the
NodePort service. The iptable rules are generated and inserted by the CNI driver, but are deleted when
the firewall reloads or restarts. The absence of the iptable rules breaks traffic flows.
99

Red Hat build of MicroShift 4.22 Networking
CHAPTER 9. CONFIGURING NETWORK SETTINGS FOR FULLY
DISCONNECTED HOSTS
Learn how to apply networking customization and settings to run MicroShift on fully disconnected
hosts. A disconnected host should be the Red Hat Enterprise Linux (RHEL) operating system, versions
9.0+, whether real or virtual, that runs without network connectivity.
9.1. PREPARING NETWORKING FOR FULLY DISCONNECTED HOSTS
To run MicroShift on a fully disconnected host with no external network connectivity, you prepare a
persistent hostname, loopback IP addressing, DNS, and /etc/hosts entries before you apply MicroShift
network configuration.
Typically this means that the device does not have an attached network interface controller (NIC) to
provide a subnet. These steps can also be completed on a host with a NIC that is removed after setup.
You can also automate these steps on a host that does not have a NIC by using the %post phase of a
Kickstart file.
IMPORTANT
Configuring networking settings for disconnected environments is necessary because
MicroShift requires a network device to support node communication. To meet this
requirement, you must configure MicroShift networking settings to use the "fake" IP
address you assign to the system loopback device during setup.
9.1.1. Procedure summary
To run MicroShift on a disconnected host, the following steps are required:
Prepare the host
Stop MicroShift if it is currently running and clean up changes the service has made to the
network.
Set a persistent hostname.
Add a “fake” IP address on the loopback interface.
Configure DNS to use the fake IP as local name server.
Add an entry for the hostname to /etc/hosts.
Update the MicroShift configuration
Define the nodeIP parameter as the new loopback IP address.
Set the .node.hostnameOverride parameter to the persistent hostname.
For the changes to take effect
Disable the default NIC if attached.
Restart the host or device.
100

CHAPTER 9. CONFIGURING NETWORK SETTINGS FOR FULLY DISCONNECTED HOSTS
After starting, MicroShift runs using the loopback device for intra-node communication.
9.2. RESTORING MICROSHIFT NETWORKING SETTINGS TO DEFAULT
To remove networking customizations and return the network to default settings, stop MicroShift and
run a clean-up script.
Prerequisites
RHEL 9 or newer.
MicroShift 4.14 or newer.
Access to the host CLI.
Procedure
1. Stop the MicroShift service by running the following command:
$ sudo systemctl stop microshift
2. Stop the kubepods.slice systemd unit by running the following command:
$ sudo systemctl stop kubepods.slice
3. MicroShift installs a helper script to undo network changes made by OVN-K. Run the cleanup
script by entering the following command:
$ sudo /usr/bin/microshift-cleanup-data --ovn
9.3. CONFIGURING THE NETWORKING SETTINGS FOR FULLY
DISCONNECTED HOSTS
To configure the networking settings for running MicroShift on a fully disconnected host, you must
prepare the host, update the networking configuration, then restart to apply the new settings. All
commands are executed from the host CLI.
Prerequisites
RHEL 9 or newer.
MicroShift 4.16 or newer.
Access to the host CLI.
A valid IP address chosen to avoid both internal and potential future external IP conflicts when
running MicroShift.
MicroShift networking settings are set to defaults.
IMPORTANT
101

Red Hat build of MicroShift 4.22 Networking
IMPORTANT
The following procedure is for use cases in which access to the MicroShift node is not
required after devices are deployed in the field. There is no remote node access after the
network connection is removed.
Procedure
1. Add a fake IP address to the loopback interface by running the following command:
$ IP="10.44.0.1"
The fake IP address used in this example is "10.44.0.1".
$ sudo nmcli con add type loopback con-name stable-microshift ifname lo ip4 ${IP}/32
NOTE
Any valid IP works if it avoids both internal MicroShift and potential future
external IP conflicts. This can be any subnet that does not collide with the
MicroShift node subnet or is be accessed by other services on the device.
2. Configure the DNS interface to use the local name server by setting modifying the settings to
ignore automatic DNS and reset it to the local name server:
a. Bypass the automatic DNS by running the following command:
$ sudo nmcli conn modify stable-microshift ipv4.ignore-auto-dns yes
b. Point the DNS interface to use the local name server:
$ sudo nmcli conn modify stable-microshift ipv4.dns "10.44.1.1"
3. Get the hostname of the device by running the following command:
$ NAME="$(hostnamectl hostname)"
4. Add an entry for the hostname of the node in the /etc/hosts file by running the following
command:
$ echo "$IP $NAME" | sudo tee -a /etc/hosts >/dev/null
5. Update the MicroShift configuration file by adding the following YAML snippet to
/etc/microshift/config.yaml:
sudo tee /etc/microshift/config.yaml > /dev/null <<EOF
node:
hostnameOverride: $(echo $NAME)
nodeIP: $(echo $IP)
EOF
6. MicroShift is now ready to use the loopback device for intra-node communications. Finish
102

CHAPTER 9. CONFIGURING NETWORK SETTINGS FOR FULLY DISCONNECTED HOSTS
6. MicroShift is now ready to use the loopback device for intra-node communications. Finish
preparing the device for offline use.
a. If the device currently has a NIC attached, disconnect the device from the network.
b. Shut down the device and disconnect the NIC.
c. Restart the device for the offline configuration to take effect.
7. Restart the MicroShift host to apply the configuration changes by running the following
command:
$ sudo systemctl reboot
This step restarts the node. Wait for the greenboot health check to report the system healthy
before implementing verification.
Verification
At this point, network access to the MicroShift host has been severed. If you have access to the host
terminal, you can use the host CLI to verify that the node has started in a stable state.
1. Verify that the MicroShift node is running by entering the following commands:
$ export KUBECONFIG=/var/lib/microshift/resources/kubeadmin/kubeconfig
$ sudo -E oc get pods -A
Example output
NAMESPACE NAME READY STATUS RESTARTS
AGE
kube-system csi-snapshot-controller-74d566564f-66n2f 1/1 Running 0
1m
openshift-dns dns-default-dxglm 2/2 Running 0 1m
openshift-dns node-resolver-dbf5v 1/1 Running 0 1m
openshift-ingress router-default-8575d888d8-xmq9p 1/1 Running 0
1m
openshift-ovn-kubernetes ovnkube-master-gcsx8 4/4 Running 1 1m
openshift-ovn-kubernetes ovnkube-node-757mf 1/1 Running 1 1m
openshift-service-ca service-ca-7d7c579f54-68jt4 1/1 Running 0 1m
openshift-storage topolvm-controller-6d777f795b-bx22r 5/5 Running 0
1m
openshift-storage topolvm-node-fcf8l 4/4 Running 0 1m
103