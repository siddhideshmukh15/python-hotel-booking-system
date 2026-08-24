rooms ={
    "101":{"type":"Single","price":1000},
    "102":{"type":"Double","price":1800},
    "103":{"type":"Delux","price":3000}
    }

bookings ={}
booking_count= 1

while True:
    print("\n === Hotel Booking System===")
    print("1. view Rooms")
    print("2. Book Rooms")
    print("3. View Bookings")
    print("6. Search bookings")
    print("5. Cancel Bookings")
    print("6. Exit")
    
    Choice = input("Enter your choice:")
    
    if Choice =="1":
        print("\n Available Rooms:")
        
        for room_id, room in rooms.items():
            if room_id in bookings:
                status ="Booked"
            else:
                status = "Available"
                
                print(room_id,"-",room["type"],
                "- rs", room["price"], "_",status)
                
    elif Choice =="2":
        room_id = input("Enter room number:")
        
        if room_id not in rooms:
            print("Room not found!")
            
        
        elif room_id in bookings:
            print("Room is already booked successfully!")
                
            
        else:
            name= input("Enter customer name:")
            phone= input("Enter phone number:")
            guests=int(input("Enter number of guests:"))
            check_in= input("Enter check-in date:")
            check_out = input("Enter check-out date: ")
            nights = int(input("Enter number of nights: "))
            
            total = rooms[room_id]["price"] * nights
            
            booking_id = "B"+ str(booking_count)
            booking_count+=1
            
            bookings[room_id]={
                "booking_id": booking_id,
                "name":name,
                "phone":phone,
                "guests":guests,
                "check_in": check_in,
                "check_out": check_out,
                "nights": nights,
                "total": total
            }
            
            print("\n === Booking confirmed===")
            print("Booking ID:", booking_id)
            print("Customer:",name)
            print("Room:", room_id)
            print("Guests:", guests)
            print("Nights:", nights)
            print("Total: rs", total)
            
    elif Choice == "3":
        if not bookings:
            print("No bookings found!")
        else:
            print("\n===== View Bookings =====")

        for room_id, booking in bookings.items():
            print("\nBooking ID:", booking["booking_id"])
            print("Customer:", booking["name"])
            print("Phone:", booking["phone"])
            print("Room:", room_id)
            print("Guests:", booking["guests"])
            print("Check-in:", booking["check_in"])
            print("Check-out:", booking["check_out"])
            print("Nights:", booking["nights"])
            print("Total: ₹", booking["total"])
                
    elif Choice =="4":
        booking_id= input("Enter booking ID:")
        found = False
        
        for room_id, booking in bookings.items():
            if booking["booking_id"] == booking_id:
                print("\n Booking Found!")
                print("Customer:", booking["name"])
                print("Room:", room_id)
                print("Guests:",booking["guests"])
                print("Total: rs",booking["total"])
                found= True
        if not found:
            print("Booking not found!")
            
    elif Choice =="5":
        booking_id=input("Enter booking ID to cancel:")
        found=False
        
        for room_id, booking in list(bookings.items()):
            for room_id, booking in bookings.items():
             if booking["booking_id"] == booking_id:
        
                print("Booking cancelled successfully!")
                found = True
                
            
            if not found:
                print("Booking not found!")
                
    elif Choice =="6":
        print("Thank you for using Hotel Booking System!")
        break
    
    else:
        print("Invalid choice!")
        
            
                
        
    