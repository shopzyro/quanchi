from brain.llm_client import LLMClient
from tools.tool_executor import ToolExecutor
from utils.tool_parser import extract_tool_calls, remove_tool_calls

def main():
    print("🤖 AI Assistant with Computer Control")
    print("Type 'quit' to exit\n")
    
    client = LLMClient()
    executor = ToolExecutor()
    conversation_history = []
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("AI: Goodbye! 👋")
                break
            
            conversation_history.append({"role": "user", "content": user_input})
            
            print("AI: Thinking...")
            llm_response = client.generate_response(conversation_history)

            # Extract and execute tools (ONCE)
            tool_calls = extract_tool_calls(llm_response)

            for tool in tool_calls:
                result = executor.execute_tool(tool)
                print(f"🛠️  Execution result: {result}")
            
            # Show clean conversation to user
            clean_response = remove_tool_calls(llm_response)
            print(f"AI: {clean_response}")
            
            conversation_history.append({"role": "assistant", "content": clean_response})
            
    except KeyboardInterrupt:
        print("\n\nAI: Session ended by user. 👋")

if __name__ == "__main__":
    main()
