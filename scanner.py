import argparse
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


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="A fast multi-threaded TCP port scanner",
        epilog="Example: python scanner.py -t 192.168.1.1 -p 1-1024",
    )

    parser.add_argument(
        "-t",
        "--target",
        required=True,
        help="Target host to scan (IP address or hostname)",
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Port range to scan, format: start-end (default: 100)",
    )

    parser.add_argument(
        "--threads",
        type=int,
        default=100,
        help="Number of threads to use (default: 100)",
    )

    return parser.parse_args()


def parse_port_range(port_string):
    try:
        parts = port_string.split("-")

        if len(parts) != 2:
            raise ValueError

        start = int(parts[0])
        end = int(parts[1])

        if not (1 <= start <= 65535) or not (1 <= end <= 65535):
            raise ValueError("Ports must be between 1 and 65535")

        if start > end:
            raise ValueError("Start port must be less than end port")

        return start, end

    except ValueError:
        print("Error: Invalid port range. Use format: 1-1024")
        exit(1)


if __name__ == "__main__":
    args = parse_arguments()

    try:
        host = socket.gethostbyname(args.target)
        if host != args.target:
            print(f"\n Resolved {args.target} → {host}")
    except socket.gaierror:
        print(f"\n Error: Could not resolve hostname '{args.target}'")
        exit(1)

    start_port, end_port = parse_port_range(args.ports)

    start_time = datetime.now()

    open_ports = scan_range(host, start_port, end_port, args.threads)

    display_results(host, open_ports, start_time)
