import re
import json

def extract_tool_calls(llm_response):
    """Extract tool calls, handling incomplete tags"""
    tool_calls = []
    
    # Look for opening tags
    opening_pattern = r'<TOOL_CALL>(.*?)(?:</TOOL_CALL>|$)'
    matches = re.findall(opening_pattern, llm_response, re.DOTALL)
    
    for match in matches:
        try:
            tool_data = json.loads(match.strip())
            tool_calls.append(tool_data)
        except:
            # Try to fix common issues
            fixed_match = match.strip()
            if fixed_match and not fixed_match.startswith('{'):
                fixed_match = '{' + fixed_match
            if fixed_match and not fixed_match.endswith('}'):
                fixed_match = fixed_match + '}'
            try:
                tool_data = json.loads(fixed_match)
                tool_calls.append(tool_data)
            except:
                continue
    
    return tool_calls

def remove_tool_calls(llm_response):
    """Remove tool calls to get clean conversation"""
    return llm_response
    #return re.sub(r'<TOOL_CALL>.*?</TOOL_CALL>', '', llm_response, flags=re.DOTALL).strip()