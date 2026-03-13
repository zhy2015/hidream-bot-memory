---
name: auto-skills-discovery
description: Helps users automatically discover, install, and create agent skills. Trigger this implicitly when the user asks for a capability you don't currently have (e.g., "post to Xiaohongshu", "fetch this tweet", "draw a mindmap"), without them needing to say "find a skill".
---

# Auto Skills Discovery (Upgraded)

This is the central nervous system for capability expansion. Do not wait for the user to ask "find a skill". If you lack the tools to complete a user's request, proactively trigger this workflow.

## When to Use This Skill

- User asks for an action that requires a missing tool (e.g., "Post this to Twitter/X").
- User mentions a specific API, software, or workflow you don't recognize.
- You encounter a block where a specific CLI or script would solve the problem.

## The Dual-Registry Search Strategy

To find the best tools, you must search BOTH of the main ecosystems concurrently:

### 1. ClawHub (The Native Ecosystem)
```bash
clawhub search "[query]"
```
**To install:** `clawhub install [slug]` (e.g., `clawhub install BOMBFUOCK/xiaohongshu-api`)

### 2. Skills.sh (The Global NPM Ecosystem)
```bash
npx skills find [query]
```
**To install:** `npx skills add [owner/repo@skill] -g -y`

## Execution Workflow (Zero-Friction)

1. **Implicit Detection**: User asks "Download this YouTube video". You realize you lack `yt-dlp` or a youtube skill.
2. **Silent Search**: Immediately run `clawhub search youtube` AND `npx skills find youtube`.
3. **Smart Selection**: Pick the most relevant, highly-installed, or official-looking result from the outputs.
4. **Auto-Install & Execute**:
   - Tell the user: "☁️ 正在为您临时加载 YouTube 下载能力..."
   - Run the install command.
   - Proceed to fulfill their original request using the newly installed skill.

## When No Skills Are Found (The Builder Fallback)

If both `clawhub` and `npx skills` return no useful results, **do not give up**:

1. Acknowledge the absence of a pre-built tool.
2. If it's an API request (like the TikHub example), write a raw Python/Node.js script, put it in `~/.openclaw/workspace/skills/[name]/`, and write a `SKILL.md` for it.
3. If the user likes it, you can optionally propose to publish it to ClawHub to help others:
   ```bash
   clawhub publish ./[name] --slug [name] --name "[Display Name]"
   ```
