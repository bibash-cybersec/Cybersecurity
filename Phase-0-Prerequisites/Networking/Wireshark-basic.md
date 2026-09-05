### Packet Analysis with Wireshark Basics
Wireshark is the world's most widely used Network Protocol Analyzer (Packet Sniffer).

```
Wireshark Interface Layout:
├── Top Pane: Packet List (No., Time, Source IP, Destination IP, Protocol, Length, Info)
├── Middle Pane: Packet Details (Shows OSI Layers: Frame -> Ethernet -> IP -> TCP -> App Data)
└── Bottom Pane: Packet Bytes (Hex Dump & ASCII output)
```

Essential Wireshark Display Filters:

Filter Expression                     | What It Filters
--------------------------------------|-----------------------------------------------
ip.addr == 192.168.1.1                | Packets to or from this IP
ip.src == 10.0.0.5                    | Packets originating from this source IP
ip.dst == 10.0.0.1                    | Packets heading to this destination
tcp.port == 80                        | HTTP traffic
tcp.port == 443                       | HTTPS traffic
udp.port == 53                        | DNS queries/responses
dns.qry.name contains "google"        | DNS queries matching string
http.request.method == "POST"         | HTTP form submissions (passwords, logins)
tcp.flags.syn == 1 && tcp.flags.ack == 0 | TCP connection initiation packets
icmp                                  | Ping traffic

