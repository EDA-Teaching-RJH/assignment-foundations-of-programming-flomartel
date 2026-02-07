##Part B, the modular architechture 

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "La Forge"] ##names of startrek tng characters
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"] ##ranks of tng characters
    divs = ["Command", "Command", "Operations", "Security", "Operations"] ##divisions of tng characters
    ids = [1001, 1002, 1003, 1004, 1005] ##ids of tng characters. i made these up im not sure if they have actual ones

    return names, ranks, divs, ids ##exits function and stores data

def display_menu(user_name): ##defines the display menu. user enters number and selects from here
    print ("Welcome to the ship's personnel management system!")
    print ("Current log in: ", user_name) ##sets current login as the input asked in main() line 76

    print ("1. Add Member")
    print ("2. Remove Member")
    print ("3. Update Rank")
    print ("4. Display Roster")
    print ("5. Search Crew")
    print ("6. Search by Division")
    print ("7. Calculate Payroll")
    print ("8. Search Officers")
    print ("9. Exit") ## ^ list of options

    opt = input("Select Option: ") ##prints select option and user inputs number
    return opt

def add_member(names, ranks, divs, ids):
    new_name = input("Enter new member's name: ")
    new_rank = input("Enter new member's rank: ")
    new_div = input("Enter new member's division: ")
    new_id = int(input("Enter new member's ID number: ")) ##asks user for new name,rank,division,id number

    valid_TNG_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
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


def remove_member(names, ranks, divs, ids):
    rem = int(input("Enter ID number to remove: ")) #promts user to enter ID number

    if rem in ids: #if the entered ID number is present it looks through the lists
        idx = ids.index(rem)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx) #removes member from every list to keep all lists in sync
        print ("Member removed.")
    else:
        print("ID number not in list. Please try again.") #prompts user to try again if ID isnt found

def update_rank(names, ranks, ids):
    update_ID = int(input("Enter ID number to update: "))
    if update_ID in ids: #finds member by ID number
        idx = ids.index(update_ID)
        updated_rank = input("Please input updated rank: ") ##here put in segment from lines 33-36, valid rank list
        ranks[idx] = updated_rank
        print("Rank updated.")

def display_roster(names, ranks, divs, ids):
    print("Current Roster: ")

    for i in range(len(names)):
        print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + str(ids[i])) ## prints a list of all crew members. had to turn ids to str to print

def search_crew(names, ranks, divs, ids):
    search_term = input("Enter name to search for crew member: ")
    for i in range(len(names)):
        if search_term.lower() in names[i].lower(): ##looks for name given by user. changed to .lower so can be put in lower case
            print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + str(ids[i])) ##prints list of crew member given

def filter_by_division(names, divs):
    div_name = input("Enter division name: ") ##promps user for division name
    match div_name:
        case "Command" | "Operations" | "Security" | "Sciences": ##all the possible divisions
            for i in range(len(names)):
                if divs[i] == div_name: ##looks for names under specified division
                    print(names[i]) ##prints names listed under that division

def calculate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Captain":
            total = total + 1000
        elif rank == "Commander":
            total = total + 700
        elif rank == "Lt. Commander":
            total = total + 500
        elif rank == "Lieutenant":
            total = total + 350
        elif rank == "Ensign":
            total = total + 200

    return total

def count_officers(ranks):
    



def main(): ##defines main function. call everything from inside here
        names, ranks, divs, ids = init_database() ## calls init_database inside main and retuns the 4 lists
        user_name = input("What is your full name? ") ##asks user for name, is displayed in 'display menu' at start
        

        active = True
        while active: ##sets while loop
            opt = display_menu(user_name)

            if opt == "1":
                add_member(names, ranks, divs, ids) ##if user selects "1", this function is called from inside main
            elif opt == "2":
                remove_member(names, ranks, divs, ids)
            elif opt == "3":
                update_rank(names, ranks, ids)
            elif opt == "4":
                display_roster(names, ranks, divs, ids)
            elif opt == "5":
                search_crew(names, ranks, divs, ids)
            elif opt == "6":
                filter_by_division(names, divs)
            elif opt == "7":
                total = calculate_payroll(ranks)
                print("Total cost of current crew:",total) ##prints total cost of crew


            elif opt == "9":
                break ## stops running, exits
             
                 
##remember to break while loop, probably add another option to display menu for exit

main()