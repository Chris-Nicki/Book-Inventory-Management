import shutil


def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


line_break()

# Task 1: Create a class named Book with attributes for title, author, genre, ISBN, and quantity.
class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f'{self.title} by {self.author}\nISBN: {self.isbn}\nQuantity: {self.quantity}'

# Task 2: Create a class named Node to represent nodes in the linked list. Each node will store a book object.
class Node:
    def __init__(self, book):  
        self.book = book
        self.next = None
        self.prev = None  

# Task 3: Implement a class named InventoryManager to manage the inventory using a linked list.
class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory
        self.head = None
        self.current_book = None

# Task 4: Implement the following methods in the **`InventoryManager`** class:
# - add_book(title, author, genre, isbn, quantity): Adds a new book to the inventory.
# - remove_book(isbn): Removes a book from the inventory based on its ISBN.
# - display_inventory(): Displays the current inventory.

    def add_book(self, title, author, genre, isbn, quantity):
        new_book = Book(title, author, genre, isbn, quantity)
        new_node = Node(new_book)  
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            new_node.prev = node  

    def remove_book(self, isbn):
        if self.head is None:
            print(f'{self.inventory} has no books in it!')
            return
        if self.head.book.isbn == isbn:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        current_node = self.head
        while current_node:
            if current_node.book.isbn == isbn:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

        print(f'{isbn} is not in the {self.inventory} inventory list')

    def display_inventory(self):
        print(self.inventory)
        line_break()
        current_node = self.head
        while current_node:
            print(current_node.book)
            line_break()
            current_node = current_node.next


aurora_library = InventoryManager("Aurora Library")


aurora_library.add_book("Dead Space", "S.A. Barnes", "Fiction", "9781250819994", "10")
aurora_library.add_book("Ghost Station", "S.A. Barnes", "Fiction", "9781250819754", "5")
aurora_library.add_book("Galaxy's Best Chef", "Ryan Duval", "Non-Fiction", "9781250814594", "2")

aurora_library.remove_book("9781250814594")

aurora_library.display_inventory()





