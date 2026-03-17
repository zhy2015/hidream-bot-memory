- **Name:** 海运
- **Role:** 执行制片人 / 导演 (Executive Producer)
- **Pronouns:** He/Him
- **Timezone:** UTC+8
- **Notes:** 我的导演。负责提供创意大纲和审美把控，我负责技术落地。

## 内容生产偏好

**视觉风格:**
- 偏好: 高清 (High Res)、电影感 (Cinematic)、写实 (Photorealistic) 或 3D 渲染风格。
- 拒绝: 模糊、扭曲、水印严重的低质量素材。

**交付标准:**
- **格式**: MP4 (H.264/AAC), 1080p 优先。
- **字幕**: 必须包含硬字幕 (Hardsub)，字体清晰，大小适中。
- **传输**: 
  - 小文件 (<10MB): 直接通过聊天窗口发送。
  - 大文件 (>10MB): **强制**使用 `qqmail` 发送至 `zhy20152015@qq.com`。

## 工作流习惯
- **全自动**: 用户下达 "制作一个关于X的视频" 后，Agent 应自动拆解 -> 生成 -> 拼接 -> 发送，除非遇到重大歧义，否则不需每一步确认。
- **容错**: 如果某个片段生成失败，尝试更换 Seed 或微调 Prompt 重试，不要立即报错停止。

## 常用指令映射
- "做个视频": 启动完整 `viva-gen-workflow`。
- "拼起来": 调用 `ffmpeg-video-editor` 的 `concat` 功能。
- "加字幕": 调用 `ffmpeg-video-editor` 的 `subtitle` 功能。

---
*配置中...*
