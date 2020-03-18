"""
File:   student.py
Resources to manage a student's name and grades.
"""

class Student(object):
    """Represents the student"""

    def __init__(self, name, id = "NA", number = 0):
        """ 
        Constructor creates a Student with the given name and number of
        scores and sets all the scores to 0.
        """
        self.name = name
        self.id = id
        self.scores =[]
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """
        Returns student name.
        """
        return self.name

    def setScore(self, i, score):
        """
        Resets the ith score, counting from 1.
        """
        self.scores[i-1] = score

    def getScore(self, i):
        """
        Returns the ith score, counting from 1.
        """
        return self.scores[i-1]

    def getAverage(self):
        """
        Returns the average score.
        """
        return (sum(self.scores)/len(self.scores))

    def getHighScore(self):
        """
        Returns the highest score.
        """
        return max(self.scores)

    def __str__(self):
        """
        Returns the string representation of the student.
        """
        return "Name: " + self.name + \
           "\nID: " + self.id + \
            "\nScores:" + \
            " ".join(map(str, self.scores))