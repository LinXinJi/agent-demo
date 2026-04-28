from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("File Tools")

@mcp.tool()
def list_files(path: str) -> list:
    """列出指定路径下的所有文件"""
    return os.listdir(path)

@mcp.tool()
def read_file(file_path: str) -> str:
    """读取指定文件的内容"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

@mcp.tool()
def rename_file(old_name: str, new_name: str) -> None:
    """重命名文件"""
    os.rename(old_name, new_name)

# 可以用装饰器，也可以用 add_tool 方法注册工具
# mcp.add_tool(list_files)
# mcp.add_tool(read_file)
# mcp.add_tool(rename_file)

if __name__ == "__main__":
    # 启动 MCP 服务，这里使用 stdio 模式，适合与 CLI 程序交互，缺点是 mcp 服务和 agent 只能跑在同一台机器上。
    mcp.run("stdio")    