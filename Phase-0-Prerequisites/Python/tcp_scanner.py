
#📌 TOPIC 3: Building a Custom TCP Port Scanner in Python
#Building a port scanner from scratch reinforces how the TCP transport layer functions programmatically.

#Create a file named tcp_scanner.py inside your Kali VM:


#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

# Define target
if len(sys.argv) == 2:
    target_host = sys.argv[1]
else:
    print("[-] Usage: python3 tcp_scanner.py <target_ip_or_domain>")
    sys.exit(1)

# Resolve target to IPv4
try:
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print("\n[-] Error: Hostname could not be resolved.")
    sys.exit(1)

print("-" * 50)
print(f"[*] Scanning Target: {target_ip} ({target_host})")
print(f"[*] Scan started at: {str(datetime.now())}")
print("-" * 50)

# List of critical ports to scan
ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]

try:
    for port in ports_to_scan:
        # Create a TCP socket: AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so the script doesn't hang forever on closed/filtered ports
        s.settimeout(1.0)
        
        # connect_ex returns 0 if the connection succeeded (port is open)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port:<5} : OPEN")
        else:
            # Non-zero indicates closed or filtered
            pass
            
        s.close()

except KeyboardInterrupt:
    print("\n[!] Scan cancelled by user.")
    sys.exit(0)

except socket.error:
    print("\n[-] Socket error occurred.")
    sys.exit(1)

print("-" * 50)
print("[*] Scan completed successfully.")
