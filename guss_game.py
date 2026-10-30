num=9
guss_count=0
guss_chance=3
while guss_count<guss_chance:
    guss=int(input("please guss what ever number you want: "))
    guss_count=guss_count+1
    if guss==num:
        print(f"wow! you are good at this, the num was really {num}")
        break
else:
    print("Sorry, try again!!")