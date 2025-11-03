TOOL_REGISTRY = {
    "click": {
        "description": "Click at screen coordinates (x, y) with verification",
        "parameters": {"x": "number", "y": "number"},
        "function": "action_library.click_and_verify"  # Updated
    },
    "type_text": {
        "description": "Type text reliably at current cursor position", 
        "parameters": {"text": "string"},
        "function": "action_library.type_with_confidence"  # Updated
    },
    "open_program": {
        "description": "Open a program by name",
        "parameters": {"program_name": "string"},
        "function": "action_library.open_program"
    },
    "press_key": {
        "description": "Press a keyboard key",
        "parameters": {"key": "string"},
        "function": "pyautogui.press"  # Direct call
    }
}