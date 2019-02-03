class TinyIntError(Exception):
    pass

def tiny_int(val):
    # tinyInt SQL evaluation
    return  val >= 0 and val <= 255

try:
    number = 400
    if tiny_int(number):
        print("Correct \n")
    else:
        # executes a custom exception
        raise TinyIntError("Your evaluation exceeds of 256 or is lower than 0, is not a TinyInt")
except TinyIntError as e:
    print(e)
    print("Unable to complete functionality \n")
