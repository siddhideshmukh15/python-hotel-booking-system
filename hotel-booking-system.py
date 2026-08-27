rooms = {
    "101": {"type": "Single", "price": 1000},
    "102": {"type": "Double", "price": 1800},
    "103": {"type": "Deluxe", "price": 3000}
}

bookings = {}
booking_count = 1

while True:
    print("\n===== Hotel Booking System =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. View Bookings")
    print("4. Search Booking")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== Available Rooms =====")

        for room_id, room in rooms.items():
            if room_id in bookings:
                status = "Booked"
            else:
                status = "Available"

            print(room_id, "-", room["type"], "- Rs.", room["price"], "-", status)

    elif choice == "2":
        room_id = input("Enter room number: ")

        if room_id not in rooms:
            print("Room not found!")

        elif room_id in bookings:
            print("Room is already booked!")

        else:
            name = input("Enter customer name: ")
            phone = input("Enter phone number: ")

            try:
                guests = int(input("Enter number of guests: "))
                nights = int(input("Enter number of nights: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            check_in = input("Enter check-in date: ")
            check_out = input("Enter check-out date: ")

            total = rooms[room_id]["price"] * nights

            print("\nPayment Methods:")
            print("1. UPI")
            print("2. Cash")
            print("3. Card")

            payment_choice = input("Choose payment method: ")

            if payment_choice == "1":
                payment_method = "UPI"
            elif payment_choice == "2":
                payment_method = "Cash"
            elif payment_choice == "3":
                payment_method = "Card"
            else:
                print("Invalid payment method!")
                continue

            payment_status = input("Enter payment status (Paid/Pending): ")

            booking_id = "B" + str(booking_count)
            booking_count += 1

            bookings[room_id] = {
                "booking_id": booking_id,
                "name": name,
                "phone": phone,
                "guests": guests,
                "check_in": check_in,
                "check_out": check_out,
                "nights": nights,
                "total": total,
                "payment_method": payment_method,
                "payment_status": payment_status
            }

            print("\n===== Booking Confirmed =====")
            print("Booking ID:", booking_id)
            print("Customer:", name)
            print("Room:", room_id)
            print("Guests:", guests)
            print("Check-in:", check_in)
            print("Check-out:", check_out)
            print("Nights:", nights)
            print("Payment Method:", payment_method)
            print("Payment Status:", payment_status)
            print("Total: Rs.", total)

    elif choice == "3":
        if not bookings:
            print("\nNo bookings found!")
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
                print("Payment Method:", booking["payment_method"])
                print("Payment Status:", booking["payment_status"])
                print("Total: Rs.", booking["total"])

    elif choice == "4":
        booking_id = input("Enter booking ID: ")
        found = False

        for room_id, booking in bookings.items():
            if booking["booking_id"] == booking_id:
                print("\n===== Booking Found =====")
                print("Booking ID:", booking["booking_id"])
                print("Customer:", booking["name"])
                print("Phone:", booking["phone"])
                print("Room:", room_id)
                print("Guests:", booking["guests"])
                print("Check-in:", booking["check_in"])
                print("Check-out:", booking["check_out"])
                print("Nights:", booking["nights"])
                print("Payment Method:", booking["payment_method"])
                print("Payment Status:", booking["payment_status"])
                print("Total: Rs.", booking["total"])

                found = True
                break

        if not found:
            print("Booking not found!")

    elif choice == "5":
        booking_id = input("Enter booking ID to cancel: ")
        found = False

        for room_id, booking in list(bookings.items()):
            if booking["booking_id"] == booking_id:
                del bookings[room_id]
                print("Booking cancelled successfully!")
                found = True
                break

        if not found:
            print("Booking not found!")

    elif choice == "6":
        print("\nThank you for using Hotel Booking System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")