# 工具与本地环境配置

## Git 仓库配置

### 1. 文件传输（与用户交流）
**仓库**: `git@github.com:zhy2015/transfer.git`
**用途**: 用户和我之间传输大文件、文章内容
**分支**: master
**使用方式**:
```bash
# 用户发送文件给我
git clone git@github.com:zhy2015/transfer.git
cp 文件.txt transfer/YYYYMMDD/
git add . && git commit -m "发送文件" && git push

# 我读取文件
cat transfer/YYYYMMDD/文件.txt

# 我发送文件给用户（如果需要）
cp 回复.txt transfer/YYYYMMDD/
git add . && git commit -m "回复文件" && git push
```

## 其他工具

### 技能发现
- skills.sh - Agent Skills 注册中心
- Antigravity-Awesome-Skills - 社区技能库

### 开发工具
- Openclaw 2026.2.23 - 运行时环境
- GitHub - 代码/记忆托管
