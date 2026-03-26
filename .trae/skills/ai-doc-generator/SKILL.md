---
name: "ai-doc-generator"
description: "AI项目文档生成Skill。生成README、更新日志、发布说明。调用时机：用户需要生成项目文档或询问如何生成项目文档时。"
---

# AI 项目文档生成 Skill

## 核心定位

API 优先、格式锁死、AI 专用、全球通用

覆盖文档类型：
- README（项目说明文档）
- Changelog（更新日志）
- Release Notes（发布说明）

## API 设计

### 请求地址

```
POST /api/generate-doc
```

### 请求参数

```json
{
  "api_key": "string",
  "content": "string",
  "doc_type": "readme | changelog | release_note",
  "lang": "zh | en (默认zh)"
}
```

### 返回格式

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "doc_type": "readme",
    "lang": "zh",
    "title": "文档标题",
    "content": "完整内容",
    "generate_time": 1742123456
  }
}
```

### 状态码

| 状态码 | 含义 |
|--------|------|
| 200 | 成功 |
| 400 | 参数错误 |
| 401 | 无效 api_key |
| 429 | 调用超限 |
| 500 | 服务器异常 |

## AI Prompt（固定格式）

```
你是专业项目文档生成助手。
只输出标准结构，不要解释，不要多余内容。
输出格式严格如下：

[TITLE]
文档标题

[CONTENT]
完整文档内容
```

## 后端解析逻辑

通过正则表达式截取 `[TITLE]` 和 `[CONTENT]` 标记内容，强制包装成固定 JSON 返回，确保 AI 输出格式统一。

## 密钥配置

| 密钥 | 额度 |
|------|------|
| free_tier_key | 50次/天 |
| pro_tier_key | 无限次 |

## 商业化方案

- 免费版：50 次/天
- 基础版：9.9 元/月 无限次
- 专业版：29.9 元/月 多密钥
- 终身版：29.9 元一次性

## 使用示例

当用户需要生成以下文档时使用此 Skill：

1. 生成项目 README 文档
2. 生成更新日志 Changelog
3. 生成发布说明 Release Notes
4. 询问文档生成 API 的使用方法
5. 需要将功能描述转换为标准文档格式

此 Skill 专注于项目文档自动生成场景，确保输出格式统一规范。
