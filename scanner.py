import socket


def check_port(host,port, timeout) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0

def scan_range(host, start, end, timeout):
    open_ports = []
    for port in range(start,end):
        if check_port(host, port, timeout):
            open_ports.append(port)
    return open_ports




host = "127.0.0.1" 
timeout = 1.0

for port in scan_range(host, 7990, 8010, timeout):
    print(f"{host}::{port} --> OPEN")
