# Strategy Pipeline

面向研究评估、artifact 编排、发布、回执和下游交接的公共 pipeline 能力。

本仓库负责 run 周边的物流控制。具体策略、研究流程、特征模型、组合规则、数据
provider 和执行场所由使用方仓库负责，并通过独立的薄 adapter 接入。

## 安装

```bash
pip install strategy-pipeline
```

运行时依赖 `alpha-research` 和 `portfolio-backtester` 提供的 owner API。请先阅读[文档首页](docs/README.md)、[控制面 API](docs/control-plane.md)
和 [owner 接入指南](docs/integrating-an-owner.md)。

## 提供的能力

- 类型明确的 request、artifact reference 和 run receipt
- 从 owner 到 publication 的确定性编排
- 与 provider 无关的 artifact publication 和 handoff 边界
- 数据集、信号和回测结果的通用 artifact 写入
- 把评估指标、组合回放和暴露产物连接起来的通用评估编排
- 把运行上下文和产物引用整理成结构化摘要
- 不依赖私有模块的通用 CLI

公共包不包含策略代码、provider SDK、凭证、私有研究流程或专有数据。
