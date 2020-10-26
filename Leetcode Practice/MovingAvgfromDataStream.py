class MovingAverage():
    def __init__(self, size):
        self.q = []
        self.maxsize = size
        
    def next(self, val):
        if len(self.q) < self.maxsize:
            self.q.append(val)
            return sum(self.q)/len(self.q)
        else:
            self.q.pop(0)
            self.q.append(val)
            return sum(self.q)/self.maxsize
        
k = MovingAverage(3)
print(k.next(1))
print(k.next(10))
print(k.next(3))
print(k.next(5))
