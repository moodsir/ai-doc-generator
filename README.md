AI 项目文档生成工具



一个智能化的项目文档自动生成工具,通过对接 Vercel API 接口,自动分析代码仓库并生成高质量的 README 和 Changelog 文档。



✨ 特性



🚀 自动化生成 - 一键生成专业的项目文档,无需手动编写

📊 智能分析 - 深度分析代码仓库结构,提取关键信息

📝 双文档支持 - 同时生成 README 和 Changelog 两种核心文档

🎨 Markdown 格式 - 生成标准的 Markdown 格式文档,便于阅读和编辑

⚡ 高效便捷 - 简单的命令行接口,快速完成文档生成



📋 功能说明



本工具通过调用 Vercel API 接口,实现以下核心功能:



README 生成: 自动生成包含项目介绍、安装步骤、使用方法等标准结构的项目说明文档

Changelog 生成: 智能分析代码变更历史,自动生成规范的版本更新日志

仓库分析: 支持对 GitHub、GitLab 等主流代码仓库的深度分析

灵活配置: 支持自定义项目路径和仓库地址



🛠️ 安装



环境要求



Python 3.7+

依赖包: requests==2.31.0



安装步骤



克隆项目仓库



bash

git clone https://github.com/moodsir/ai-doc-generator.git

cd ai-doc-generator





安装依赖包



bash

pip install -r requirements.txt





或手动安装:



bash

pip install requests==2.31.0





📖 使用方法



基本用法



通过命令行调用脚本来生成文档:



bash

python scripts/call\_api.py --project-path <项目路径> --repo-url <仓库地址>





参数说明



参数	必填	说明	示例

\--project-path	是	项目路径	/workspace/my-project

\--repo-url	是	代码仓库地址	https://github.com/user/repo

\--api-url	否	API 接口地址	https://xxx.vercel.app/api/generate



使用示例



示例 1: 生成单个项目的文档



bash

python scripts/call\_api.py \\

&#x20; --project-path "/ai-doc-generator" \\

&#x20; --repo-url "https://github.com/moodsir/ai-doc-generator"





示例 2: 使用自定义 API 地址



bash

python scripts/call\_api.py \\

&#x20; --project-path "/my-project" \\

&#x20; --repo-url "https://github.com/user/repo" \\

&#x20; --api-url "https://custom-api.example.com/generate"





输出格式



执行成功后,脚本会返回 JSON 格式的文档内容:



json

{

&#x20; "readme": "# 项目名称\\n\\n项目描述...",

&#x20; "changelog": "# Changelog\\n\\n## \[1.0.0] - 2024-01-01..."

}





你可以将返回的内容分别保存为 README.md 和 CHANGELOG.md 文件。



🏗️ 项目结构



plaintext

ai-doc-generator/

├── README.md                      # 项目说明文档

├── CHANGELOG.md                   # 版本更新日志

├── requirements.txt               # Python 依赖包

└── doc-generator/                 # 核心模块

&#x20;   ├── SKILL.md                   # 技能配置文件

&#x20;   ├── scripts/

&#x20;   │   └── call\_api.py           # API 调用脚本

&#x20;   └── references/

&#x20;       └── api\_spec.md           # API 接口规范文档





🔧 技术实现



Python 3.7+: 项目开发语言

requests: HTTP 请求库,用于调用 Vercel API

JSON: 数据交换格式

Markdown: 文档输出格式



⚠️ 注意事项



网络连接: 确保网络环境可以正常访问 Vercel API 接口

超时设置: 由于需要进行代码仓库分析,API 响应时间可能较长(建议超时时间 60 秒)

参数准确性: 确保 project\_path 和 repo\_url 参数正确无误

内容微调: 生成的文档内容可能需要根据实际情况进行适当调整



📝 开发说明



核心脚本说明



scripts/call\_api.py: 主脚本,负责调用 Vercel API 并处理返回结果



主要功能:



构建请求参数

发送 POST 请求

解析返回数据

错误处理和异常捕获



API 接口规范



详细的 API 接口说明请参考: references/api\_spec.md



🤝 贡献指南



欢迎提交 Issue 和 Pull Request 来改进本项目!



Fork 本仓库

创建特性分支 (git checkout -b feature/AmazingFeature)

提交更改 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

开启 Pull Request



📄 开源协议



本项目采用 MIT 协议开源。详见 LICENSE 文件。



👥 作者



moodsir - 项目维护者



🔗 相关链接



GitHub 仓库: https://github.com/moodsir/ai-doc-generator

API 文档: doc-generator/references/api\_spec.md



如有任何问题或建议,欢迎通过 Issue 进行反馈。

