import heapq

class MedianMonitor:
    def __init__(self):
        self.left = []   # Max-heap (invert values)
        self.right = []  # Min-heap

    def add(self, val: int):
        # Step 1: Insert
        if not self.left or val <= -self.left[0]:
            heapq.heappush(self.left, -val)
        else:
            heapq.heappush(self.right, val)

        # Step 2: Rebalance
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def median(self):
        if not self.left and not self.right:
            return None

        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]

    def debug(self):
        left_vals = [-x for x in self.left]
        right_vals = list(self.right)
        left_vals.sort(reverse=True)
        right_vals.sort()
        print(f"Left (MaxHeap): {left_vals}")
        print(f"Right (MinHeap): {right_vals}")
m = MedianMonitor()

m.add(28)
m.add(12)
m.add(3)
m.debug()
print("Median:", m.median())

m.add(56)
m.debug()
print("Median:", m.median())
