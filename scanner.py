import socket
import sys
import argparse
import time
from concurrent.futures import ThreadPoolExecutor

def parse_args():
    parser = argparse.ArgumentParser(description="Localhost Port-Scanner in range Start-End with a timeout")
    parser.add_argument("host", type=str, help="The scanned Host")
    parser.add_argument("-s", "--start",type =int, help="Sets a starting point of scan-range",default=1)
    parser.add_argument("-e", "--end", type =int, help="Sets an ending point of scan-range",default=1000)
    parser.add_argument("-t","--timeout", type=float, help="Port response awaiting time", default=0.3) 
    args = parser.parse_args()
    if args.end not in range(1,65536) or args.start not in range(1,65536) :
        parser.error("Wrong initialization of scan-range. Values MUST be in RANGE(1, 65536)")
    elif args.end < args.start:
        parser.error(f"Wrong initialization of scan-range. start ({args.start}) must be <= end ({args.end})")

    return args 


def check_port(host,port, timeout) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0



def scan_range(host, start, end, timeout) -> list[int]:
    open_ports = []
    ports = range(start, end + 1)
    with ThreadPoolExecutor() as executor:
            ports_scan = executor.map(check_port,[host]*len(ports), ports, [timeout]*len(ports))
    
    for i, is_open in enumerate(ports_scan, start=start):
            if is_open == True:
                open_ports.append(i)
    return open_ports 

#========Programm=========
def main():
    print("")    
    s_time = time.perf_counter()

    args = parse_args()
    host = args.host
    start = args.start
    end = args.end
    timeout = args.timeout
    
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit(f"The hostname: \"{host}\" is invalid. Please correct it and try again!")    

    ports = scan_range(host, start, end, timeout)

    if not ports:
        print(f"No OPEN ports on host: {host}")
    else:
         for port in ports:
              print(f"{host}::{port} -> OPEN")

    print("--------------------------------------")    
    print(f"(Multithread)Scan time in port-range {args.start} to {args.end}: {time.perf_counter()-s_time:.3f}s") 
    print("")    



if __name__ == "__main__":
    main()



