def reqInput(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("!!!! This Field is REQUIRED. Please try again.")
