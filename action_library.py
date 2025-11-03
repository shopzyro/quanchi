import pyautogui
import time

class ActionLibrary:
    def __init__(self):
        pyautogui.FAILSAFE = True
    
    def smart_wait(self, seconds):
        """Better than time.sleep - we can enhance this later"""
        time.sleep(seconds)
    
    def click_and_verify(self, x, y, expected_change=None):
        """Click with basic verification"""
        print(f"Clicking at ({x}, {y})")
        pyautogui.click(x, y)
        
        if expected_change:
            # Simple verification - we'll improve this
            self.smart_wait(1)
            # TODO: Add visual verification later
    
    def type_with_confidence(self, text):
        """Type text reliably"""
        pyautogui.write(text, interval=0.05)  # Slower, more reliable
    
    def open_program(self, name):
        """Open program with better error handling"""
        try:
            pyautogui.hotkey('win')
            self.smart_wait(0.5)
            pyautogui.write(name)
            self.smart_wait(0.5)
            pyautogui.press('enter')
            self.smart_wait(2)
            return True
        except:
            return False

# Test with what we have
actions = ActionLibrary()
