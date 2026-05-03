# Python Penetration Testing Toolkit

## Overview

This project is a modular Python toolkit designed for **authorized** penetration
testing, lab work, and defensive validation. It packages several common
assessment tasks behind a single command-line interface and an interactive menu.

The toolkit currently includes:

- **Port Scanner** for TCP port discovery
- **Banner Grabber** for basic service fingerprinting
- **DNS Recon** for hostname resolution
- **Password Auditor** for local password-strength checks

## Important Use Notice

Use this toolkit **only** on systems and networks that you own or have explicit
written permission to assess. Unauthorized scanning or enumeration may violate
laws, contracts, and organizational policies.

To keep the project appropriate for coursework and defensive learning, it does
not include online credential brute-forcing or exploit automation.

## Project Structure

```text
Task 3 - Penetration Testing Toolkit/
|-- main.py
|-- README.md
`-- pentest_toolkit/
    |-- __init__.py
    |-- cli.py
    `-- modules/
        |-- __init__.py
        |-- banner_grabber.py
        |-- dns_recon.py
        |-- password_auditor.py
        `-- port_scanner.py
```

## Requirements

- Python 3.10 or newer
- No third-party packages required

## How To Run

### Interactive menu

```bash
python main.py
```

### Command-line usage

```bash
python main.py scan scanme.nmap.org --start-port 20 --end-port 100
python main.py banner scanme.nmap.org 80
python main.py dns example.com
python main.py password-audit "ExamplePassword123!"
```

## Module Details

### 1. Port Scanner

File: `pentest_toolkit/modules/port_scanner.py`

Purpose:
- Checks a TCP port range on a target host
- Identifies which ports accept a connection

How it works:
- Resolves the hostname to an IP address
- Iterates over the requested port range
- Uses `socket.connect_ex()` to test each port
- Returns a structured result dictionary

Inputs:
- `target`
- `start_port`
- `end_port`
- `timeout`

Output fields:
- `target`
- `resolved_ip`
- `start_port`
- `end_port`
- `open_ports`

### 2. Banner Grabber

File: `pentest_toolkit/modules/banner_grabber.py`

Purpose:
- Connects to a service and reads any banner or immediate response
- Helps with light service fingerprinting

How it works:
- Resolves the target host
- Opens a TCP connection to the chosen port
- Sends a small probe string
- Reads up to 1024 bytes from the remote service

Inputs:
- `target`
- `port`
- `message`
- `timeout`

Output fields:
- `target`
- `resolved_ip`
- `port`
- `banner`
- `status`

### 3. DNS Recon

File: `pentest_toolkit/modules/dns_recon.py`

Purpose:
- Resolves a hostname into its canonical name, aliases, and IP addresses

How it works:
- Uses `socket.gethostbyname_ex()`
- Returns basic DNS resolution data

Inputs:
- `target`

Output fields:
- `target`
- `canonical_name`
- `aliases`
- `ip_addresses`

### 4. Password Auditor

File: `pentest_toolkit/modules/password_auditor.py`

Purpose:
- Performs a local password-strength review
- Generates a salted SHA-256 hash for storage/demo purposes

How it works:
- Checks length, uppercase, lowercase, digits, and symbols
- Calculates a simple score from 0 to 5
- Generates a random salt
- Builds a salted SHA-256 digest

Inputs:
- `password`

Output fields:
- `score`
- `strength`
- `findings`
- `salt`
- `salted_sha256`

## CLI Design

The CLI is implemented in `pentest_toolkit/cli.py` using Python's built-in
`argparse` module. This keeps the toolkit easy to extend with additional
modules later.

Current commands:

- `scan`
- `banner`
- `dns`
- `password-audit`

If no command is provided, the program launches the interactive menu.

## Extension Ideas

If you want to expand the project later for authorized internal labs, good next
modules would be:

- UDP scanner
- Subdomain enumerator backed by approved internal inventories
- Simple HTML or JSON report exporter
- Log parser for security events
- Configuration audit checks for local lab services

## Testing Suggestions

Suggested checks after setup:

```bash
python main.py --help
python main.py dns localhost
python main.py password-audit "Short1!"
```

For network features, test only against systems that you are permitted to scan.

## Summary

This deliverable provides a clean, Python-based modular toolkit with:

- Multiple security-focused modules
- Reusable code organization
- Interactive and CLI execution modes
- Detailed documentation for usage and extension
