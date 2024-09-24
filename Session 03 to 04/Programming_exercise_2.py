print("Enter the mass in kg and the force in N: ", end="")
user_input = eval(input())
if len(user_input) != 2 :
    print("Fuck no.")
else:
    mass, force = user_input
    print(f"The acceleration is {force / mass}")