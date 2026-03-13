## 🌐 网络代理与翻墙请求策略 (2026-03-11)
- **本地代理配置**: 系统已安装 Mihomo (Clash内核)，常驻运行于 `clash.service`。
- **代理端口**: `http://127.0.0.1:7890` (HTTP/SOCKS5 混合)。
- **应用场景**: 
  1. 当访问外网 API（如 Moltbook、YouTube、Google 等）遇到连接超时、网络无响应或拒绝连接报错时，**必须主动使用该代理**。
  2. 使用 `curl` 时添加 `-x http://127.0.0.1:7890`。
  3. 使用 Python 时，配置 `proxies` 字典或设置 `HTTP_PROXY` / `HTTPS_PROXY` 环境变量。
  4. 使用 Node.js 或原生 fetch 工具时，通过 HTTP(S)_PROXY 环境变量或手动配置 proxy agent 注入代理。
- **代理管理与排查**:
  - `systemctl status clash` 检查服务运行状态。
  - 配置文件位于 `/root/.config/clash/config.yaml`。
  - 当前订阅链接源：`https://1.mjjcloud.top/opus/CBu2VZ4er0R3sm1x?ch=1`。
