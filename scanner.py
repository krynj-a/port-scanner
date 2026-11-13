import socket


def check_port(HOST,PORT, timeout)->str:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((HOST, PORT))
    if result == 0: return True
    return  False
    s.close()


HOST = "127.0.0.1" 
PORT = 8000
timeout = 1.0

print(f"{HOST}::{PORT} --> {check_port(HOST,PORT, timeout)}")