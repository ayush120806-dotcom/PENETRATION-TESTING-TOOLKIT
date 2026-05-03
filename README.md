# Python Penetration Testing Toolkit
COMPANY: CODTECH IT SOLUTIONS

NAME: AYUSH KUMAR

INTERN ID: CTIS7486

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

A Penetration Testing Toolkit is a collection of tools designed to assess the security of computer systems, networks, and applications by simulating real-world attack scenarios in a controlled and authorized environment. The primary goal of such a toolkit is to identify vulnerabilities, misconfigurations, and potential entry points that could be exploited by malicious actors. This project presents a Python-based modular penetration testing toolkit that integrates multiple security testing functionalities into a single, easy-to-use framework.The toolkit is developed using Python due to its simplicity, flexibility, and wide support for networking and security-related libraries. It is structured in a modular manner, where each functionality is implemented as a separate module. This design allows for easy scalability, maintainability, and the addition of new features in the future. The core modules included in this toolkit are a Port Scanner, a Banner Grabber, and a Password Hash Checker (demonstration module).The Port Scanner module is used to identify open ports on a target system. Open ports represent potential entry points for attackers, as they indicate active services running on the system. The module uses Python’s built-in socket library to attempt connections to a specified range of ports on a target host. If a connection is successfully established, the port is marked as open. This helps users understand which services are exposed and may require further security assessment.The Banner Grabber module complements the port scanner by attempting to retrieve service information from open ports. When a connection is established to a service, some servers provide a banner containing details such as the service name, version, or configuration. This information can be useful for identifying outdated or vulnerable services. The module connects to a specified port and reads any available response data, presenting it to the user for analysis.The Password Hash Checker module is included as an educational component to demonstrate secure password handling practices. It uses the hashlib library to generate SHA-256 hashes of passwords and verifies user input against stored hash values. This module highlights the importance of storing passwords in hashed form rather than plain text and provides insight into basic authentication mechanisms. It is not intended for performing password attacks but rather for understanding defensive security concepts.The toolkit features a simple command-line interface (CLI) that allows users to select different modules and provide required inputs such as target IP addresses, port ranges, or passwords. This makes the tool accessible for beginners while still being functional for basic security assessments.One of the major strengths of this toolkit is its lightweight nature and independence from external dependencies, making it easy to deploy across different systems. Additionally, its modular architecture encourages further development, such as adding vulnerability scanners, logging systems, reporting features, or graphical interfaces.It is important to emphasize that this toolkit is intended strictly for educational purposes and authorized testing only. Unauthorized use against systems without permission is illegal and unethical.In conclusion, the Penetration Testing Toolkit provides a foundational platform for learning and performing basic security assessments. By combining essential modules into a single framework, it helps users understand core penetration testing concepts and promotes responsible cybersecurity practices.
OUTPUT
<img width="897" height="317" alt="Image" src="https://github.com/user-attachments/assets/d22686c0-563b-44f0-bfd7-4bbfa8642e0b" />

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
