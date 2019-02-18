class Array(list):
    def __new__(cls, value):
        return list.__new__(cls, list(value))
    def map(self, func):
        return Array([func(i) for i in self])
    def filter(self, func):
        return Array([i for i in self if func(i)])
    def reduce(self, func, t=0):
        for i in self:
            t = func(t, i)
        return t
    def reduceRight(self, func, t=0):
        for i in self:
            t = func(t, self[len(selfself.index(i)])
        return t
    def some(self, func):
        for i in self:
            if func(i):
                return True
        return False
    def every(self, func):
        for i in self:
            if not func(i):
                return False
        return True
    def find(self, func):
        for i in self:
            if func(i):
                return i
        return None
    def findIndex(self, func):
        for i in self:
            if func(i):
                return self.index(i)
        return -1
    def keys(self):
        return Array([i for i in range(len(self))])
    def entries(self):
        obj = {}
        for i in range(len(self)):
            obj[i] = self[i]
        return obj
