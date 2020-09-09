class ArrayList:

    size = None

    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def removeFront(self, k):
        del(self.data[0:k])
        size -= k

    def removeBack(self, k):
        del(self.data[-k:])
        size -= k

    def removeAll(self, t):
        while t in self.data:
            self.data.remove(t)
            size -= 1

    def stretch(self, k):
        copy = []
        for i in range(k):
            copy.extend(self.data)
         
        size *= k
        copy.sort()

        self.data = copy

        return self.data

    def __str__(self):
        return str(self.data)


#a Remove the first k elements
aList = ArrayList([8, 17, 9, 24, 42, 3, 8])
aList.removeFront(4)
print(aList) # [42, 3, 8]

#b Remove the last k elements
bList = ArrayList([8, 17, 9, 24, 42, 3, 8])
bList.removeBack(4)
print(bList) # [8, 17, 9]

#c Remove all matching elements
cList = ArrayList(["a", "b", "c", "d", "a", "d", "d", "e", "f", "d"])
cList.removeAll("d")
print(cList) #['a', 'b', 'c', 'a', 'e', 'f']

#d Stretch list with k copies
dList = ArrayList([18.2, 7.5, 4.2, 24.9])
dList.stretch(3)
print(dList) #[4.2, 4.2, 4.2, 7.5, 7.5, 7.5, 18.2, 18.2, 18.2, 24.9, 24.9, 24.9]