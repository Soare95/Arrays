class Array:

    def __init__(self):
        self.data = {}
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        del self.data[self.length-1]
        self.length -= 1

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]

        del self.data[self.length-1]
        self.length -= 1


my_array = Array()

my_array.append(1)
my_array.append(5)
my_array.append("car")
my_array.pop()
my_array.append("BMW")
my_array.append("Super")
my_array.delete(2)
print(my_array)
