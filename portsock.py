import socket

 

target_host = "example.com"
target_ports = [80, 443, 22, 3389]  # List of ports to scan
 

def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        sock.connect((host, port))
        print(f"Port {port} is open")
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        print(f"Port {port} is closed")

 

for port in target_ports:
    port_scan(target_host, port)