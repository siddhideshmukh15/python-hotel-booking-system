rooms ={
    "101":{"type":"Single","price":1000},
    "102":{"type":"Double","price":1800},
    "103":{"type":"Delux","price":3000}
    }

bookings ={}

while True:
    print("\n === Hotel Booking System===")
    print("1. view Rooms")
    print("2. Book Rooms")
    print("3. View Bookings")
    print("4. Cancel Bookings")
    print("5. Exit")
    
    Choice = input("Enter your choice:")
    
    if Choice =="1":
        for room_id, room in rooms.items():
            if room_id in bookings:
                status ="Booked"
            else:
                status = "Available"
                
                print(room_id,"-",room["type"],
                "- rs", room["price"], "_",status)
                
    elif Choice =="2":
        room_id = input("Enter room number:")
        
        if room_id in rooms:
            if room_id not in bookings:
                name = input("Enter customer name:")
                bookings[room_id] = name
                print("Room booked successfully!")
            
            else:
               print("Room is already booked!")
               
        else:
            print("Room not found!")
            
    elif Choice == "3":
        if not bookings:
            print("No bookings found!")
            
        else:
            for room_id, name in bookings.items():
                print("Room:",room_id,"customer:",name)
                
    elif Choice =="4":
        room_id = input("Enter room number to cancel:")
        
        if room_id in bookings:
            del bookings[room_id]
            print("Booking cancelled!")
            
        else:
            print("Booking not found!")
            break
        
    else:
        print("Invalid choice!")
        
print("Thank you! visit again.")
            
                
        
    