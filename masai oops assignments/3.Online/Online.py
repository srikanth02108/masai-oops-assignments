class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

class Instructor(User):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.expertise = expertise

    def upload_content(self):
        print(f"{self.name} uploaded course content.")

    def display_info(self):
        print(f"Instructor: {self.name}, Email: {self.email}, Expertise: {self.expertise}")

class CourseCreator(Instructor):
    def __init__(self, name, email, expertise):
        super().__init__(name, email, expertise)
        self.courses = []

    def create_course(self, course_name):
        self.courses.append(course_name)

    def display_info(self):
        print(f"Course Creator: {self.name}, Email: {self.email}, Expertise: {self.expertise}")
        print(f"Courses Created: {self.courses}")

# Runtime input and usage 
if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    expertise = input("Enter your expertise: ")

    creator = CourseCreator(name, email, expertise)

    num_courses = int(input("How many courses do you want to add? "))
    for _ in range(num_courses):
        course = input("Enter course name: ")
        creator.create_course(course)

    creator.upload_content()
    creator.display_info()
