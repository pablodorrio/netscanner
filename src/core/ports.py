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
    #service = None

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
