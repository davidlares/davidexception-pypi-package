class TinyIntError(Exception):
    # constructor
    def __init__(self):
        self.message = "Your evaluation exceeds of 256 or is lower than 0, is not a TinyInt"

    # class override
    def __str__(self):
        return self.message

def tiny_int(val):
    # tinyInt SQL evaluation
    return  val >= 0 and val <= 255

def validate_value(val):
    # validating if value is a integer instance
    try:
        return isinstance(int(val), int)
    except ValueError as e:
        return False

def tiny_int_eval(val):
    try:
        if validate_value(val) and tiny_int(val):
            return True
        else:
            raise TinyIntError()
    except TinyIntError as error:
        print(error)

print(tiny_int_eval(400))
