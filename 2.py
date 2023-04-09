choice = "-"
your_choice = input("> ")

while True:
    if your_choice == 0:
        break
    elif your_choice == '12345':
        print("your choice is {}".format(your_choice))
        break
    else:
        print("the entire list...")