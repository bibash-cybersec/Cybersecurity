### Structure of an IPv4 Address
An IPv4 address is 32 bits long, divided into 4 octets (8 bits each), separated by dots.

```
Decimal:   192   .   168   .    1    .    10

Binary:  11000000.10101000.00000001.00001010
```
Every IP address consists of two parts:

- Network ID: Identifies the specific network.
- Host ID: Identifies the specific device on that network.
The Subnet Mask defines where the Network ID ends and the Host ID begins.

### IP Address Classes (Traditional)
   
Class | Leading Bits | Range                     | Default Mask    | Purpose
------|--------------|---------------------------|-----------------|----------------------
A     | 0            | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 (/8)  | Huge organizations
B     | 10           | 128.0.0.0 – 191.255.255.255| 255.255.0.0 (/16)| Mid-size networks
C     | 110          | 192.0.0.0 – 223.255.255.255| 255.255.255.0 (/24)| Small Local LANs
D     | 1110         | 224.0.0.0 – 239.255.255.255| N/A             | Multicast
E     | 1111         | 240.0.0.0 – 255.255.255.255| N/A             | Experimental

*Note: 127.0.0.0/8 is reserved for Loopback (127.0.0.1 = localhost).

### Public vs. Private IP Addresses
Private IP addresses are non-routable over the public internet. They exist inside home and enterprise LANs behind NAT (Network Address Translation).
```
Private Ranges
├── Class A: 10.0.0.0    to 10.255.255.255   (10.0.0.0/8)
├── Class B: 172.16.0.0  to 172.31.255.255   (172.16.0.0/12)
└── Class C: 192.168.0.0 to 192.168.255.255 (192.168.0.0/16)
```
### CIDR Notation & Subnetting
CIDR (Classless Inter-Domain Routing) uses a /prefix representing how many bits belong to the network.

The Subnetting Cheat Sheet (For a single octet)

CIDR  | Subnet Mask       | Total Hosts | Usable Hosts (2ⁿ - 2)
------|-------------------|-------------|----------------------
/24   | 255.255.255.0     | 256         | 254
/25   | 255.255.255.128   | 128         | 126
/26   | 255.255.255.192   | 64          | 62
/27   | 255.255.255.224   | 32          | 30
/28   | 255.255.255.240   | 16          | 14
/29   | 255.255.255.248   | 8           | 6
/30   | 255.255.255.252   | 4           | 2 (Used for point-to-point links)
/32   | 255.255.255.255   | 1           | 1 (Single Host)

The "Minus 2" Rule:
In every subnet, two IP addresses cannot be assigned to endpoints:

Network Address (First IP): Identifies the subnet itself (e.g., 192.168.1.0).

Broadcast Address (Last IP): Sends data to all devices on that subnet (e.g., 192.168.1.255).
```
Practical Calculation Example:
Given: 192.168.1.68/26
/26 means 
32−26=6 host bits.
   
Block sizes: 0-63, 64-127, 128-191, 192-255.
68 falls in block 64-127:
Network ID: 192.168.1.64
First Usable IP: 192.168.1.65
Last Usable IP: 192.168.1.126
Broadcast IP: 192.168.1.127
```
