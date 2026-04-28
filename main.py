import os
from dotenv import load_dotenv

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from pydantic_ai.messages import ModelMessage

import tools

load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

system_prompt = """你是一名资深的软件工程师，希望你能用严谨抽象的思维来分析问题，给出清晰的解决方案。"""

model = OpenAIChatModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key=DEEPSEEK_API_KEY),
)

agent = Agent(
    model,
    system_prompt=system_prompt,
    tools=[tools.list_files, tools.read_file, tools.rename_file]
)

def main():
    # 存储对话历史
    history: list[ModelMessage] = []
    
    print("AI助手已启动（输入 'exit' 退出）")
    print("\n============================================")
    
    while True:
        user_input = input("\n请输入你的问题：")
        
        print("\n--------------------------------------------\n")
        if user_input.lower() in ('exit', 'quit'):
            break
        
        # 将历史消息传入，实现短期记忆
        response = agent.run_sync(user_input, message_history=history)
        
        print("\nAI回答：", response.output)
        print("\n============================================")
        
        # 更新消息历史
        # response.new_messages 包含了本轮对话的完整消息（用户输入 + AI回复 + 工具调用等）
        history.extend(response.new_messages())
        
app = agent.to_web()

if __name__ == "__main__":
    main()    
