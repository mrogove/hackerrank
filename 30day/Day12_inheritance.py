"""
https://www.hackerrank.com/challenges/30-inheritance/problemx
"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores #a little fuzzy on this call
    def calculate(self):
        val = self.scores
        temp = 0
        for i in val:
            temp += int(i)
        num = temp//len(val)

        if num >= 90 and num <=100:
            return "O"
        elif num >= 80 and num <90:
            return "E"
        elif num >= 70 and num <80:
            return "A"
        elif num >= 55 and num <70:
            return "P"
        elif num >= 40 and num <55:
            return "D"
        else:
            return "T"

#given:
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
