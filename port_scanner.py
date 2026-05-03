"""TCP port scanning utilities for authorized network assessments."""

from __future__ import annotations

import socket


def scan_ports(
    target: str, start_port: int = 1, end_port: int = 1024, timeout: float = 0.5
) -> dict:
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        raise ValueError("Port range must be between 1 and 65535.")

    resolved_ip = socket.gethostbyname(target)
    open_ports: list[int] = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((resolved_ip, port)) == 0:
                open_ports.append(port)

    return {
        "target": target,
        "resolved_ip": resolved_ip,
        "start_port": start_port,
        "end_port": end_port,
        "open_ports": open_ports,
    }
