import pyautogui
from action_library import ActionLibrary
from tools.tool_registry import TOOL_REGISTRY

class ToolExecutor:
    def __init__(self):
        self.actions = ActionLibrary()
    
    def execute_tool(self, tool_call):
        try:
            tool_name = tool_call["tool"]
            params = tool_call["params"]
            
            if tool_name == "click":
                self.actions.click_and_verify(params.get("x"), params.get("y"))
            elif tool_name == "type_text":
                self.actions.type_with_confidence(params.get("text"))
            elif tool_name == "open_program":
                # Handle both "name" and "program_name" parameters
                program_name = params.get("program_name") or params.get("name")
                if program_name:
                    self.actions.open_program(program_name)
                else:
                    return {"success": False, "error": "Missing program name"}
            elif tool_name == "press_key":
                pyautogui.press(params.get("key"))
                
            return {"success": True, "tool": tool_name}
            
        except Exception as e:
            return {"success": False, "error": str(e)}