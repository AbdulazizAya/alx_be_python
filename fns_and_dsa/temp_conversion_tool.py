class ValueTooHighError(Exception):

    def __str__(self):
        return f"Sorry the Value of the Number is Too High"
    

try:
    Val = int(input("Enter: "))
    if Val >= 100:
        raise ValueTooHighError
except ValueTooHighError as e:
    print(e)

