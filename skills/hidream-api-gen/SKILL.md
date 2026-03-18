# HiDream API Gen Skills

A comprehensive collection of AI generation skills for the OpenClaw platform (vivago.ai).

## Installation

This skill has been installed via `git clone`.
Dependencies: `requests` (installed).

## Configuration

**Step 1: Get Token**
Go to [vivago.ai/platform/token](https://vivago.ai/platform/token) to get your API Token.

**Step 2: Configure**
Run the interactive configuration script:
```bash
python3 skills/hidream-api-gen/scripts/configure.py
```
Or set the environment variable:
```bash
export HIDREAM_AUTHORIZATION="your-sk-token"
```

## Usage

### Image Generation (Seedream)
```bash
python3 skills/hidream-api-gen/scripts/seedream.py --version "M2" --prompt "A cyberpunk city" --resolution "2048*2048"
```

### Video Generation (Kling)
```bash
python3 skills/hidream-api-gen/scripts/kling.py --version "Q2.5T-pro" --prompt "A cat flying in the sky" --duration 5
```

## Notes
- Ensure `HIDREAM_AUTHORIZATION` is set before running any generation script.
- Output files will be saved in the current directory or specified output path.
