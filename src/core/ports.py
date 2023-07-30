"""Open host ports.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import socket

open_ports = []


def scan_ports(ip: str) -> bool:
    """Scan open ports in a host.

    Args:
        ip (str): Host IP.

    Returns:
        bool: True if there are open ports, False otherwise.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    established = False

    for port in range(1, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.settimeout(0.5)
                client_socket.connect((ip, port))

                if not established:
                    print("PORT\t  STATE\t SERVICE")
                    established = True

                open_ports.append(port)

                try:
                    service = socket.getservbyport(port)
                    print(f"{port}/tcp".ljust(9), "open\t", service)
                except:
                    print(f"{port}/tcp".ljust(9), "open\t", "unknown")
            except:
                pass

    return established


def check_http_https(ip: str) -> None:
    """Check if the host is listening on ports 80 and 443.

    Args:
        ip (str): Host IP.
    """
    if not 80 in open_ports or not 443 in open_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                if 80 not in open_ports:
                    connect_to_port(ip, 80)
                if 443 not in open_ports:
                    connect_to_port(ip, 443)
            except:
                pass


def connect_to_port(ip: str, port: int) -> None:
    """Connect to a port and if it is open, add it to the list of open ports.

    Args:
        ip (str): Host IP.
        port (int): Port number.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.settimeout(0.5)
            client_socket.connect((ip, port))
            open_ports.append(port)
        except:
            pass
