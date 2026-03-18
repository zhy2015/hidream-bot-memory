from __future__ import annotations

import json
import os
from pathlib import Path

# Unified config directory (XDG Base Directory compliant)
CONFIG_DIR = Path.home() / ".config" / "openclaw"
CONFIG_FILE = CONFIG_DIR / "hidream_config.json"

# Project-specific config path (Added by user request)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
PROJECT_CONFIG_FILE = PROJECT_ROOT / "memory/config/hidream_config.json"


def _ensure_config_dir() -> None:
    """Ensure the config directory exists."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def get_token() -> str | None:
    """
    Get authorization token from environment variables or config file.
    Priority:
    1. HIDREAM_AUTHORIZATION env var
    2. OPENCLAW_AUTHORIZATION env var (legacy)
    3. memory/config/hidream_config.json (Project-specific)
    4. ~/.config/openclaw/hidream_config.json (User global)
    """
    # 1. Check Env
    token = os.getenv("HIDREAM_AUTHORIZATION") or os.getenv("OPENCLAW_AUTHORIZATION")
    if token:
        return token

    # 2. Check Project Config File
    if PROJECT_CONFIG_FILE.exists():
        try:
            with open(PROJECT_CONFIG_FILE, "r") as f:
                data = json.load(f)
                # Support both "authorization" and "api_key" keys
                return data.get("authorization") or data.get("api_key")
        except Exception:
            pass

    # 3. Check Global Config File
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("authorization")
        except Exception:
            pass
    return None


def set_token(token: str) -> None:
    """Save authorization token to unified config file."""
    _ensure_config_dir()
    data = {}
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
        except Exception:
            pass

    data["authorization"] = token
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=2)
