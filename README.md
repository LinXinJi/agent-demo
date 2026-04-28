# agent-demo

## 项目启动

1. 安装 `uv`
2. 执行 `uv sync`
3. 激活虚拟环境
4. 创建 .env 文件，添加 API_KEY 到环境变量，或直接在系统中配置

## 运行

启动指令

```
uv run main.py
```

或启动网页端指令

```
uvicorn main:app --host 127.0.0.1 --port 7932
```

## 测试

项目根目录下有 test.md 文件，可用于测试工具

## MCP 配置模板

```json
{
  "mcpServers": {
    "FileTools": {
      "command": "uv",
      "args": [
        "--directory",
        "F:\\GitHub\\agent-demo",
        "run",
        "tools.py"
      ]
    }
  }
}
```