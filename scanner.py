import socket


def check_port(host,port, timeout) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0
    


host = "127.0.0.1" 
port = 8000
timeout = 1.0

print(f"{host}::{port} --> {check_port(host,port, timeout)}")