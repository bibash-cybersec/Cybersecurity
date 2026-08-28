#### Why networking matters in cybersecurity ?
EVERY attack travels through a network
EVERY defense monitors network traffic

OSI Model = The foundation of ALL networking

### The 7 layers of OSI model and explanation
---
	Layer-7 Application
	User interaction directly with application
	protocol: HTTP, HTTPS, SSH, DNS, FTP
	data unit: data
	example: web browser 
	attack: SQL injection, XXS, Phishing

	Layer-6 Presentation
	translate, encrypt, compress
	protocol: SSL/TLS, JPEG, MPEG, ASCII
	data unit: data
	example: messages gets encrypt here
	attack: SSL stripping 

	Layer-5 Session 
	manages connection between applications
	protocol: NetBIOS, PPTP, RPC
	data unit: data
	example: keeps us logged in to a website
	attack: session hijacking

	Layer-4 Transport
	end-to-end communication, reliability
	protocol: TCP/UDP
	data unit: TCP (segment) UDP (datagram)
	example: makes sure all data arrives
	attack: SYN floods, port scanning

	Layer-3 Network
	logical addressing, routing
	protocol: IP, ICMP, ARP, 
	data unit: packet 
	device: router
	example: IP address live here
	attack: IP spoofing, MITM

	Layer-2 Data Link
	physical address (MAC address)
	protocol: Ethernet, Wifi, ARP
	data type: frames
	device: switch, bridge
	example: MAC address live here
	attack: MAC flooding, ARP spoofing

	Layer-1 Physical
	actual physical transmission of bits
	data type: bits (Os and 1s)
	devices: hub, repeater, cables
	example: ethernet cables, wifi signal 
	attack: cable taping, jamming
---
