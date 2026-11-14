import socket
import sys

def check_port(host,port, timeout) -> bool:
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((host, port))
    except socket.gaierror:
        sys.exit(f"The hostname: \"{host}\" is invalid. Please correct it and try again!")     
    s.close()
    return result == 0

def scan_range(host, start, end, timeout) -> list[int]:
    open_ports = []
    for port in range(start,end+1):
        if check_port(host, port, timeout):
            open_ports.append(port)
    return open_ports




host = "no-such-host.invalid" 
timeout = 0.3

for port in scan_range(host, 7990, 8010, timeout):
    print(f"{host}::{port} --> OPEN")
