import socket

from scapy.all import *


def get_ip() -> str:
    try:
        ip = input("Enter IPv4: ")
        socket.inet_aton(ip)
    except socket.error:
        print("Invalid IPv4")
        exit()

    return ip


def icmp_trace(ip: str) -> None:
    p = sr1(IP(dst=ip)/ICMP()/Raw(load="Hello World"), timeout=1, verbose=0)
    if not p:
        print("Host is down")
        exit()

    print("Host is up")
    which_system(ttl=p.ttl)


def which_system(ttl: str) -> None:
    if ttl <= 64:
        print("Linux/Unix")
    elif ttl <= 128:
        print("Windows")
    else:
        print("Unknown")


def scan_ports(ip: str) -> bool:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    established = False

    for port in range(1, 65535):
        try:
            client_socket.connect((ip, port))
            print(f"{port}/tcp OPEN")
            established = True
        except:
            pass

    return established


if __name__ == "__main__":
    ip = get_ip()
    icmp_trace(ip)
    established = scan_ports(ip)

    if not established:
        print(f"{ip} is not listening on any port")
