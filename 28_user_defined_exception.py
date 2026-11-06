class InvalidMarksError(Exception):
    pass

marks = 120

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    print("Valid marks:", marks)
except InvalidMarksError as error:
    print("Error:", error)
