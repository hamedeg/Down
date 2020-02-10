import subprocess
import re
import ipaddress
print('#####################################################################')
print('This script to Shutdown or Restart Single IP, Range of IPs, IP Subnet in Microsoft Active Directory Environment ')
print('Auther: Hamed Adel')
print('#####################################################################')
userInput = input("Enter 1 for Single IP - 2 for Range of IP's - 3 for IP Subnet: ")
if userInput == '1':
    ip_add = input("Enter IP:")
    if not re.match(r'[0-9]+(?:\.[0-9]+){3}', ip_add):
        print('Invalid IP Address ',ip_add)
    else:
        remote_ip_add = str("\\\\")+str(ip_add)
        userOption = input("1 for Restart - 2 for Shutdown: ")
        if userOption == '1':
            res = subprocess.Popen(['shutdown', '-r','-m', remote_ip_add]).communicate()[0]
            print(res)
        elif userOption == '2':
            res = subprocess.Popen(['shutdown', '-s','-m', remote_ip_add]).communicate()[0]
            print(res)
        else:
            print('Invalid input!')

elif userInput == '2':
    s_ip_add = input("Start IP: ")
    e_ip_add = input("End IP: ")
    start_ip = ipaddress.IPv4Address(s_ip_add)
    end_ip = ipaddress.IPv4Address(e_ip_add)
    userOption = input("1 for Restart - 2 for Shutdown: ")
    if userOption == '1':
        for ip_int in range(int(start_ip), int(end_ip)):
            ip = ipaddress.IPv4Address(ip_int)
            remote_ip_add = str("\\\\")+str(ip)
            res = subprocess.Popen(['shutdown', '-r','-m', remote_ip_add]).communicate()[0]
            print(res)
    elif userOption == '2':
        for ip_int in range(int(start_ip), int(end_ip)):
            ip = ipaddress.IPv4Address(ip_int)
            remote_ip_add = str("\\\\")+str(ip)
            res = subprocess.Popen(['shutdown', '-s','-m', remote_ip_add]).communicate()[0]
            print(res)
    else:
        print('Invalid input!')
elif userInput == '3':
    ip_range = input("Enter IP subnet like 10.10.0.0/16: ")
    userOption = input("1 for Restart - 2 for Shutdown: ")
    if userOption == '1':
        for ip in ipaddress.IPv4Network(ip_range):
            remote_ip_add = str("\\\\")+str(ip)
            res = subprocess.Popen(['shutdown', '-r','-m', remote_ip_add]).communicate()[0]
            print(res)
    elif userOption == '2':
        for ip in ipaddress.IPv4Network(ip_range):
            remote_ip_add = str("\\\\")+str(ip)
            res = subprocess.Popen(['shutdown', '-s','-m', remote_ip_add]).communicate()[0]
            print(res)
    else:
        print('Invalid input!')
else:
    print('Invalid input!')
