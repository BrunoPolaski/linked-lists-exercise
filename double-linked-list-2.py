class Patient:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def show_patient(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}')
    
    def show_name_and_age(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Node:
    def __init__(self, patient: Patient):
        self.patient = patient
        self.next = None
        self.previous = None

class PatientDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, patient: Patient):
        new_node = Node(patient)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_end(self, patient: Patient):
        new_node = Node(patient)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_by_id(self, id):
        current = self.head
        while current is not None:
            if current.patient.id == id:
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

    def remove_head_product(self):
        self.head.next.previous = None
        self.head = self.head.next

    def remove_tail_product(self):
        self.tail.previous.next = None
        self.tail = self.tail.previous

    def show_by_id(self, id):
        current = self.head
        while current is not None:
            if current.patient.id == id:
                current.patient.show_patient()

    def show_reverse_list(self):
        current = self.tail
        while current is not None:
            current.patient.show_name_and_age()
            current = current.previous