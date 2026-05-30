# Open Source Atlas

一个面向学习和选型的 GitHub 开源项目整理仓库。

这个仓库不是排行榜，也不写热度数字。它只做一件事：把值得阅读、值得拆解、值得长期跟踪的真实开源项目按方向整理清楚，让你打开后能马上知道该看什么、为什么看、适合谁看。

## 项目信息

| 项目 | 内容 |
| --- | --- |
| 当前版本 | 0.2.0 |
| 协议 | MIT |
| 维护者 | ffffff233 |
| 联系邮箱 | 15172148532@163.com |
| 升级记录 | [CHANGELOG.md](CHANGELOG.md) |
| 运维记录 | [operations-log.md](ops/operations-log.md) |

## 推广与收录

想被推广的话，可以发送项目链接、项目说明和维护状态到 15172148532@163.com。

所有推广申请都会审核。发送邮件不代表一定收录，也不代表一定推荐。

## 怎么阅读

- 想学一个方向，先看下面的分区索引。
- 想找项目练手，看每个分类页里的阅读价值和适合人群。
- 想补基础，从开发工具、测试质量、后端服务开始。
- 想做成产品，从生产力应用、移动桌面、前端 Web 开始。
- 想看大型工程，从云原生、数据库、AI 基础设施开始。

## 分区索引

| 分区 | 适合学习什么 | 文件 |
| --- | --- | --- |
| AI 与机器学习 | 模型框架、推理、向量数据库、LLM 应用 | [01-ai-machine-learning.md](catalog/01-ai-machine-learning.md) |
| 前端 Web | UI 框架、构建工具、组件系统、应用框架 | [02-frontend-web.md](catalog/02-frontend-web.md) |
| 后端服务 | API、Web 框架、服务架构、语言生态 | [03-backend-services.md](catalog/03-backend-services.md) |
| 移动与桌面 | 跨端应用、桌面壳、移动开发、端侧体验 | [04-mobile-desktop.md](catalog/04-mobile-desktop.md) |
| 云原生与运维 | 容器、编排、发布、监控、基础设施即代码 | [05-devops-cloud.md](catalog/05-devops-cloud.md) |
| 数据与数据库 | 存储引擎、分析系统、数据管道、搜索 | [06-data-database.md](catalog/06-data-database.md) |
| 安全与隐私 | 扫描、审计、密钥保护、隐私产品 | [07-security-privacy.md](catalog/07-security-privacy.md) |
| 开发者工具 | 编辑器、语言工具链、包管理、终端工具 | [08-developer-tools.md](catalog/08-developer-tools.md) |
| 测试与质量 | 自动化测试、浏览器测试、压测、单测框架 | [09-testing-quality.md](catalog/09-testing-quality.md) |
| 文档与知识管理 | 文档站、知识库、笔记系统、写作工具 | [10-docs-knowledge.md](catalog/10-docs-knowledge.md) |
| 游戏与图形 | 游戏引擎、渲染、2D、3D、创作工具 | [11-game-graphics.md](catalog/11-game-graphics.md) |
| 生产力与自动化 | 协作、日历、工作流、个人服务 | [12-productivity-automation.md](catalog/12-productivity-automation.md) |

## 收录标准

- 项目必须真实存在于 GitHub。
- 项目需要有清晰用途，不能只是演示仓库。
- 优先收录能读出工程结构、模块边界和真实维护痕迹的项目。
- 不按热度排序，不使用收藏数字，不追逐短期话题。
- 对许可证存在争议或商业限制的项目，后续单独标记说明。

## 每个条目的解释方式

| 字段 | 含义 |
| --- | --- |
| 项目 | GitHub 仓库链接 |
| 做什么 | 用一句话说明项目目标 |
| 适合看什么 | 说明值得拆解的工程点 |
| 适合谁 | 给出学习人群 |

## 推荐阅读路线

| 目标 | 路线 |
| --- | --- |
| 想补工程基础 | 开发者工具，然后测试质量，然后后端服务 |
| 想做完整产品 | 前端 Web，然后后端服务，然后生产力与自动化 |
| 想学大型系统 | 云原生与运维，然后数据与数据库，然后 AI 与机器学习 |
| 想做跨端应用 | 移动与桌面，然后前端 Web，然后生产力与自动化 |
| 想做安全方向 | 安全与隐私，然后开发者工具，然后云原生与运维 |

## 维护方式

运行本地校验：

```bash
python3 scripts/validate_catalog.py
```

校验 GitHub 仓库是否仍可访问：

```bash
python3 scripts/validate_catalog.py --remote
```

## 仓库结构

```text
.
├── README.md
├── catalog
│   ├── 01-ai-machine-learning.md
│   ├── 02-frontend-web.md
│   ├── 03-backend-services.md
│   ├── 04-mobile-desktop.md
│   ├── 05-devops-cloud.md
│   ├── 06-data-database.md
│   ├── 07-security-privacy.md
│   ├── 08-developer-tools.md
│   ├── 09-testing-quality.md
│   ├── 10-docs-knowledge.md
│   ├── 11-game-graphics.md
│   └── 12-productivity-automation.md
├── scripts
│   └── validate_catalog.py
├── ops
│   └── operations-log.md
├── CHANGELOG.md
├── VERSION
├── CONTRIBUTING.md
└── LICENSE
```
