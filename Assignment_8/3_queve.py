# class Queue:
#     def init(self):
#         self.items = []

#     def enqueue(self, item: str):
#         if isinstance(item, str):
#             self.items.append(item)
#             print(f"Enqueued: {item}")
#         else:
#             print("Only string values are allowed.")


#     def dequeue(self):
#         if self.items:
#         removed = self.items.pop(0)
#         print(f"Dequeued: {removed}")
#         return removed
#       else:
# print("Queue is empty.")
# #         return None


#             def size(self):
#     print(f"Queue size: {len(self.items)}")
#     return len(self.items)


# q = Queue()
# q.enqueue("apple")
# q.enqueue("banana")
# q.enqueue("cherry")
# q.dequeue()
# q.size()
# print("Remaining items in queue:", q.items)
class Queue:
    def __init__(self):
        self.queueTask = []

    def enqueue(self, item: str):
        if isinstance(item, str):
            self.queueTask.append(item)
            print(f"Enqueued: {item}")
        else:
            print("Only string values are allowed.")

    def dequeue(self):
        if self.queueTask:
            removed = self.queueTask.pop(0)
            print(f"Dequeued: {removed}")
            return removed

        else:
            print("Queue is empty.")
            return None

    def size(self):
        print(f"Queue size: {len(self.queueTask)}")
        return len(self.queueTask)


q = Queue()
q.enqueue("apple")
q.enqueue("banana")
q.enqueue("cherry")
q.dequeue()
q.size()
print("Remaining items in queue:", q.queueTask)
