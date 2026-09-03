# Control-plane API

`strategy-pipeline` 负责协调 owner 实现和 artifact publication，传递 reference 和
receipt，不计算 artifact 的具体内容。

## Contracts

`ArtifactRef` 用 kind、URI、digest 和 producer 标识不可变输出。`RunRequest` 携带
run ID 和输入 artifact reference。`PublicationRequest` 与 `HandoffRequest` 描述
下游交付。`RunReceipt` 记录公共结果，不暴露 owner 的异常文本。

```python
from strategy_pipeline import ArtifactRef, RunRequest, run

request = RunRequest(run_id="run-2026-01-01", inputs=())
```

所有 contract 都是不可变且经过校验的 dataclass。产出 artifact 的代码应返回
`ArtifactRef`，避免返回内存中的 domain object 或 provider client。

## 编排

公共 runner 先调用 `RunOwner`，再调用 `ArtifactPublisher`：

```python
receipt = run(request, owner=owner, publisher=publisher)
if receipt.status == "published":
    print(receipt.artifacts)
```

注入的实现抛出异常时，runner 返回经过脱敏的 `owner_failure` 或
`publication_failure` category，不把私有异常细节序列化到 receipt。

## 其他边界

使用 `publish_artifact` 接入 callable writer，使用 `publish_handoff` 接入目标
publisher。两者都会校验注入实现返回 `ArtifactRef`。

公共包不包含 provider SDK、凭证、网络 client、存储 backend、模型实现或策略 registry。
这些能力应放在使用方仓库的 adapter 后面。
