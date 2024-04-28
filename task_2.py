from collections import deque


def is_palindrome(string: str) -> bool:
    queue = deque()
    string: str = string.lower().replace(" ", "")

    for ch in string:
        queue.append(ch)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("Able was I ere I saw Elba"))
    print(is_palindrome("Hello"))
    print(is_palindrome("Was it a car or a cat I saw"))
