"""Fuzzing module.

Author:
    Pablo Dorrio Vazquez (@pablodorrio)
"""

import readline

import requests


def request_response(url: str) -> None:
    """Send a request to a URL.

    Args:
        url (str): URL to send the request.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Found directory: {url}")
    except requests.exceptions.ConnectionError:
        pass


def dir_fuzzer(ip: str, http: bool = False, https: bool = False) -> None:
    """Fuzz directories.

    Args:
        ip (str): IP address to fuzz.
        http (bool, optional): Use HTTP protocol. Defaults to False.
        https (bool, optional): Use HTTPS protocol. Defaults to False.
    """
    print("\nDIRECTORY DISCOVERY")

    if http and https:
        use_http = use_https = ""

        while use_http != "y" and use_http != "n":
            use_http = input("Use HTTP? (y/n): ").lower()

            if use_http == "f":
                http = False

        while use_https != "y" and use_https != "n":
            use_https = input("Use HTTPS? (y/n): ").lower()

            if use_https == "f":
                https = False

    readline.set_completer_delims(" \t\n;")
    readline.parse_and_bind("tab: complete")
    dictionary = input("  Enter a path to a wordlist: ")

    try:
        with open(dictionary, "r", encoding="utf-8") as wordlist:
            print("\033[1;31m" + "\n[*] Fuzzing directories..." + "\033[0m")

            for word in wordlist:
                word = word.strip()
                if http:
                    url = f"http://{ip}/{word}"
                    request_response(url)
                if https:
                    url = f"https://{ip}/{word}"
                    request_response(url)
    except FileNotFoundError:
        print("\033[1;31m" + "\n[!] " + "\033[0m" + "File not found.")
