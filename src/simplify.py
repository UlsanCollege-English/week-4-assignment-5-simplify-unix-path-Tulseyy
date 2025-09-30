

def simplify_path(path):
    parts = path.split('/')
    stack = []
    
    for part in parts:
        if part == '' or part == '.':
            # Ignore empty parts and current directory symbol
            continue
        elif part == '..':
            # Go up one directory if possible
            if stack:
                stack.pop()
        else:
            # Valid directory name, push onto stack
            stack.append(part)
    
    # Construct normalized path
    return '/' + '/'.join(stack)
