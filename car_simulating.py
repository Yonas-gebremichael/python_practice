command=""
while True:
     command=input("> ").lower()
     if command=="start":
         print("the car started, ready to go")
     elif command=="stop":
         print("The car has become to end")
     elif command=="help":
         print("""
start -  to start the car
stop- to stop the car
quit - to exit the simlation""")
     elif command=="quit":
         break

     else:
         print("the simulation can't work with this command")





