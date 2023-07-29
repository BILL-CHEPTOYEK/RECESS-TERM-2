
import Bill_Cheptoyek_afternoon
print(Bill_Cheptoyek_afternoon.square(5))

from math import sqrt
print(sqrt(25)) 

print("++++++++++++++++++++++++++++++++++++++++++++++++")
# input and output(example 1)
def send_message():
    message = input("Enter your message: ")
    print("Message sent:{message}")

def receive_message():
    sender = input("Enter the sender's name: ")
    message = input("Enter the message: ")
    print("Message received from", sender + ":", message)

# Main program
print("Welcome to the messaging app!")
print("1. Send a message")
print("2. Receive a message")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    send_message()
elif choice == "2":
    receive_message()
else:
    print("Invalid choice!")

# input and output(example 2)
# Dictionary containing plot details
print("++++++++++++++++++++++++++++++++++++++++++++++++")
plot_details = {
    "P000": {"owner": "Bill", "for_sale": True,"number": "0785521231", "Location": {"District":"Mbale","street":"123_half_london"}},
    "P001": {"owner": "Johnny walker", "for_sale": True,"number": "0785555231", "Location": {"District":"Mukono","street":"231_nabuti"}},
    "P002": {"owner": "Jane Smith", "for_sale": False,"number": "0785347273", "Location": {"District":"Jinja","street":"161_Jinja_College_road"}},
    "P003": {"owner": "Robert debuk", "for_sale": True,"number": "0785560157", "Location": {"District":"Kapchorwa","street":"891_senior_quaters"}},
}

def get_plot_details(plot_number):
    if plot_number in plot_details:
        details = plot_details[plot_number]
        owner = details["owner"]
        for_sale = details["for_sale"]
        location = details["Location"]
        Number = details["number"]
        if for_sale:
            sale_status = "is for sale"
            print(f"Contact: {number}")
        else:
            sale_status = "is not for sale"

        print(f"Plot Number: {plot_number}")
        print(f"Owner: {owner}")
        print(f"Location: {location}")
        maps_url = f"https://www.google.com/maps/search/?api=1&query={location}"
        print(f"Google Maps: {maps_url}")
        print(f"Sale Status: {sale_status}")
    else:
        print("Invalid plot number")

# Main program
plot_number = input("Enter plot number: ")
get_plot_details(plot_number)
