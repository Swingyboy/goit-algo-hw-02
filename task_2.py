from collections import deque


def is_palindrome(string: str) -> bool:
    queue = deque()
    for ch in string:
        queue.append(ch)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True
