# to reverse a string using a stack

def reverse_string_stack(input_str):
    stack = list(input_str)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

input_string = "Hello, World!"
reversed_string = reverse_string_stack(input_string)
print(reversed_string)  # Output: "!dlroW ,olleH"