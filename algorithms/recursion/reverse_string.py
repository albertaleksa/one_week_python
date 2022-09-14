# Implement a function that reverses a string using iteration...and then recursion!


def reverse_string_recursive(string):
    if len(string) < 2:
        return string
    return f"{string[-1]}{reverse_string_recursive(string[1:-1])}{string[0]}"


def reverse_string_iterative(string):
    result = []
    for i in range(len(string)-1, -1, -1):
        result.append(string[i])
    return "".join(result)


if __name__ == "__main__":
    print(reverse_string_recursive("yoyo mastery"))
    print(reverse_string_iterative("yoyo mastery"))