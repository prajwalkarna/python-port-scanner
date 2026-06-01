# Python Port Scanner

A multi-thread TCP port scanner built from scratch using Python sockets.
Inspired by tools like nmap, this project demonstrates core networking concepts including TCP hankshakes, socket programming, and concurrent scanning.

## Demo

*(coming soon - will be added after completion)*

## How it Works

A port scanner works by attempting a TCP connection to each port on a target host. If the connection succeeds (TCP handshake completes), the port is **open**.
If the connection is refused or times out, the port is **closed** or **filtered**.

This tool uses Python's  `socket` library to perform these connection attempts, and `concurrent.futures` to scan multiple ports simultaneously making it fast enough to scan 1000 ports in seconds.

## Installation

```bash
git clone https://github.com/prajwalkarna/python-port-scanner.git
cd python-port-scanner
python sacnner.py
```

## Usage

```bash
# Scan common ports on a host
python scanner.py -t 192.168.1.1

# Scan a custom port range
python scanner.py -t 192.168.1.1 -p 1-1024

# Scan with more threads (faster)
python scanner.py -t 192.168.1.1 -p 1-12345 --threads 200
```

## What I Learned

- How TCP three-way handshakes work in practice
- Python socket programming
- Multi-threading with `concurrent.future`
- CLI argument parsing with `argparse`
- Real network behavior vs Packet Tracer simulations

## Technologies

- Python 3
- `socket` : core TCP connections
- `concurrent.futures` : multi-threaded scanning
- `argparse` : command line interface
- Linux (CachyOS)

## Disclaimer

This tool is for educational purposes and authorized testing only.
Only can hosts you own or have explicit permission to scan.
