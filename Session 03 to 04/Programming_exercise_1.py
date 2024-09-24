print("Enter your height.")
user_height = float(input())
suggested_board_length = user_height * 0.88
user_height_feet = user_height // 30.48  # 1 feet is 30.48 cm
user_height_inch = (user_height % 30.48) // 2.54  # 1 inch is 2.54 cm
print(f"Feet: {user_height_feet}")
print(f"Inches: {user_height_inch}")
print(f'Suggested board length: {suggested_board_length:.4f} cm')