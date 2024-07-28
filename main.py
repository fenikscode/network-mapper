import nmap
import json
from sql_control import SQLQuery, sql_connection_stack


# New Instance Of Nmap Class
scanner = nmap.PortScanner()

# ICMP Ping scan
result = scanner.scan('192.168.10.0/24', arguments='-sn -T5')

print(result)

# for host in result['scan']:
#     print(f'Host {}')

# Temp place for command above    
# result['scan'][host]['addresses']



# # Debug SCAN to JSON
# file = open('wyniki.csv', 'w')
# file.write(json.dumps(result, sort_keys=True, indent=5))
# file.close()

# # First Simple Scan
# scanner.scan('127.0.0.1', arguments='-p 22')

# # Print Results Of Scan
# print(scanner.scaninfo())
# print(scanner.all_hosts())