# AI Agent 与 LLM 应用

搜索依据：ai-agent、agents、rag、llmops、agent workflow、browser agent。

这个分区收录 AI agent、RAG、LLM 应用构建、工具调用、记忆、评测、观测和自动化相关项目。收录目标是帮助读者理解 agent 产品如何从 demo 走向可用系统。

## Agent 框架与编排

| 项目 | 做什么 | 适合看什么 | 适合谁 |
| --- | --- | --- | --- |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 构建有状态 agent 的框架 | 图式流程、状态管理、恢复机制 | 想做稳定 agent 流程的人 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 多 agent 编程框架 | 多角色协作、消息协议、工具调用 | 想研究多 agent 的人 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 多角色 agent 编排框架 | 角色、任务、协作流程 | 想做业务 agent 的人 |
| [camel-ai/camel](https://github.com/camel-ai/camel) | 多 agent 研究和应用框架 | agent 社会、任务拆解、协作模式 | 想读 agent 研究工程的人 |
| [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 自动化 AI agent 平台 | 任务循环、工具调用、长期目标 | 想理解早期自主 agent 的人 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 轻量 AI agent | 工具接入、聊天工作流、轻量结构 | 想做小型 agent 的人 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 可成长的 agent 系统 | 记忆、工具、持续任务 | 想看 agent 产品化尝试的人 |
| [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) | 多模型 AI 助手和 agent harness | 多渠道、技能、记忆和工具 | 想做助手型 agent 的人 |

## Agent 应用与构建平台

| 项目 | 做什么 | 适合看什么 | 适合谁 |
| --- | --- | --- | --- |
| [langgenius/dify](https://github.com/langgenius/dify) | LLM 应用和 agent 工作流平台 | 应用编排、RAG、工具和发布 | 想做 AI 应用平台的人 |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 可视化构建 AI agent | 节点编排、流程编辑、模型连接 | 想做低代码 AI 工具的人 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 可视化构建 AI 工作流 | 组件图、部署、agent 流程 | 想做 AI workflow 的人 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | AI 聊天和本地模型界面 | 模型管理、用户界面、插件 | 想做 AI 客户端的人 |
| [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | AI 生产力客户端 | 多模型接入、助手管理、桌面体验 | 想做 AI 桌面产品的人 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | AI 驱动开发平台 | 代码任务、工具执行、开发代理 | 想做编程 agent 的人 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 浏览器操作 agent | 网页理解、动作执行、任务自动化 | 想做网页自动化 agent 的人 |
| [langchain-ai/agent-chat-ui](https://github.com/langchain-ai/agent-chat-ui) | agent 聊天界面 | 前端消息流、agent 会话、UI 结构 | 想做 agent 前端的人 |

## RAG、记忆与工具调用

| 项目 | 做什么 | 适合看什么 | 适合谁 |
| --- | --- | --- | --- |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | RAG 和 agent 上下文引擎 | 文档解析、检索、上下文构建 | 想做知识库 agent 的人 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | AI agent 记忆层 | 长期记忆、用户画像、上下文召回 | 想做持续记忆的人 |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | agent 工具和集成平台 | 工具注册、鉴权、外部系统连接 | 想做 agent 工具生态的人 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | LLM API 网关 | 多模型代理、成本控制、调用日志 | 想做模型网关的人 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR 工具集 | 文档识别、结构化抽取、多语言 | 想做文档 agent 的人 |
| [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | RAG 和企业搜索模板 | 数据同步、实时索引、RAG 管线 | 想做企业搜索的人 |

## 评测、观测与生产化

| 项目 | 做什么 | 适合看什么 | 适合谁 |
| --- | --- | --- | --- |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | LLM 可观测性平台 | trace、prompt、评测、数据集 | 想做 LLMOps 的人 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | AI 工程平台 | 模型管理、实验、部署和评估 | 想做 AI 工程化的人 |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | prompt、agent 和 RAG 测试工具 | 评测用例、回归测试、红队检查 | 想提高 AI 应用质量的人 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 可运行的 Agent 和 RAG 应用集合 | 应用样例、落地场景、模板组织 | 想找项目练手的人 |
| [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | prompt、RAG 和 agent 学习资料 | 提示工程、上下文工程、案例组织 | 想系统学习 AI 应用的人 |
| [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | 从零构建 agent harness 的学习项目 | shell agent、工具循环、最小实现 | 想理解 agent 底层的人 |

