# python program to append, delete and display elements of a list using classes

class List:
    def __init__(self, list1):
        self.list1 = list1

    def append(self):
        element = input("Enter to append to the list: ")
        self.list1.append(element)
        print("")

    def delete(self):
        x = self.list1.pop()
        print("Element deleted is", x)
        print("")

    def display(self):
        print("The list is", self.list1)
        print("")

if __name__=='__main__':
    list1 = List([])
    while True:
        choice = int(input("Enter 1 to append and 2 to delete a element: "))
        if choice == 1:
            list1.append()
            list1.display()
        elif choice == 2:
            list1.delete()
            list1.display()
        else:
            break