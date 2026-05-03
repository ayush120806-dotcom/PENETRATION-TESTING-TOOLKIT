"""Banner grabbing helpers for identifying exposed services."""

from __future__ import annotations

import socket


def grab_banner(
    target: str,
    port: int,
    message: str = "HEAD / HTTP/1.0\r\n\r\n",
    timeout: float = 2.0,
) -> dict:
    resolved_ip = socket.gethostbyname(target)

    try:
        with socket.create_connection((resolved_ip, port), timeout=timeout) as sock:
            if message:
                sock.sendall(message.encode("utf-8", errors="ignore"))
            banner = sock.recv(1024).decode("utf-8", errors="replace").strip()
            return {
                "target": target,
                "resolved_ip": resolved_ip,
                "port": port,
                "banner": banner,
                "status": "success",
            }
    except OSError as exc:
        return {
            "target": target,
            "resolved_ip": resolved_ip,
            "port": port,
            "banner": "",
            "status": str(exc),
        }
