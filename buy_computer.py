available_options = ["monitor",
                     "keyboard",
                     "CPU",
                     "Mouse",
                     "Mouse Mat",
                     "HDMI cable"
                     ]


current_choice = "-"        #initiating with a current choice that is not in 012345
computer_parts = []         #creating an empty list of the stuff that we want to buy

valid_choices = []          #the valid options that are available to buy
for i in range(1,len(available_options)+1):
    valid_choices.append(str(i))
print(valid_choices)
while current_choice != "0":
    if current_choice in valid_choices:

        index = int(current_choice)-1
        chosen_part = available_options[index]
        if chosen_part in computer_parts:
            #we already have it, hence we need to remove it
            print("Removing {} from the list".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {} to the list".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))


    else:
        print("Please enter options from the list below:")
        for index,part in enumerate(available_options):
            print("{}. {}".format(index+1, part))

    current_choice= input()
print(computer_parts)