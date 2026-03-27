Changelog



本文档记录 AI 项目文档生成工具的所有重要变更。



格式遵循 Keep a Changelog,版本号遵循 语义化版本。



\[Unreleased]



计划中



支持更多代码托管平台(GitLab, Gitee 等)

添加更多文档模板选项

支持自定义文档结构

添加 Webhook 集成功能



\[1.0.0] - 2026-03-26



新增



🎉 首次发布 AI 项目文档生成工具

✨ 核心功能:对接 Vercel API 接口

📝 自动生成 README 文档功能

📊 自动生成 Changelog 文档功能

🔍 智能代码仓库分析能力

🛠️ 命令行接口支持

📦 完整的 Python 依赖管理

📖 详细的 API 接口规范文档

💡 完善的使用说明和示例



功能特性



支持 GitHub 代码仓库分析

支持 Markdown 格式文档输出

提供灵活的参数配置选项

完善的错误处理和异常捕获

60 秒超时设置,适应复杂仓库分析



文档



完整的 README.md 项目说明文档

详细的 scripts/call\_api.py 脚本注释

规范的 references/api\_spec.md API 接口文档

多个使用示例和参数说明



技术栈



Python 3.7+ 支持

requests 2.31.0 HTTP 客户端

JSON 数据交换格式

标准 Markdown 文档格式



依赖包



plaintext

requests==2.31.0





版本说明



版本号规则



本项目的版本号遵循语义化版本规范(Semantic Versioning):



主版本号(MAJOR) : 不兼容的 API 修改

次版本号(MINOR) : 向下兼容的功能性新增

修订号(PATCH) : 向下兼容的问题修正



变更类型说明



新增: 新增的功能

变更: 功能的变更

弃用: 即将在未来版本中移除的功能

移除: 已在版本中移除的功能

修复: Bug 修复

安全: 安全性相关的修复



升级指南



从 1.0.0 升级到未来版本



请关注每个版本的变更说明,特别是:



弃用(Deprecated) : 提前了解即将移除的功能

移除(Removed) : 确保代码中不再使用已移除的功能

新增(Added) : 了解新功能并考虑是否需要升级使用



问题反馈



如果在使用过程中遇到问题,欢迎通过以下方式反馈:



GitHub Issues: https://github.com/moodsir/ai-doc-generator/issues



贡献者



moodsir - 初始版本发布



本 Changelog 最后更新时间: 2026-03-26

