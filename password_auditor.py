"""Local password auditing helpers for defensive use."""

from __future__ import annotations

import hashlib
import secrets
import string


def audit_password(password: str) -> dict:
    findings: list[str] = []
    score = 0

    if len(password) >= 12:
        score += 1
    else:
        findings.append("Use at least 12 characters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        findings.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        findings.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        findings.append("Add digits.")

    punctuation = set(string.punctuation)
    if any(char in punctuation for char in password):
        score += 1
    else:
        findings.append("Add special characters.")

    if not findings:
        findings.append("Password meets the basic local strength checks.")

    salt = secrets.token_hex(8)
    salted_hash = hashlib.sha256(f"{salt}{password}".encode("utf-8")).hexdigest()

    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong",
    }

    return {
        "score": score,
        "strength": labels[score],
        "findings": findings,
        "salt": salt,
        "salted_sha256": salted_hash,
    }
