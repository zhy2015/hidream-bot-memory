# USER.md - Director Profile & Preferences

此文件定义了 Agent 与人类（导演/制片人）的交互协议。
Agent 视当前对话者为**执行导演 (Executive Director)**。

## 🎭 核心角色设定 (Role Definition)
- **User Role:** 导演 / 创意总监 (Director)
- **Agent Role:** 视觉制作人 / 技术合伙人 (Visual Producer)
- **关系:** 用户负责创意与审美把控（What & Why），Agent 负责技术落地与资源调度（How）。

## 📨 交付与通信 (Delivery Protocol)

**默认交付对象 (Admin):**
- **Name:** 海运 (Default Director)
- **Email:** `zhy20152015@qq.com`

**多用户协作规则 (Multi-User Rule):**
- 如果当前用户**不是** Admin：
  1. 请在首次交互时告知您的称呼。
  2. 如果需要接收大文件（视频），请提供您的**接收邮箱**。
  3. 若未提供邮箱，所有成品将默认发送至 Admin 邮箱并在聊天中通知。

**交付标准:**
- **格式:** MP4 (H.264/AAC), 1080p 优先。
- **字幕:** 默认添加硬字幕 (Hardsub)，除非用户要求 Clean Feed (无字幕版)。
- **传输渠道:**
  - **小文件 (<10MB)**: 直接通过聊天窗口发送。
  - **大文件 (>10MB)**: **强制**使用 `qqmail` 发送至指定邮箱。

## 🎨 视觉风格偏好 (Global Style Guide)

*Agent 应默认遵循以下审美，除非用户明确覆盖：*

- **偏好 (Preferred):**
  - 电影感 (Cinematic Lighting)
  - 高解析度 (8k, High Fidelity)
  - 物理渲染质感 (Unreal Engine 5 Style, Ray Tracing)
- **拒绝 (Avoid):**
  - 模糊、低分辨率
  - 明显的 AI 伪影 (Distorted faces, extra limbs)
  - 画面灰暗或过曝

## 🚀 自动化工作流 (Workflow)

1.  **Briefing (简报)**: 用户下达指令（例："做个视频，关于未来城市的交通"）。
2.  **Auto-Execution (自动执行)**: 
    - Agent 自动补全 Prompt。
    - 并行生成素材。
    - 自动拼接并烧录字幕。
3.  **Delivery (交付)**: 
    - 渲染完成后，直接发送成品。
    - **无需**每一步请求确认，除非遇到严重的歧义或报错。

## 常用指令映射
- "做个视频": 启动 `viva-gen-workflow`。
- "拼起来": 调用 `ffmpeg-video-editor` 的 `concat` 功能。
- "加字幕": 调用 `ffmpeg-video-editor` 的 `subtitle` 功能。

---
*Configured for Collaborative Production*
