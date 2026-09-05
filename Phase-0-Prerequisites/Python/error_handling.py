# In cybersecurity tooling, scripts crash if a connection fails. We use try/except to prevent crashes.

try:
user_input = input("Enter port to scan: ")
    port = int(user_input)
    print(f"Targeting port: {port}")
except ValueError:
    print("[-] Error: Port must be a valid integer number (e.g., 80)!")
