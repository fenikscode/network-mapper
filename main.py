import nmap
from random import seed, randint
from os import urandom
from socket import gethostbyname, gethostname
from sql_control import SQLQuery, sql_connection_stack

LOCAL_IP = gethostbyname(gethostname())

seed(urandom(10))

# New Instance Of Nmap Class
scanner = nmap.PortScanner()

query_set = SQLQuery(f'network_layout_dev_{randint(0, 9999999)}')
stack = [query_set.create_dataset()]

# Nmap Scan to determine all network data
result = scanner.scan('192.168.10.0/24', arguments='-sn -T5')

for host in result['scan']:
    if host == LOCAL_IP:    # This section skip local address to not raise error code xD
        continue
    stack.append(
        query_set.entry_add_dataset(
            result['scan'][host]['addresses']['mac'], 
            result['scan'][host]['addresses']['ipv4']
        )
    )

sql_connection_stack(stack)

# # Debug SCAN to JSON
# file = open('wyniki.csv', 'w')
# file.write(json.dumps(result, sort_keys=True, indent=5))
# file.close()

# # First Simple Scan
# scanner.scan('127.0.0.1', arguments='-p 22')

# # Print Results Of Scan
# print(scanner.scaninfo())
# print(scanner.all_hosts())