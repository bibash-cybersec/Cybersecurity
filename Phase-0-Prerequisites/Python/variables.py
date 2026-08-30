# String (text):
name = "John"
course = "Cybersecurity"
target_ip = "192.168.1.1"

# Integer (whole number):
port = 80
year = 2024
age = 25

# Float (decimal):
version = 2.4
score = 9.5

# Boolean (True/False):
is_vulnerable = True
is_patched = False
is_admin = False

# Print variables:
print("Name:", name)
print("Target IP:", target_ip)
print("Port:", port)
print("Is vulnerable:", is_vulnerable)

# String formatting (f-strings - very useful!):
print(f"Scanning {target_ip} on port {port}")
print(f"Apache version: {version}")

# Type checking:
print(type(name))     # <class 'str'>
print(type(port))     # <class 'int'>
print(type(is_vulnerable))  # <class 'bool'>
