# File and exception handling
# you should a file called receipt.txt 
def write_receipt():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))

    try:
        with open("receipt.txt", "a") as file:
            file.write(f"{item}: {price}\n")
        print("Receipt entry added successfully.")
    except FileNotFoundError:
        print("Receipt file not found.")
    except PermissionError:
        print("Permission denied. Unable to write to the receipt file.")
    except IOError as e:
        print("An error occurred while writing the receipt:", e)

def read_receipt():
    try:
        with open("receipt.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Receipt file not found.")
    except PermissionError:
        print("Permission denied. Unable to read the receipt file.")
    except IOError as e:
        print("An error occurred while reading the receipt:", e)
print("================================================ ")


def generate_total_price():
    try:
        total_price = 0.0
        with open("receipt.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    _, price = line.split(":")
                    total_price += float(price)
        print("Total Price:", total_price)
    except FileNotFoundError:
        print("Receipt file not found.")
    except PermissionError:
        print("Permission denied. Unable to read the receipt file.")
    except ValueError:
        print("Invalid price format found in the receipt.")
    except IOError as e:
        print("An error occurred while calculating the total price:", e)


write_receipt()
write_receipt()
write_receipt()
read_receipt()
generate_total_price()
print("*************************************************")
