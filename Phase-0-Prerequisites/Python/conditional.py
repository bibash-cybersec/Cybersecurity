port = int(input("Enter a port number: "))

# Check what service runs on this port:
if port == 22:
    print("SSH - Secure Shell")
    print("Risk: Brute force attacks possible")
elif port == 80:
    print("HTTP - Web Server (unencrypted)")
    print("Risk: Traffic can be intercepted")
elif port == 443:
    print("HTTPS - Secure Web Server")
    print("Risk: Lower - encrypted traffic")
elif port == 445:
    print("SMB - Windows File Sharing")
    print("Risk: HIGH - EternalBlue vulnerability!")
elif port == 3389:
    print("RDP - Remote Desktop Protocol")
    print("Risk: HIGH - Brute force target!")
elif port == 23:
    print("Telnet - INSECURE Remote Access")
    print("Risk: CRITICAL - Never use Telnet!")
else:
    print(f"Port {port} - Unknown or uncommon service")
    print("Research this port!")
