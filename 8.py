#loops(while,for, do while)
#while loop
i=1
while i <= 5:
    print(i)
    i+=1

#use break
sheep_count=1
while sheep_count <= 19:
    print(f"sheep {sheep_count}")
    if sheep_count==5:
        print("thats enough")
        break
    sheep_count+=1


#continue
sheep_count=1
while sheep_count <= 19:
    if sheep_count==5:
        sheep_count+=1
        continue
    print(f"sheep {sheep_count}")
    sheep_count+=1


    
#using while loop for user input
pin=" "
currect_pin="1234" 
while pin != currect_pin:
    pin=input("Enter your pin:")
    if pin != currect_pin:
        print("incurrect pin.try again")
print("pin accepted you can proceed")

#basic counting with while loop
i=1
while i <= 10:
    print(i)
    i+=1

#odd number printer
i=1
while i < 20:
    if i%2 !=0:
        print(i)
    i+=1

#ticket booking simulation
bus_seats=8
while bus_seats > 0:
    print(f" {bus_seats} seat available")
    booking=input("do you want to book a seat? (yes/no):").lower()

    if booking=="yes":
        bus_seats-=1
        print("seat booked")
    else:
        print("no booking mode")
print("all seats are booked")

#countdown timer
i=10
while i >=1:
    print(i)
    i-=1