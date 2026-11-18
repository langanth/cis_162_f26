
class Student:
    """
    Class Student
    A clas designed to hold grade information for a 
    given student

    attributes:
        name: str
        grades: list[str]
        credits: list[int]
    """
    
    def __init__(self, name, grades, credits):
        self.name = name
        if isinstance(grades, list):
            for i in grades:
                if not isinstance(i, str):
                    raise TypeError
                if not i in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']:
                    raise ValueError
            self.grades = grades
        else:
            raise TypeError
        self.credits = credits

    def add_grade(self, grade, credits):
        self.grades.append(grade)
        self.credits.append(credit)

    def calculate_gpa(self):       
        scale = {
            'A': 4.0,'A-': 3.7,'B+': 3.3,
            'B': 3.0,'C+': 2.3,'C': 2.0,
            'C-': 1.7,'D+': 1.3,'D': 1.0,
            'F': 0.0
        } 
        total_credits = 0
        total_quality_credits = 0
        for i in range(len(self.grades)):
            total_credits += self.credits[i]
            grade_points = scale[self.grades[i]]
            total_quality_credits += (grade_points * self.credits[i])
        return total_quality_credits / total_credits
    
    def honor_roll(self):
        return 3.2 <= self.calculate_gpa()

if __name__ == "__main__":
    try:
        lst = [1, "2", 3]
        print(type(lst[1:2]))
        jimmy = Student("Jimmy", ['A', 'B', 'C'], [3, 4, 3])
        print(jimmy.calculate_gpa())
        print(jimmy.honor_roll())
        val = isinstance(31, (int, float))
        print(val)
        bob = Student('Bob', [1, 2, 4], [3, 4, 3])
        print(bob.calculate_gpa())
    except TypeError:
        print('Wrong data types were used')
    except:
        print('Something went wrong')