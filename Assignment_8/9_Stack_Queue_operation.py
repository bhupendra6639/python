def check_operations(operations):
    stack = []
    queue = []
    stack_result = []
    queue_result = []

    for op in operations:
        action = op[0]
        if len(op) > 1:
            value = op[1]
        else:
            None

        if action == "push":
            stack.append(value)
        elif action == "pop":
            if stack:
                stack_result.append(stack.pop())

        elif action == "enqueue":
            queue.append(value)
        elif action == "dequeue":
            if queue:
                queue_result.append(queue.pop(0))

    return stack_result, queue_result


ops = [
    ("push", 1),
    ("push", 2),
    ("pop",),
    ("enqueue", 10),
    ("enqueue", 20),
    ("dequeue",),
]

stack_output, queue_output = check_operations(ops)
print("Stack result:", stack_output)
print("Queue result:", queue_output)
