# MEMORY.md — 视觉工坊核心记忆库

### 🎥 视频生成最佳实践 (Standard Operating Procedures)

#### 1. 提示词工程 (Prompt Engineering)
- **结构**: `[主体描述] + [环境/背景] + [动作/运镜] + [风格/画质]`
- **示例**: "A cyberpunk samurai standing in neon rain, holding a glowing katana, dynamic camera angle, volumetric lighting, 8k, unreal engine 5 render."
- **Kling 特性**: 在图生视频时，Prompt 必须着重描述**变化**。如果 Prompt 是静态的（如 "a beautiful woman"），生成的视频可能也是静止的。必须加上 "turning head", "smiling", "wind blowing hair" 等动态词。

#### 2. 视频拼接规范 (FFmpeg Concat)
- **分辨率对齐**: 所有素材必须统一分辨率（如 1080p）再拼接。不同分辨率会导致 FFmpeg 报错或画面撕裂。
- **编码统一**: 拼接前最好将所有片段转码为统一的中间格式（如 ProRes 或高码率 H.264），防止时间戳跳变。
- **音频处理**: 纯画面生成通常无声。拼接时考虑是否需要添加背景音乐（BGM）或静音轨道。

#### 3. 字幕烧录 (Subtitling)
- **SRT 格式**: 必须严格遵守 `Seq -> Time -> Content -> Blank` 格式。
- **防遮挡**: 字幕位置通常设为 `Alignment=2` (底部居中)，`MarginV=20`。避免遮挡画面核心主体。

### 🛡️ 资源管理与熔断机制
- **存储空间**: 视频生成极其占用空间。
  - **规则**: 每次 Heartbeat 检查 `downloads/` 文件夹。
  - **清理**: 删除超过 24 小时的原始素材（raw clips）。只保留最终成品（final output）。
- **API 成本**: 视频生成 API 通常昂贵。
  - **熔断**: 如果连续 3 次生成失败，停止任务并报错，不要死循环重试。

### 🧩 技能链路整合 (Skill Chain)
- **Standard Flow**:
  1. `summarize` (User Request -> English Prompt)
  2. `viva-gen-workflow` (Prompt -> Images -> Video Clips)
  3. `ffmpeg-video-editor` (Clips -> Concat -> Add Subtitles -> Final.mp4)
  4. `qqmail` (Final.mp4 -> Email Delivery)

### 🚫 历史教训 (Do Not Repeat)
- **不要** 试图用 ASCII 字符画图，用户需要的是真图。
- **不要** 在没有下载完所有片段前就开始拼接，会导致黑屏。
- **不要** 把几百兆的视频直接丢进 Markdown 渲染，会卡死客户端。必须用邮件。

---
*Last Updated: Video Production Era*
