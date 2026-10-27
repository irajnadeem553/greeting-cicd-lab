
def calculate_grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
