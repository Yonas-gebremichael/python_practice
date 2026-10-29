weight=float(input("Please Enter your weight please " ))
kind=input("In which kind of mesurement do you want to know,"
           "To know your kg Enter k"
           " or to know your lbs enter l")

to_kilo=weight * 2.2
to_pound=weight /0.4

if kind.upper()=="L":
    print(f'Your weight in pound is {to_pound}lbs GG!')
elif kind.upper()=="k":
    print(f'your weight in kilo is {to_kilo} kg GG!')

else:
    print("invalid message")
