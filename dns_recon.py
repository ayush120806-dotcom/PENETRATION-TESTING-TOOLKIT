"""DNS lookup helpers for lightweight recon on authorized targets."""

from __future__ import annotations

import socket


def resolve_target(target: str) -> dict:
    canonical_name, aliases, ip_addresses = socket.gethostbyname_ex(target)
    return {
        "target": target,
        "canonical_name": canonical_name,
        "aliases": aliases,
        "ip_addresses": ip_addresses,
    }
