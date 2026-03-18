# TOOLS.md - Studio Equipment & Config

这里记录本地生产环境的配置参数、路径和工具链细节。

## 🎬 视频生产环境

### FFmpeg 配置
- **Path**: 系统默认 `/usr/local/bin/ffmpeg` 或 Agent 路径。
- **Version**: 7.1.1
- **Standard Flags**:
  - 兼容性: `-c:v libx264 -pix_fmt yuv420p` (确保 QuickTime/Windows 能播)
  - 字幕烧录: `-vf subtitles=subtitle.srt:force_style='Fontname=Arial,FontSize=24'`

### 工作区目录 (Workspace)
- **Downloads**: `/Users/hidream/Desktop/zhy/projects/personal/harrybot-memory/downloads`
  - *用途*: 存放从 API 下载的原始图片和视频片段。
- **Output**: `/Users/hidream/Desktop/zhy/projects/personal/harrybot-memory/output`
  - *用途*: 存放最终合成的成品视频。
- **Temp**: `/tmp/viva_gen`
  - *用途*: 存放 concat list、SRT 字幕文件等临时数据。

## 🧠 模型参数笔记 (Prompt Engineering)

### Seedream (文生图)
- **正向词**: `8k resolution, masterpiece, best quality, cinematic lighting, ray tracing`
- **负向词**: `low quality, bad anatomy, blurry, watermark, text, signature`
- **分辨率**: 推荐 `2048*2048` (方形) 或 `1920*1080` (宽屏)。

### Kling (图生视频)
- **Duration**: 通常为 5s。
- **Prompt**: 重点描述动作 (Motion)。例如 `slow motion, camera pan right, walking forward`。
- **Image权重**: 保持高保真度。

## 📧 交付渠道
- **SMTP Server**: `smtp.qq.com` (SSL: 465)
- **Sender**: `your_email@qq.com`
- **Target**: `user@example.com`

---
*Updated for Video Production Workflow*
