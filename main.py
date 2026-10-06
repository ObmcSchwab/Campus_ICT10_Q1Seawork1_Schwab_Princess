from pyscript import display, document

# Variables
name = "Princess"  # string
age = 17           # int
height_cm = 160.2  # float
travel_list = ["France", "Italy", "Greece"]  # list
is_new_student = True  # boolean
profile = {
    "color": "Navy Blue",
    "car_brand": "Toyota",
    "shoe_size": "37",
    "best_friend": "Therese"
}  # dictionary
fruits = {"apple", "orange", "kiwi", "pineapple", "strawberry"}  # set
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")  # tuple

# Display variable types
display("📌 Variable Types:", target="types")
display(type(name), target="types")
display(type(age), target="types")
display(type(height_cm), target="types")
display(type(travel_list), target="types")
display(type(is_new_student), target="types")
display(type(profile), target="types")
display(type(fruits), target="types")
display(type(weekdays), target="types")

# Arithmetic functions
def add(e):
    document.getElementById("result").innerHTML = ""
    n1 = float(document.getElementById("num1").value)
    n2 = float(document.getElementById("num2").value)
    display(f"➕ Sum: {n1 + n2}", target="result")

def subtract(e):
    document.getElementById("result").innerHTML = ""
    n1 = float(document.getElementById("num1").value)
    n2 = float(document.getElementById("num2").value)
    display(f"➖ Difference: {n1 - n2}", target="result")

def multiply(e):
    document.getElementById("result").innerHTML = ""
    n1 = float(document.getElementById("num1").value)
    n2 = float(document.getElementById("num2").value)
    display(f"✖ Product: {n1 * n2}", target="result")

def divide(e):
    document.getElementById("result").innerHTML = ""
    n1 = float(document.getElementById("num1").value)
    n2 = float(document.getElementById("num2").value)
    if n2 != 0:
        display(f"➗ Quotient: {n1 / n2}", target="result")
    else:
        display("⚠ Cannot divide by zero!", target="result")
