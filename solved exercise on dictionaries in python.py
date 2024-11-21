# Muhammad Wasif Zawar               FA24-BBD-053(A)
#SOLVES EXERCISE ON DICTIONARIES IN PYTHON
#QUESTION 13 (a)
info = {"Name :": "Mozzam", "Age :" : "19", "City :" : "Lahore", "Hobby :" : "Book_Reading"}
for key,value in info.items():
    print(key ,value)

#(b)
text = input("Enter the text: ").lower()
words = text.split() 
frequencies = {} 
for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1
print("\nWord Frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")

#(c)
inventory = {}
print ("Store: S\nQuit : Q")
while True :
    product = input("ENTER YOUR PRODUCT NAME:")
    units   = int(input("ENTER NUMBER OF UNITS:"))
    option = input("ENTER S OR Q:").lower()
    inventory[product] = units
    if option == "q" :
        break
print(inventory)

#(d)
orders = [
    {"ProductCategory": "Electronics", "Quantity": 1},
    {"ProductCategory": "Clothing", "Quantity": 2},
    {"ProductCategory": "Electronics", "Quantity": 3},
    {"ProductCategory": "Books", "Quantity": 1},
    {"ProductCategory": "Clothing", "Quantity": 2},
    {"ProductCategory": "Books", "Quantity": 4}
]
category_totals = {}
for order in orders:
    category = order["ProductCategory"]
    quantity = order["Quantity"]
    category_totals[category] = category_totals.get(category, 0) + quantity
most_popular = max(category_totals, key=category_totals.get)
print("Category Totals:", category_totals)
print(f"Most Popular Product Category: {most_popular} ({category_totals[most_popular]} items sold)")

#(e)
grades = {}
n = int(input("Enter the number of students: "))
for _ in range(n):
    name = input("Enter the student's name: ")
    grade = float(input(f"Enter the grade for {name}: "))
    grades[name] = grade
average_grade = sum(grades.values()) / len(grades)
print("\nStudent Grades:")
for student, grade in grades.items():
    print(f"{student}: {grade:.2f}")
print(f"\nAverage Grade: {average_grade:.2f}")

#(f)
students = {}
def add_student():
    name = input("Enter student name: ")
    subjects = int(input(f"How many subjects for {name}? "))
    grades = {}
    for _ in range(subjects):
        subject = input("Enter subject name: ")
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade
    students[name] = grades
    print(f"Added {name} successfully!")
def calculate_averages():
    print("\nAverage Grades:")
    for name, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        print(f"{name}: {avg:.2f}")
def subject_grades():
    subject = input("Enter subject name: ")
    highest, lowest = None, None
    high_name, low_name = "", ""

    for name, grades in students.items():
        if subject in grades:
            grade = grades[subject]
            if highest is None or grade > highest:
                highest, high_name = grade, name
            if lowest is None or grade < lowest:
                lowest, low_name = grade, name

    if highest is not None:
        print(f"\n{subject} - Highest: {highest} ({high_name}), Lowest: {lowest} ({low_name})")
    else:
        print(f"No grades found for {subject}.")
def sort_students():
    averages = {name: sum(grades.values()) / len(grades) for name, grades in students.items()}
    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    print("\nStudents sorted by average grade:")
    for name, avg in sorted_students:
        print(f"{name}: {avg:.2f}")
while True:
    print("\n1. Add Student\n2. Calculate Averages\n3. Subject Grades\n4. Sort Students\n5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        calculate_averages()
    elif choice == "3":
        subject_grades()
    elif choice == "4":
        sort_students()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

#(h)
products = {"Apple": {"price": 2, "quantity": 10}, 
            "Banana": {"price": 1, "quantity": 20}, 
            "Milk": {"price": 3, "quantity": 5}}
cart = {}

def add_to_cart():
    """Add a product to the cart."""
    name = input("Enter product name: ").strip()
    if name in products:
        quantity = int(input(f"Enter quantity of {name}: "))
        if quantity <= products[name]["quantity"]:
            cart[name] = cart.get(name, 0) + quantity
            products[name]["quantity"] -= quantity
            print(f"{quantity} {name}(s) added to the cart.")
        else:
            print("Not enough stock available.")
    else:
        print("Product not found.")

def remove_from_cart():
    """Remove a product from the cart."""
    name = input("Enter product name to remove: ").strip()
    if name in cart:
        quantity = int(input(f"Enter quantity of {name} to remove: "))
        if quantity <= cart[name]:
            cart[name] -= quantity
            products[name]["quantity"] += quantity
            if cart[name] == 0:
                del cart[name]
            print(f"{quantity} {name}(s) removed from the cart.")
        else:
            print("You don't have that many in your cart.")
    else:
        print("Product not in the cart.")

def calculate_total():
    """Calculate the total cost, including discounts and taxes."""
    total = 0
    for name, quantity in cart.items():
        total += quantity * products[name]["price"]
    discount = total * 0.1  # 10% discount
    tax = total * 0.05     # 5% tax
    total_after_discount = total - discount
    total_with_tax = total_after_discount + tax
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Discount (10%): -${discount:.2f}")
    print(f"Tax (5%): +${tax:.2f}")
    print(f"Total: ${total_with_tax:.2f}")
def main():
    """Main menu for the shopping cart."""
    while True:
        print("\n1. Add to Cart\n2. Remove from Cart\n3. View Total\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_to_cart()
        elif choice == "2":
            remove_from_cart()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()