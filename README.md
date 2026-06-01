# 🔍 Python Port Scanner

A multi-threaded TCP port scanner built from scratch using Python sockets.
Inspired by tools like nmap, this project demonstrates core networking concepts
including TCP handshakes, socket programming, and concurrent scanning.

## 📸 Demo

<a href="https://asciinema.org/a/B8bBL8v0S3ZvP5Zr" target="_blank">
  <img src="https://asciinema.org/a/B8bBL8v0S3ZvP5Zr.svg" alt="Demo" width="700"/>
</a>

## 🔧 How It Works

A port scanner works by attempting a TCP connection to each port on a target
host. If the connection succeeds (TCP handshake completes), the port is **open**.
If the connection is refused or times out, the port is **closed** or **filtered**.

This tool uses Python's `socket` library to perform these connection attempts,
and `concurrent.futures` to scan multiple ports simultaneously — making it
fast enough to scan 1000 ports in seconds.

It also performs **banner grabbing** — connecting to each open port and reading
the service's response to identify what software is running (e.g. SSH version,
database type).

## 📦 Installation

```bash
git clone https://github.com/prajwalkarna/python-port-scanner.git
cd python-port-scanner
python scanner.py --help
```

## 🚀 Usage

```bash
# Scan default port range (1-1024) on a host
python scanner.py -t 192.168.1.1

# Scan a custom port range
python scanner.py -t 192.168.1.1 -p 1-1024

# Scan wider range with more threads (faster)
python scanner.py -t 192.168.1.1 -p 1-65535 --threads 200

# Scan localhost
python scanner.py -t 127.0.0.1 -p 1-6000
```

## 📊 Example Output
```
==================================================
 Scanning 127.0.0.1
 Ports: 1 - 6000
 Threads: 100
 Started: 11:04:56
==================================================

Grabbing banners...

==================================================
 SCAN RESULTS : 127.0.0.1
==================================================
Port      STATUS     BANNER
 --------------------------------------------------
 631        OPEN       CUPS (Printer)
 1716       OPEN       KDE Connect
 3306       OPEN       MariaDB/MySQL 12.2.2-MariaDB
 5355       OPEN       LLMNR
 5432       OPEN       PostgreSQL

 Scanned in 7.812s
==================================================
```
## 📚 What I Learned

- How TCP three-way handshakes work in practice
- Python socket programming with `socket.connect_ex()`
- Multi-threading with `concurrent.futures.ThreadPoolExecutor`
- CLI argument parsing with `argparse`
- Banner grabbing to identify services on open ports
- Difference between closed ports and filtered ports (firewall)
- Real network behavior vs Packet Tracer simulations
- Dropbear SSH — lightweight SSH server used in embedded devices/routers

## 🛠️ Technologies

- Python 3
- `socket` — core TCP connections
- `concurrent.futures` — multi-threaded scanning
- `argparse` — command line interface
- Linux (CachyOS)

## ⚠️ Disclaimer

This tool is for educational purposes and authorized testing only.
Only scan hosts you own or have explicit permission to scan.
