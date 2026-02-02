##Part B, the modular architechture 

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "La Forge"] ##names of startrek tng characters
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"] ##ranks of tng characters
    divs = ["Command", "Command", "Operations", "Security", "Operations"] ##divisions of tng characters
    ids = [1001, 1002, 1003, 1004, 1005] ##ids of tng characters. i made these up im not sure if they have actual ones

    return names, ranks, divs, ids ##exits function and stores data

def display_menu():
    print ("Welcome to the ship's personnel management system!")
    print ("Current log in: -------") ##ADD SOMETHING HERE

    print ("1. Add Member")
    print ("2. Remove Member")
    print ("3. Update Rank")
    print ("4. Display Roster")
    print ("5. Search Crew")
    print ("6. Search by Division")
    print ("7. Calculate Payroll")
    print ("8. Search Officers")

    opt = input("Select Option: ")
    return opt


    def main():
        if opt == "1":
            

