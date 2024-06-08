# Function to scan a list of IP addresses with a default timeout
def scan_ip(ip_list, timeout=5):
    """
    Scans a list of IP addresses with a specified timeout.
    """
    for ip in ip_list:
        # Print the IP and timeout value (simulated scan)
        print(f"Scanning {ip} with timeout {timeout} seconds.")

# Different types in Python
# Integer type
port_number = 8080

# Float type
response_time = 123.45

# String type
hostname = "example.com"

# Boolean type
is_secure = True

# List type
ports = [22, 80, 443]

# Set type
unique_ports = {22, 80, 443, 80}  # Duplicates are automatically removed

# Dictionary type
server_info = {
    "hostname": "example.com",
    "ip": "192.168.1.1",
    "ports": [22, 80, 443]
}

# Tuple type
credentials = ("admin", "password123")

# Lists are mutable
ports = [22, 80, 443]
ports[0] = 21  # Changing the first element

# Tuples are immutable
credentials = ("admin", "password123")
# credentials[0] = "user"  # This would raise an error

# List of ports
ports = [22, 80, 443]

# Multidimensional list representing a firewall rule table
firewall_rules = [
    ["ALLOW", "192.168.1.1", 22],
    ["DENY", "192.168.1.2", 80],
    ["ALLOW", "192.168.1.3", 443]

# For loop
for port in ports:
    print(f"Checking port {port}")

# While loop
i = 0
while i < len(ports):
    print(f"Checking port {ports[i]}")
    i += 1

# Nested loop for multidimensional lists
for rule in firewall_rules:
    for element in rule:
        print(element, end=" ")
    print()  # Newline after each rule

# Define a class for a Firewall rule
class FirewallRule:
    def __init__(self, action, ip, port):
        self.action = action  # Instance variable for action
        self.ip = ip  # Instance variable for IP address
        self.port = port  # Instance variable for port

    def display_rule(self):
        # Method to display the firewall rule
        print(f"{self.action} traffic from {self.ip} on port {self.port}")

# Create an object of FirewallRule
rule1 = FirewallRule("ALLOW", "192.168.1.1", 22)
rule1.display_rule()

# Inheritance
class AdvancedFirewallRule(FirewallRule):
    def __init__(self, action, ip, port, protocol):
        super().__init__(action, ip, port)
        self.protocol = protocol  # New instance variable for protocol

    def display_rule(self):
        # Overriding the display_rule method
        print(f"{self.action} {self.protocol} traffic from {self.ip} on port {self.port}")

# Create an object of AdvancedFirewallRule
rule2 = AdvancedFirewallRule("DENY", "192.168.1.2", 80, "TCP")
rule2.display_rule()

# Define a class with dunder methods
class IPAddress:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return f"IP Address: {self.address}"

    def __eq__(self, other):
        return self.address == other.address

# Create objects of IPAddress
ip1 = IPAddress("192.168.1.1")
ip2 = IPAddress("192.168.1.1")

print(ip1)  # Uses __str__ method
print(ip1 == ip2)  # Uses __eq__ method

# Web crawling basics using requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

# Fetch the webpage
response = requests.get("https://example.com")
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find and print all hyperlinks
    for link in soup.find_all('a'):
        print(link.get('href'))

# Original function to check open ports
def check_ports(ports):
    for port in ports:
        print(f"Checking port {port}")

# Refactored function with additional functionality
def check_ports(ports, hostname="localhost"):
    for port in ports:
        print(f"Checking port {port} on {hostname}")

# Take user input for an IP address
ip_address = input("Enter an IP address: ")
print(f"You entered: {ip_address}")

# Function with a docstring
def scan_port(ip, port):
    """
    Scans a specific port on a given IP address.

    Parameters:
    ip (str): The IP address to scan.
    port (int): The port number to scan.

    Returns:
    str: Result of the scan.
    """
    return f"Scanning port {port} on IP {ip}"

# Using the help function
help(scan_port)

# Check if a port is open or closed
def check_port_status(port):
    if port == 22:
        return "Port 22 is open."
    elif port == 80:
        return "Port 80 is open."
    else:
        return f"Port {port} is closed."

# Using format strings to display scan results
ip = "192.168.1.1"
port = 22
result = "open"

print(f"Scan result for {ip} on port {port}: {result}")

# This is a single-line comment

"""
This is a
multi-line comment
"""

# Function to check a port
def check_port(port):
    # Print the port number being checked
    print(f"Checking port {port}")

# Read a file with IP addresses
def read_ips(filename):
    try:
        with open(filename, 'r') as file:
            ips = file.readlines()
            return [ip.strip() for ip in ips]
    except FileNotFoundError:
        return "File not found."

# Importing the math module
import math

# Function to divide two numbers with exception handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)