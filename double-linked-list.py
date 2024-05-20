class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product(self):
        print(f'{self.name} - {self.price} - {self.quantity}')

class Node:
    def __init__(self, product):
        self.product = product
        self.next = None
        self.previous = None
    
class ProductDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, product):
        new_node = Node(product)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_start(self, product):
        new_node = Node(product)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def show_products(self):
        current = self.head
        while current is not None:
            current.product.show_product()
            current = current.next

    def remove_product(self, name):
        current = self.head
        while current is not None:
            if current.product.name == name:
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                return
            current = current.next

    def show_product_by_name(self, name):
        current = self.head
        while current is not None:
            if current.product.name == name:
                current.product.show_product()
                return
            current = current.next

    def show_products_in_reverse(self):
        current = self.tail
        while current is not None:
            current.product.show_product()
            current = current.previous