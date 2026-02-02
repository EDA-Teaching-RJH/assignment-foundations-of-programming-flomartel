##Part B, the modular architechture 

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "La Forge"] ##names of startrek tng characters
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"] ##ranks of tng characters
    divs = ["Command", "Command", "Operations", "Security", "Operations"] ##divisions of tng characters
    ids = [1001, 1002, 1003, 1004, 1005] ##ids of tng characters. i made these up im not sure if they have actual ones

    return names, ranks, divs, ids ##exits function and stores data

def display_menu(user_name): ##defines the display menu. user selects from here
    print ("Welcome to the ship's personnel management system!")
    print ("Current log in: ", user_name) ##ADD SOMETHING HERE

    print ("1. Add Member")
    print ("2. Remove Member")
    print ("3. Update Rank")
    print ("4. Display Roster")
    print ("5. Search Crew")
    print ("6. Search by Division")
    print ("7. Calculate Payroll")
    print ("8. Search Officers")

    opt = input("Select Option: ") ##prints select option and user inputs number
    return opt

def add_member(names, ranks, divs, ids):
    new_name = input("Enter new member's name: ")
    new_rank = input("Enter new member's rank: ")
    new_div = input("Enter new member's division: ")
    new_id = input("Enter new member's ID number: ") ##asks user for new name,rank,division,id number

    valid_TNG_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    if new_rank not in valid_TNG_ranks:
        print("Please enter a valid TNG rank") ## if rank given isnt one of the listed it will prompt for another rank
        return

    if new_id in ids:
        print("Please enter a new and correct ID number") ##if id is already in use it will prompt for a different number
        return

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id) ##adds new crew member to the roster list
    print("New crew member added.")   


##tomorrow do def remove_member()

    def main(): ##defines main function. call everything from inside here
        names, ranks, divs, ids = init_database() ## calls init_database inside main and retuns the 4 lists
        user_name = input("What is your full name? ")
        

        active = True
        while active:
             opt = display_menu(user_name)

             if opt == "1":
                 add_member(names, ranks, divs, ids)

            ##elif opt 2 remove_member()




    main()