# Simulating writing logs to a file
sample_logs = """192.168.1.50 - SUCCESS - User login: admin
192.168.1.105 - FAILED - User login: root
192.168.1.105 - FAILED - User login: root
192.168.1.105 - FAILED - User login: test
192.168.1.200 - SUCCESS - User login: john"""

# Write mock log file
with open("auth_sim.log", "w") as f:
    f.write(sample_logs)

print("[+] Reading log file and searching for failed logins...\n")

# Reading and parsing the log file line by line
with open("auth_sim.log", "r") as f:
    for line in f:
        if "FAILED" in line:
            parts = line.strip().split(" - ")
            ip_address = parts[0]
            action = parts[2]
            print(f"[!] Alert: Suspicious activity from {ip_address} -> {action}")
