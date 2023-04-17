print("Welcome to this script that does stuff that is absolutly not going to come handy to anyone! For information on the commands please type Help")

while True:
    print("Specify the commands you would like to choose. Type help for information on all commands ")
    command = input("> ")


    if command == "help":
        print('''
number      command
1           lower
2           capitalize
3           
4           
5           
6           
7           
8           
9           
10          
        ''')


    elif command =="word":
        print("Type your word here!")
        word = input("> ")
        if word.isdigit():
            print("only string")
        else:
            print("your specifications")
            word_command = input("> ")
            if word_command == "one":
                print(word.lower())  
            elif word_command == "two":
                print(word.capitalize())
            else:
                print("Can't understand m8")


    elif command =="print_pattern":
        print("Which pattern would you like")
        pattern_commad = input("> ")
        if pattern_commad == "square":
            n = 5
            for i in range(n):
                for j in range(n):
                    print("*", end="  ")
                print()
        if pattern_commad == "left triangle":
            n = 5
            for i in range(n):
                for j in range(i+1):
                    print("*", end="  ")
                print()
        else:
            print("sorry not added yet!")


    elif command == "quit":
        break
    else:
        print("sorry I couldnt understand your command")
    continue