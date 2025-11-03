import os
from huggingface_hub import InferenceClient

os.environ["HUGGINGFACE_HUB_TOKEN"] = "hf_your_actual_token_here"

class LLMClient:
    def __init__(self):
        self.model_name = "deepseek-ai/DeepSeek-V3.2-Exp"
        self.client = InferenceClient(model=self.model_name)
        print(f"✅ Using {self.model_name}")
    
    def generate_response(self, conversation_history):
        try:
            # Add system prompt with available tools
            system_prompt = """You are Quan Chi, an AI assistant that can also control computers.
            Available tools: click(x,y), type_text(text), open_program(name), press_key(key)
            When you need to use a tool, wrap it in <TOOL_CALL> tags in the following format:
            <TOOL_CALL>{"tool": "click", "params": {"x": 100, "y": 200}}</TOOL_CALL>"""
            
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(conversation_history)
            
            response = self.client.chat_completion(
                messages=messages,
                max_tokens=300,  # Increased for tool calls
                temperature=0.7,
            )

            return response.choices[0].message["content"].strip()
        
        except Exception as e:
            return f"API Error: {str(e)}"

if __name__ == "__main__":
    client = LLMClient()
    test_convo = [{"role": "user", "content": "Hello! How are you today?"}]
    response = client.generate_response(test_convo)
    print(f"Response: {response}")
