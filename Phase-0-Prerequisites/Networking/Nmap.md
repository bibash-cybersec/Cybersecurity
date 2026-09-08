# Nmap

Nmap (Network Mapper) is the primary reconnaissance tool used across both offensive pentesting and defensive network auditing.


### General Nmap Syntax:
nmap [Scan Type(s)] [Options] [Target IP/Subnet]

1. Essential Scan Types & Flags
   

Flag          | Meaning                       | Description
--------------|-------------------------------|---------------------------------------------------------
-sS           | TCP SYN Scan                  | Fast, half-open stealth scan (requires sudo)
-sT           | TCP Connect Scan              | Full 3-way handshake scan (no sudo required)
-sU           | UDP Scan                      | Scans UDP services (DNS, SNMP, DHCP)
-sV           | Service Version Detection     | Probes open ports to determine software version
-O            | OS Detection                  | Analyzes TCP/IP stack fingerprint to guess the OS
-A            | Aggressive Scan               | Enables OS detection, Version detection, Script scan, Traceroute
-sn           | Ping Sweep (No Port Scan)     | Discovers live hosts on a subnet without port scanning


2. Port Specification & Speed Controls


Flag          | Target Ports
--------------|---------------------------------------------------------
-p 80,443     | Scans only ports 80 and 443
-p 1-1000     | Scans ports 1 through 1000
-p-           | Scans ALL 65,535 TCP ports (Critical during real pentests!)
--top-ports 100 | Scans the 100 most common ports

Timing Templates (-T0 to -T5):

├── -T0 (Paranoid): Extremely slow, avoids IDS detection

├── -T2 (Polite): Slow, reduces network bandwidth usage

├── -T3 (Normal): Default speed

├── -T4 (Aggressive): Fast, recommended for CTFs/stable networks

└── -T5 (Insane): Very fast, can miss ports if network drops packets


3. Nmap Scripting Engine (NSE)
NSE scripts automate vulnerability checks, service enumeration, and advanced discovery.

### Script Categories:

--script=default      # Standard safe enumeration scripts (-sC does this)

--script=vuln         # Checks target for known CVEs/vulnerabilities

--script=safe         # Runs only non-intrusive scripts

--script=auth         # Tests for default/bypassed credentials


### Examples:
sudo nmap -sV --script=vuln 192.168.1.50

sudo nmap --script=http-title,http-headers 192.168.1.50

4. Saving Output Formats

-oN scan.txt       # Normal human-readable format

-oX scan.xml       # XML format (used for importing into Metasploit/tools)

-oG scan.gnmap     # Grepable format (great for awk/grep filtering)

-oA full_scan      # Outputs ALL THREE formats at once (Best Practice!)

💡 The Golden Professional Nmap Scan Command:

sudo nmap -sC -sV -p- -T4 -oA initial_scan <TARGET_IP>
