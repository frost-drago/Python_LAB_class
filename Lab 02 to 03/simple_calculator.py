# The classic.
num_A = float(input("enter a number: "))
num_B = float(input("enter another number: "))
symbol = input("enter a symbol: ")

if symbol == '+':
    answer = num_A + num_B
elif symbol == '-':
    answer = num_A - num_B
elif symbol == '/':
    answer = num_A / num_B
elif symbol == '*':
    answer = num_A * num_B
elif symbol == '**':
    answer = num_A ** num_B
elif symbol == '%':
    answer = num_A % num_B
elif symbol == '//':
    answer = num_A // num_B
elif symbol == 'and':
    answer = num_A and num_B
elif symbol == 'or':
    answer = num_A or num_B
else:
    print("Symbol not accepted")
    answer = "N/A"
print(f"answer: {answer}")