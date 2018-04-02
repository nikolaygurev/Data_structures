def bracket_sequence(sequence):
    """Time complexity: O(n), where n = len(sequence)"""
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    first_left_bracket_pos = 0

    for i, char in enumerate(sequence, 1):
        if char in brackets.values():
            stack.append(char)
            if first_left_bracket_pos == 0:
                first_left_bracket_pos = i

        elif char in brackets:
            if not stack or brackets[char] != stack.pop():
                return i

            if not stack:
                first_left_bracket_pos = 0

    return first_left_bracket_pos if stack else 'Success'


def main():
    sequence = input()
    print(bracket_sequence(sequence))


if __name__ == '__main__':
    main()
