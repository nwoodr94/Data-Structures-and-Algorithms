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