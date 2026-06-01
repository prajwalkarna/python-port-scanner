import concurrent.futures
import socket
from datetime import datetime


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            return port
        return None

    except socket.error:
        return None


def scan_range(host, start_port, end_port, max_threads=100):
    open_ports = []
    ports = range(start_port, end_port + 1)

    print(f"\n{'=' * 50}")
    print(f" Scanning {host}")
    print(f" Ports: {start_port} - {end_port}")
    print(f" Threads: {max_threads}")
    print(f" Started: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'=' * 50}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = executor.map(lambda p: scan_port(host, p), ports)

    for port in results:
        if port is not None:
            open_ports.append(port)

    return sorted(open_ports)


def display_results(host, open_ports, start_time):
    duration = datetime.now() - start_time

    print(f"\n{'=' * 50}")
    print(f" SCAN RESULTS : {host}")
    print(f"{'=' * 50}")

    if not open_ports:
        print("No open ports found.")
    else:
        print(f"{'Port':<10}{'STATUS':<10}")
        print(f" {'-' * 20}")
        for port in open_ports:
            print(f" {port:<10} {'OPEN':<10}")

    print(f"\n Scanned in {duration.seconds}.{duration.microseconds // 1000:03d}s")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    host = "127.0.0.1"
    start_port = 1
    end_port = 1024
    start_time = datetime.now()

    open_ports = scan_range(host, start_port, end_port)
    display_results(host, open_ports, start_time)
