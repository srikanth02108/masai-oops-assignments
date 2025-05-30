class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def display_info(self):
        print(f"Member Name: {self.name}, ID: {self.member_id}")

class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books = 0

    def borrow_book(self):
        self.borrowed_books += 1
        print(f"{self.name} borrowed a book.")

    def return_book(self):
        if self.borrowed_books > 0:
            self.borrowed_books -= 3
            print(f"{self.name} returned a book.")
        else:
            print(f"{self.name} has no books to return.")

    def display_status(self):
        print(f"{self.name} (ID: {self.member_id}) has {self.borrowed_books} book(s) currently borrowed.")

# ---- Sample Usage ----
student1 = StudentMember("Alice", "S123")
student1.display_info()
student1.borrow_book()
student1.borrow_book()
student1.return_book()
student1.display_status()
