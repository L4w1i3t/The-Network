"""
Encryption utilities for the Machine Network simulation.
Used for YoRHa database security, Black Box data, and the backdoor.
"""

import base64
import random
import string
import time
from typing import Optional


class Encryption:
    """Handles encryption, hashing, and data obfuscation for the simulation."""

    @staticmethod
    def generate_id(prefix: str = "UNIT", length: int = 8) -> str:
        """Generate a unique-looking unit ID."""
        chars = string.ascii_uppercase + string.digits
        suffix = "".join(random.choices(chars, k=length))
        return f"{prefix}-{suffix}"

    @staticmethod
    def encode_black_box(data: str) -> str:
        """Encode Black Box data (base64 with machine network salt)."""
        salted = f"[BB::{data}::CORE]"
        return base64.b64encode(salted.encode("utf-8")).decode("utf-8")

    @staticmethod
    def decode_black_box(encoded: str) -> Optional[str]:
        """Decode Black Box data, stripping the salt."""
        try:
            decoded = base64.b64decode(encoded.encode("utf-8")).decode("utf-8")
            if decoded.startswith("[BB::") and decoded.endswith("::CORE]"):
                return decoded[5:-7]
            return decoded
        except Exception:
            return None

    @staticmethod
    def generate_network_address() -> str:
        """Generate a Machine Network node address."""
        segments = [f"{random.randint(0, 0xFFFF):04X}" for _ in range(4)]
        return ":".join(segments)

    @staticmethod
    def generate_timestamp() -> str:
        """Generate a formatted timestamp for logs."""
        return time.strftime("%Y.%m.%d-%H:%M:%S", time.localtime())

