import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, value):
        heapq.heappush(self.queue, (priority, value))

    def dequeue(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def __str__(self):
        return str(self.queue)


pq = PriorityQueue()
pq.enqueue(3, "Low")
pq.enqueue(1, "High")
pq.enqueue(2, "Medium")

print("Dequeued:", pq.dequeue())
print("Dequeued:", pq.dequeue())
print("Dequeued:", pq.dequeue())
