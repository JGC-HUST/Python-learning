# inherit.py
# coding=UTF-8
class SchoolMember:
      '''代表学校里的成员'''
      def __init__(self, name, age):
            self.name = name
            self.age = age
            print('(Initialized SchoolMember: {})'.format(self.name))

      def tell(self):
            '''告诉我有关我的细节'''
            print('Name:"{}" Age:"{}"'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
      '''代表一位老师'''
      def __init__(self, name, age, salary):
            SchoolMember.__init__(self, name, age)
            self.salary = salary
            print('(Initialized Teacher: {})'.format(self.name))

      def tell(self):
            SchoolMember.tell(self)
            print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
      '''代表一位同学'''
      def __init__(self, name, age, marks):
            SchoolMember.__init__(self, name, age)
            self.marks = marks
            print('(Initialized Student: {})'.format(self.name))

      def tell(self):
            SchoolMember.tell(self)
            print('Marks: "{:d}"'.format(self.marks))

t = Teacher('A', 40, 300000)
s = Student('B', 25, 99)

print()

members = [t, s]
for member in members:
      member.tell()
