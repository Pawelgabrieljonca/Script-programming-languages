input_string = "2,5"
try:
    # some_number = 3/0
    # some_number = float(input_string)
    some_number = float(input_string)
    print(f"This number is: {some_number}")
except (ValueError, UnicodeError) as ex1:
    print("cannot do it :(")
    print(ex1)
except NameError:
    print("i dont know this name :(")
except:
    print("i dont know this error, sorry..")
