

class Stack(object):
    def __init__(self,limit=10):
        self.stack = []
        self.limit = limit

    def push(self,data):
        if len(self.stack) >= self.limit:
            raise IndexError("chaochurongliang")
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from a empty stack")

    def peek(self):
        if self.stack:
            return self.satck[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

def balanced_parentheses(parentheses):
        stack = Stack(len(parentheses))
        for parenthesis in parentheses:
            if parenthesis == "(":
                stack.push(parenthesis)
            else:
                if stack.is_empty():
                    return False
                else:
                    stack.pop()
        return stack.is_empty()


if __name__ == "__main__":
    examples = ["((()))","((())","(()))"]
    for example in examples:
        print(example + ":" +str(balanced_parentheses(example)))


