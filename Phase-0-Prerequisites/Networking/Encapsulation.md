### How data travels in OSI model

Sending an email
- Layer-7 (Application) - actual message 
- layer-6 (Presentation) - message gets encrypt here(TLS)
- layer-5 (Session) - session ID added for track connection
- layer-4 (Transport) - TCP header added (source port, destination port) |TCP Header|Encrypted message|
- layer-3 (Network) - IP header added (source IP, destination IP) |IP Header|TCP Header|Encrypted message|
- layer-2 (Data Link) - MAC header added (source MAC, destination MAC) |MAC Header|IP Header|TCP Header|Encrypted message|
- layer-1 (Physical) - all data converted to bits and sent over cables and wifi

At the other end header are removed layer by layer until original email message received called Decapsulation.

NOTE: 

sending - Encapsulation

receiving - Decapsulation 
