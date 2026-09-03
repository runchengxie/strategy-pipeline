# 参与贡献

公共包应保持无依赖、与具体领域无关的边界。Pull request 应使用 synthetic fixture，
不能加入 owner 仓库导入、provider SDK、凭证、私有路径或策略选择规则。

本地检查时，先用 `scripts/dev/public_surface_export.py` 导出经过审阅的公共 surface，
再在无依赖环境中安装导出结果，并运行 `tests/control_plane` 下的 synthetic 测试。
