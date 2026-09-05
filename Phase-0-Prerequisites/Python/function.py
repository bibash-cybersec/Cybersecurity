# Function to classify ports based on risk level
def check_port_risk(port):
    critical_ports = [21, 23, 445, 3389]
    standard_ports = [80, 443, 53, 22]
    
    if port in critical_ports:
        return "CRITICAL RISK - Common exploitation target!"
    elif port in standard_ports:
        return "STANDARD SERVICE - Verify configuration."
    else:
        return "UNKNOWN / CUSTOM PORT"

target_port = 445
status = check_port_risk(target_port)
print(f"Port {target_port} Analysis: {status}")
