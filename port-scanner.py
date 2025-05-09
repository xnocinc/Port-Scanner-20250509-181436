import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.100', '1-65535')
print(nm.csv())