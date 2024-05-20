class Student:
    def __init__(self, name, average, registration):
        self.name = name
        self.average = average
        self.registration = registration

    def show_student(self):
        print(f'{self.name} - {self.average}')

class Node:
    def __init__(self, student):
        self.student = student
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, student):
        new_node = Node(student)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def show_students(self):
        current = self.head
        while current is not None:
            current.student.show_student()
            current = current.next

    def remove_student(self, registration):
        current = self.head
        previous = None
        while current is not None:
            if current.student.registration == registration:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def show_student_by_registration(self, registration):
        current = self.head
        while current is not None:
            if current.student.registration == registration:
                current.student.show_student()
                return
            current = current.next