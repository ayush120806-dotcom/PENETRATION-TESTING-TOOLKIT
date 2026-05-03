"""Command-line interface for the penetration testing toolkit."""

from __future__ import annotations

import argparse
import sys
from typing import Iterable, Sequence

from pentest_toolkit.modules.banner_grabber import grab_banner
from pentest_toolkit.modules.dns_recon import resolve_target
from pentest_toolkit.modules.password_auditor import audit_password
from pentest_toolkit.modules.port_scanner import scan_ports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pentest-toolkit",
        description=(
            "A modular Python toolkit for authorized penetration testing "
            "and defensive security validation."
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser(
        "scan", help="Scan a TCP port range on a target host."
    )
    scan_parser.add_argument("target", help="Hostname or IP address to scan.")
    scan_parser.add_argument(
        "--start-port", type=int, default=1, help="First TCP port in the range."
    )
    scan_parser.add_argument(
        "--end-port", type=int, default=1024, help="Last TCP port in the range."
    )
    scan_parser.add_argument(
        "--timeout",
        type=float,
        default=0.5,
        help="Socket timeout in seconds per port.",
    )

    banner_parser = subparsers.add_parser(
        "banner", help="Retrieve a banner from a TCP service."
    )
    banner_parser.add_argument("target", help="Hostname or IP address.")
    banner_parser.add_argument("port", type=int, help="TCP port to connect to.")
    banner_parser.add_argument(
        "--message",
        default="HEAD / HTTP/1.0\r\n\r\n",
        help="Probe payload sent after connection.",
    )
    banner_parser.add_argument(
        "--timeout", type=float, default=2.0, help="Socket timeout in seconds."
    )

    dns_parser = subparsers.add_parser(
        "dns", help="Resolve DNS information for a host."
    )
    dns_parser.add_argument("target", help="Hostname to resolve.")

    password_parser = subparsers.add_parser(
        "password-audit",
        help="Estimate password strength and generate a salted SHA-256 hash.",
    )
    password_parser.add_argument("password", help="Password to audit locally.")

    return parser


def interactive_menu() -> int:
    while True:
        print("\n=== Python Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Banner Grabber")
        print("3. DNS Recon")
        print("4. Password Auditor")
        print("5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            target = input("Enter target IP/domain: ").strip()
            start_port = int(input("Start port: ").strip())
            end_port = int(input("End port: ").strip())
            scan_result = scan_ports(target, start_port, end_port)
            _print_scan_result(scan_result)
        elif choice == "2":
            target = input("Enter target IP/domain: ").strip()
            port = int(input("Enter port: ").strip())
            banner_result = grab_banner(target, port)
            _print_banner_result(banner_result)
        elif choice == "3":
            target = input("Enter target hostname: ").strip()
            dns_result = resolve_target(target)
            _print_dns_result(dns_result)
        elif choice == "4":
            password = input("Enter password to audit: ")
            audit_result = audit_password(password)
            _print_password_audit(audit_result)
        elif choice == "5":
            print("Exiting toolkit.")
            return 0
        else:
            print("Invalid choice.")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command is None:
        return interactive_menu()

    if args.command == "scan":
        result = scan_ports(
            args.target,
            start_port=args.start_port,
            end_port=args.end_port,
            timeout=args.timeout,
        )
        _print_scan_result(result)
        return 0

    if args.command == "banner":
        result = grab_banner(
            args.target,
            port=args.port,
            message=args.message,
            timeout=args.timeout,
        )
        _print_banner_result(result)
        return 0

    if args.command == "dns":
        result = resolve_target(args.target)
        _print_dns_result(result)
        return 0

    if args.command == "password-audit":
        result = audit_password(args.password)
        _print_password_audit(result)
        return 0

    print(f"Unknown command: {args.command}", file=sys.stderr)
    return 1


def _print_scan_result(result: dict) -> None:
    print(f"\nTarget: {result['target']} ({result['resolved_ip']})")
    print(f"Port range: {result['start_port']}-{result['end_port']}")
    if result["open_ports"]:
        print("Open ports:", ", ".join(str(port) for port in result["open_ports"]))
    else:
        print("No open ports detected in the requested range.")


def _print_banner_result(result: dict) -> None:
    print(f"\nTarget: {result['target']} ({result['resolved_ip']})")
    print(f"Port: {result['port']}")
    if result["banner"]:
        print("Banner:")
        print(result["banner"])
    else:
        print(f"No banner returned. Details: {result['status']}")


def _print_dns_result(result: dict) -> None:
    print(f"\nTarget: {result['target']}")
    print(f"Canonical name: {result['canonical_name']}")
    print("Resolved IPs:", ", ".join(result["ip_addresses"]) or "None")
    print("Aliases:", ", ".join(result["aliases"]) or "None")


def _print_password_audit(result: dict) -> None:
    print("\nLocal Password Audit")
    print(f"Score: {result['score']}/5")
    print(f"Strength: {result['strength']}")
    print("Findings:")
    for item in result["findings"]:
        print(f"- {item}")
    print(f"Salt: {result['salt']}")
    print(f"Salted SHA-256: {result['salted_sha256']}")
