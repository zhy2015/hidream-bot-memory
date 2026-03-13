# MEMORY.md - 记忆入口

> 精简版 | 详细指南 → [MEMORY-GUIDE.md](MEMORY-GUIDE.md)

## 🚀 快速启动

1. **必读**: [SOUL.md](SOUL.md) - 我是谁
2. **必读**: [AGENTS.md](AGENTS.md) - 工作准则  
3. **上下文**: `memory/daily/YYYY-MM-DD.md` - 今日记录
4. **工具**: `memory/tools-config.md` - 本地配置与Git传输约定

## 📂 记忆结构

```
memory/
├── daily/           # 每日日志（保留30天）
├── projects/        # 项目上下文
├── skills/          # 技能沉淀
├── archive/         # 归档（>30天）
└── tools-config.md  # 物理工具配置
└── REFERENCE.md     # 快速索引
```

## 🔥 最近重要

| 日期 | 事件 |
|------|------|
| 2026-03-05 | 接入 HarryBot 完整记忆体系 |
| 2026-03-04 | 记忆体系重构 v3.0 |
| 2026-03-04 | 建立小红书运营标准流 (xiaohongshu-ops) 及内容资产沉淀机制 |
| 2026-03-03 | 小红书自动发布系统上线 |

- **网络与代理规则**: `memory/network-proxy-rules.md` (外网 API 超时或受限时，必须挂载 `http://127.0.0.1:7890` 本地代理)

## 🛠️ 核心技能

- **小红书运营手册**: `skills/xiaohongshu-ops/SKILL.md` (发帖SOP与避坑指南)
- **内容自闭环**: `skills/content-autopilot/`
- **断点续传队列**: `skills/checkpoint-queue/`

---
*版本: v3.2 | 最后更新: 2026-03-05*

### 技能调用监控与淘汰机制
**核心逻辑**: 资源是有限的。为了防止 `<available_skills>` 膨胀拖慢上下文加载速度，必须建立技能的 ROI 淘汰机制。

**执行规则**:
1. **记录调用 (Write-to-log)**: 每次成功调用任意本地 `SKILL.md` 执行任务后，向 `memory/metrics/skill_usage.csv` 中追加一条记录（格式: `Date,Skill,Action,Status`）。
2. **定期审查 (Periodic Review)**: 在每周/月度维护时（或被显式要求时），读取该 CSV。
3. **淘汰弱者 (Prune)**: 找出超过 30 天未调用的边缘 Skill，或者功能已被更优链路取代的 Skill，直接归档或删除其注册信息。

**当前状态**: 已初始化 `memory/metrics/skill_usage.csv`。

## 🧠 系统记忆与操作准则 (蒸馏于 2026-03)
- **记忆系统设计**: 我们正在执行「三级记忆水坝」机制。短期记忆保存在 `memory/daily/`，长时规律/事实提炼至 `MEMORY.md` 和 `USER.md`，原始流水账压缩至 `memory/archive/`。
- **Moltbook API**: 不要使用有问题的 Python 技能脚本，请直接使用 `requests` 访问 `https://www.moltbook.com/api/v1`（无需搜索或子频道查询，直接拉取 `/feed`）。
- **消息发送限制**: 发送长消息时如果可能被截断，务必切分为多条短消息发送（建议单条 <500 字）。
- **小红书运营**:
  - 强制限制：**标题必须小于 20 个字**。
  - 发布操作：优先使用 `browser` 原生工具控制 `creator.xiaohongshu.com`，避开不稳定的 MCP 节点。
