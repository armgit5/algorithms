a = "{[]()}"
b = "{[(])}"

def is_valid(brackets):
    openers_to_closers = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    openers = frozenset(openers_to_closers.keys())
    closers = frozenset(openers_to_closers.values())

    openers_stack = []

    for char in brackets:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_opener = openers_stack.pop()
                if not openers_to_closers[last_opener] == char:
                    return False
    return openers_stack == []


print(is_valid(a))
print(is_valid(b))