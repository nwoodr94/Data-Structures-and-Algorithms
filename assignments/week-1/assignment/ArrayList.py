class ArrayList:

    """
    ArrayList abstracts built-in list functionality.

    Attributes:
        data (list): A list of data
        size (int): The length of 'data'

    """

    size = None

    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def removeFront(self, k):
        """Remove the first 'k' elements in the ArrayList.
        
        Args:
            k (int): The number of elements to remove from the front of the list
        
        """
        del(self.data[0:k])
        self.size -= k

    def removeBack(self, k):
        """Remove the last 'k' elements in the ArrayList.
        
        Args:
            k (int): The number of elements to remove from the end of the list.
        
        """
        del(self.data[-k:])
        self.size -= k

    def removeAll(self, t):
        """Remove all elements matching 't' in the ArrayList.
        
        While the condition that 't' is in the ArrayList is True, the function calls lst.remove(t), and decrements the size property.

        Args:
            t (any): The target element to remove from the list
        
        """
        while t in self.data:
            self.data.remove(t)
            self.size -= 1

    def stretch(self, k):
        """Copy the ArrayList 'k' times and extend them into a new ArrayList. 

        For each iteration in range(k), the ArrayList is copied, and sorted, before incrementing the size property.

        Args:
            k (int): The number of times the original ArrayList should be copied

        """
        copy = []
        for i in range(k):
            copy.extend(self.data)
         
        self.size *= k
        copy.sort()

        self.data = copy

        return self.data

    def __str__(self):
        """Returns the string representation of the ArrayList"""
        return str(self.data)



aList = ArrayList([8, 17, 9, 24, 42, 3, 8])
aList.removeFront(4)
print(aList) # [42, 3, 8]


bList = ArrayList([8, 17, 9, 24, 42, 3, 8])
bList.removeBack(4)
print(bList) # [8, 17, 9]


cList = ArrayList(["a", "b", "c", "d", "a", "d", "d", "e", "f", "d"])
cList.removeAll("d")
print(cList) #['a', 'b', 'c', 'a', 'e', 'f']


dList = ArrayList([18.2, 7.5, 4.2, 24.9])
dList.stretch(3)
print(dList) #[4.2, 4.2, 4.2, 7.5, 7.5, 7.5, 18.2, 18.2, 18.2, 24.9, 24.9, 24.9]