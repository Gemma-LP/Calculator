print("\n\nHi there!")
while True:
  jokechoice = int(input("Select a number for a joke from 1, 2 or 3. "))
  if (jokechoice ==1):
    print("Did you hear about the mathematician who was afraid od negative numbers...he would stop at nothing to avoid them.")
  elif (jokechoice ==2):
    print ("What does a nosey pepper do? Gets jalapeno business!")
  elif (jokechoice ==3):
    print("What do you call a parade of rabbits hopping backwards? A redeecding hare-line.")
  elif (jokechoice ==0):
    break
else:
  print("That's not a valid selection. Try again.")

def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply (x,y):
  return x * y
def divide(x, y):
  return x / y 
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
  choice = input("Enter your selection (1/2/3/4): ")
  if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice =='1': 
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice =='2': 
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice =='3':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice =='4':
      print(num1, "/", num2, "=", divide(num1, num2))
    break
  else:
    print("Invalid input")