# List of common ports to check:
common_ports = [21, 22, 23, 25, 53, 80, 
                110, 443, 445, 3306, 3389]

# List of vulnerable ports:
dangerous_ports = [23, 445, 3389]

print("Common ports in cybersecurity:")
print("="*40)

# Loop through ports:
for port in common_ports:
    if port in dangerous_ports:
        print(f"Port {port} ⚠️  HIGH RISK")
    else:
        print(f"Port {port} ✓")

print("="*40)
print(f"Total ports checked: {len(common_ports)}")
print(f"High risk ports: {len(dangerous_ports)}")
