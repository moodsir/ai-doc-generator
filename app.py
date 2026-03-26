from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import re

def call_ai(content: str, doc_type: str, lang: str):
    prompt = f"""
你是专业项目文档生成助手。
只输出标准结构，不要解释，不要多余内容。
输出格式严格如下：
[TITLE]
文档标题
[CONTENT]
完整文档内容

生成类型：{doc_type}
语言：{"中文" if lang=="zh" else "English"}
内容：{content}
    """
    return f"""
[TITLE]
{content[:20]}项目文档
[CONTENT]
# {doc_type.upper()}

本文档由AI自动生成。

## 内容概要
{content}

---
生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}
"""

def parse_ai_output(text: str):
    title = re.search(r'\[TITLE\]\s*(.*?)\s*\[CONTENT\]', text, re.DOTALL)
    content_match = re.search(r'\[CONTENT\]\s*(.*)', text, re.DOTALL)
    return {
        "title": (title.group(1) or "无标题").strip(),
        "content": (content_match.group(1) or "无内容").strip()
    }

key_config = {
    "free_tier_key": {"limit": 50, "count": 0},
    "pro_tier_key": {"limit": -1, "count": 0}
}

app = FastAPI()

class RequestBody(BaseModel):
    api_key: str
    content: str
    doc_type: str
    lang: str = "zh"

@app.post("/api/generate-doc")
async def generate_doc(body: RequestBody):
    if body.api_key not in key_config:
        raise HTTPException(status_code=401, detail="invalid api_key")

    user = key_config[body.api_key]
    if user["limit"] != -1:
        if user["count"] >= user["limit"]:
            raise HTTPException(status_code=429, detail="rate limit exceeded")
        user["count"] += 1

    if body.doc_type not in ["readme", "changelog", "release_note"]:
        raise HTTPException(status_code=400, detail="invalid doc_type")

    ai_raw = call_ai(body.content, body.doc_type, body.lang)
    parsed = parse_ai_output(ai_raw)

    return {
        "code": 200,
        "msg": "success",
        "data": {
            "doc_type": body.doc_type,
            "lang": body.lang,
            "title": parsed["title"],
            "content": parsed["content"],
            "generate_time": int(time.time())
        }
    }

@app.get("/")
async def root():
    return {"info": "AI Doc Skill API Running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
