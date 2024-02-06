#Quere from Stack
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # data = self.queue[0]
        # self.queue = self.queue[1:]
        data = self.queue.pop(0)
        return data

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0