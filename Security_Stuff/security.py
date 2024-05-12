'''

Practicing Security Topics and Ethical projects

Linux Cmd: Run "ipconfig" combine the IPv6 addresses and the subnet mask addr to get the IP Address Range for your network

'''
import subprocess
import re

def count_connected_devices():
    try:
        # Run the nmap command to scan the local network for active hosts
        nmap_output = subprocess.check_output(["nmap", "-sn", "10.0.0.0/24"]).decode("utf-8")
        
        # Extract IP addresses from the nmap output using regular expressions
        ip_addresses = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", nmap_output)
        
        # Exclude network and broadcast addresses
        connected_devices = [ip for ip in ip_addresses if not ip.endswith(".0") and not ip.endswith(".255")]

        return len(connected_devices)
    
    except subprocess.CalledProcessError:
        print("Error: Unable to run the nmap command.")
        return -1

if __name__ == "__main__":
    num_devices = count_connected_devices()
    if num_devices >= 0:
        print("Number of devices connected to the Wi-Fi network:", num_devices)
