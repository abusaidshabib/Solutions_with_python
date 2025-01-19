def is_valid_parentheses(s: str) -> bool:
    stack = []
    # Map of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:  # Check if it matches the last opening bracket
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets are matched
    return not stack

# Example usage
print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))  # False
print(is_valid_parentheses("([)]"))  # False
print(is_valid_parentheses("{[]}"))  # True



