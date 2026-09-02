### Domain Name System (DNS) — Port 53 (UDP/TCP)
DNS translates human-readable domain names (google.com) into computer-readable IP addresses (142.250.190.46).


The DNS Resolution Hierarchy:
1. Local Hosts file (/etc/hosts or C:\Windows\System32\drivers\etc\hosts)
2. Local DNS Cache
3. Recursive DNS Resolver (e.g., 8.8.8.8 or your ISP router)
4. Root Nameserver (. [dot])
5. TLD Nameserver (.com, .org, .gov)
6. Authoritative Nameserver (holds actual DNS records for the domain)
Common DNS Record Types:

Record | Name                  | Function
-------|-----------------------|------------------------------------------------
A      | Address Record        | Maps hostname to IPv4 address
AAAA   | IPv6 Address Record   | Maps hostname to IPv6 address
CNAME  | Canonical Name        | Alias (points a domain to another domain name)
MX     | Mail Exchange         | Specifies mail servers handling emails for domain
TXT    | Text Record           | Holds SPF, DKIM, DMARC records (Anti-phishing!)
PTR    | Pointer Record        | Reverse lookup (Maps IP back to hostname)
NS     | Name Server           | Delegates DNS zone to an authoritative server
SOA    | Start of Authority    | Administrative data about the DNS zone
2. Dynamic Host Configuration Protocol (DHCP) — Ports 67 & 68 (UDP)
DHCP automatically assigns IP addresses, subnet masks, default gateways, and DNS servers to connecting devices.

```
The DORA Process:

Client                                      DHCP Server
  │                                              │
  │──── Discover (Broadcast: 255.255.255.255) ──▶│ "Is there a DHCP server here?"
  │                                              │
  │◀─── Offer (Unicast/Broadcast) ───────────────│ "You can use IP 192.168.1.50"
  │                                              │
  │──── Request (Broadcast) ────────────────────▶│ "I accept IP 192.168.1.50"
  │                                              │
  │◀─── Acknowledge (ACK) ───────────────────────│ "IP 192.168.1.50 is leased to you!"
```
Security Attack Vector:

- DHCP Starvation Attack: Attacker spams fake MAC addresses sending DHCP Discovers to exhaust the entire IP pool.
- Rogue DHCP Server: Attacker sets up a rogue server responding to DHCP requests faster than the real router, giving victims the attacker's machine as the Default Gateway (Man-in-the-Middle).
