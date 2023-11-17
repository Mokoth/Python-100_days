class SchoolMember:
    """Represents any school member"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('(Initialized SchoolMember: {})'.format(self.name))
        print(f'(Initialized SchoolMember: {self.name})')

    
    def tell(self):
        """Tell my details."""
        # print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
        print(f'Name: {self.name} Age: {self.age}', end=" ")

    
class Teacher(SchoolMember):
    """Represents a teacher."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))


    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

    
class Student(SchoolMember):
    """Represents a student."""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))


    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Marcus', 24, 300200)
s = Student('Noble', 25, 90)

# prints a blank lline
print()

members = [t, s]
for member in members:
    # Workd for both Teachers and Students
    member.tell()