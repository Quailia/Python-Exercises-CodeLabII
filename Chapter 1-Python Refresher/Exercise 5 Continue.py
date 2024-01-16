loop_count = 0

while True:
    user_input = input("Do you want to continue? (Y/N): ").upper()
    loop_count += 1
    if user_input != 'Y':
        break  

print(f"The loop was executed {loop_count} times.")
