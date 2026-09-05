How Port Scanning Actually Works at the Wire Level

Port scanning is the process of sending packets to specific TCP or UDP ports on a target system to determine:
What ports are Open, Closed, or Filtered (firewalled). What services and software versions are listening on those ports.

```
Port State Definitions:
├── Open: The application is listening and accepts connections.
├── Closed: The host responds, but no application is listening (RST packet returned).
└── Filtered: A firewall or router drops/blocks the probe. No response or ICMP unreachable returned.
```

The Core TCP Scan Types
1. TCP Connect Scan (-sT)
Completes the full 3-way handshake (SYN → SYN-ACK → ACK).
Once established, it immediately tears down the connection with an RST or FIN.
- Pros: Does not require root/admin privileges to run.
- Cons: Extremely noisy; gets logged by almost every target server's application logs
```
Attacker                        Target
   │                              │
   │──── SYN (Port 80) ──────────▶│
   │◀─── SYN-ACK (Port Open) ─────│
   │──── ACK ────────────────────▶│ (Connection Established!)
   │──── RST/ACK ────────────────▶│ (Tear down connection)
```
   
2. TCP SYN Stealth Scan / Half-Open Scan (-sS) — Default Nmap Root Scan
Sends a SYN packet.
If the target responds with SYN-ACK (Port Open), the attacker immediately responds with RST (Reset) instead of ACK.
- Pros: Faster, stealthier (often never logged by target application because connection is never completed).
- Cons: Requires root or sudo privileges to craft raw packets.

```
Attacker                        Target
   │                              │
   │──── SYN (Port 80) ──────────▶│
   │◀─── SYN-ACK (Port Open) ─────│
   │──── RST (Reset connection!) ─▶│ (Connection aborted before logging)
If the port is Closed:

Attacker                        Target
   │                              │
   │──── SYN (Port 81) ──────────▶│
   │◀─── RST-ACK (Port Closed) ───│
```
   
3. UDP Port Scanning (-sU)
UDP is connectionless (no handshake).
Nmap sends an empty UDP packet to the port:
- If no response is received → Marked as Open|Filtered.
- If an ICMP Type 3 Code 3 (Port Unreachable) is returned → Marked as Closed.
- If a service-specific response is received → Marked as Open.

Note: UDP scans are significantly slower because operating systems rate-limit ICMP responses.
