import socket
import ipaddress
import threading

# Function to scan a single port on an IP address
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"Port {port} is open on {ip}")
        return True
    except:
        return False
    finally:
        s.close()

# Function to scan a single IP address for RDP
def scan_ip_for_rdp(ip):
    if scan_port(ip, 3389):
        print(f"RDP is open on {ip}")

# Function to scan a network for active devices and check for RDP
def scan_network_for_rdp(network):
    threads = []
    for ip in ipaddress.IPv4Network(network):
        thread = threading.Thread(target=scan_ip_for_rdp, args=(str(ip),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    network = input("Enter the network (e.g., 192.168.1.0/24): ")
    scan_network_for_rdp(network)