#!/usr/bin/python3

from map import rooms #importing rooms from map.py
from player import * # importing * (all files) from player.py
from items import * #importing everything from items.py
from gameparser import * # importing all values from gameparser



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    itemsinventory="" #creating a new variable , items iventory, that will hold the comma list of the inventory items
    i=0 #declaring the variable i which will be incremented through the for loop
    for key in items: #for loop , which will loop for each key in the items dictionary in list.py, imported in line 2 
    	if i> 0: # if statment , which should be true after first iteration, as i is incremented by 1 each time but starts at 0.
    		itemsinventory = itemsinventory + ", " + key["name"] # for each iteration, the variable itemsiventory has the name added to the string from the items list, with a comma after it each time
    		i=i+1 # i incremented
    	else:
    		itemsinventory = itemsinventory + key["name"] # same as the above statment, but no comma added - this is to make sure that there are no trailing or leading commas
    		i=i+1 # i incremented
    return itemsinventory # at the end of the function the variable items inventory is returned.

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if str(list_of_items(room["items"])) != "": # initially had errors , so worked out needed if statement that says only to print if the list of items....
    # ...doesnt return a blank value(!=""), as if it does then the print function will not work. Also this means the blank line will not be printed as well if empty list

    	print("There is " + list_of_items(room["items"]) + " here." ) #prints there is, followed by the comma seperated list from list of items and then finally the string "here"
    	print() # as per the spec, a blank line is then printed also


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    print("You have "+ list_of_items(items)+".") # prints the string "you have", followed by the result of the function list of items...
    #.. this time using the items variable , where in the previous function using the items held within the room and not the inventory...#
    #Finally ends with a full stop to pass doctest
    print() # as per spec , blank line printed
   

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print() #prints blank line
    print(room["name"].upper()) #prints the name of the room from map  , in upper case using the .upper function.
    print() #prints blank line
    print(room["description"]) # Display room description
    print() #prints blankline
    #above was existing code
    print_room_items(room) # the print room items function is called here , which will print the items in the room...
    #.. according to the syntax as defined by the function, meaning also the final blank like will be printed by the function also.
        
def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"] # returns name of room that exit leads to from dictonary


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")# prints the string go, then in upper case the direction then the leads_to followed by .


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """

    print("You can:") #prints you can

    for direction in exits: # for loop for all avaialble exit directions
        
        print_exit(direction, exit_leads_to(exits, direction)) # Print the exit name and where it leads to


    for item in room_items: # for loop that iterates for each item in the room items list
    	print("TAKE " + item["id"].upper() +" to take " + item["name"] + ".")
    #prints "take" , followed by the name of the item - in capitals due to the .upper function , then the string to take , then the full description, followed by full stop
    for item in inv_items: # for lopp that iterates for each item in the inventory of the player, so same as above just different list as drop rather than take
    	print("DROP " + item["id"].upper() + " to drop your " + item["name"] + ". ")
    #prints drop, followed by the name of the item in capitals, then the string to drop your, followed by the full description name from thr dictionary and followed by a .
    print()#print blank line
    print("You are carrying a total of " + str(round(mass, 2)) + 'kg') #prints the string "you are caryying a total of". Then the mass and then adds kg to the end
    #mass is made a string so it can be concenated together , as only string can be done this way. The round function is used or else the mass would be too long in terms of decimals...
    #... the 2 signifiying that it will be shown only with only 2 numbers .
    print("What do you want to do?") #prints what do you want to do 


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits # checks if valid exit, code pre-exisiting


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room # global variable current_room needed for execute_go function

    exits= is_valid_exit(current_room["exits"], direction) #exits updated to valid exit list from is valid exit function
    if exit:
    	current_room= move(current_room["exits"], direction)  # current room updated to allow player movement , if its valid from above if statement
    else:
    	print("You cannot go there.")#prints you cannot go there, as per spec due to the if statement failing as its not a valid exit. 


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    global current_room #global variable of current room needed for function
    global inventory #inventory needed for function
    global items #items needed for function
    global mass #mass needed for function
    try: #try is a way of error handling , as its possible the user can type an invalid option. so the below code is executed, if not then the except will be run
        item_in_room = items[item_id] # the items in room equals the list of items IDs
        if (mass + item_in_room['mass']) > max_weight: # this if statment relates to the mass , so if the mass of the item being taken is larger than the max weight set in items.py, then the user will be told they cannot do this
            print('\nYou cannot carry that much') # prints blank line, then the statement that they cannot carry that much weight as per spec.

        else: # if statment failure, meaning there is no weight issues 
            if current_room['items']: # if the item the user wants to take is in that room 
                items_lst = current_room['items'] # then the items list is updated to the current room item

                if item_in_room not in items_lst: # if item user wants to take is not in the avaialble items list for room.
                    print('You cannot take this')  # user is told they cannot take this item , since it is not in that room

                for item in items_lst: #for loop for each item in the item list ,which are what are being taken from the room
                    if item == item_in_room: # if statement for if the item is in the item in room list
                        inventory.append(item) # the user inventory is appended to include the newly added item
                        current_room['items'].remove(item) # the current room items is appended so that the item that has been added to the inventory , is removed from this list
                        mass += item_in_room['mass'] # the total mass is then updated to include the newly added items mass (=+ means mass = mass + 1)

    except KeyError:
    	print("Not possible") # if the try fails, the except runs printing out not possible as the input cannot be run. 
   

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global current_room # current room needed for this function
    global inventory # iventory needed for this function
    global mass # mass needed for this function

    try: # as with the take function(this is just reverse), the try statement is used
        item_to_drop = items[item_id] #items to drop set to items 
        if mass < 0:
            print('\nYou cannot drop that much') # if the mass is going to be less than 0 , then prints string saying you cannot drop that much

        else:
            if inventory:
                inv_lst = inventory #inventory list set to inventory

                if item_to_drop not in inventory: # if the item the user wants to drop is not in the players inventory
                    print('You cannot drop this') # the string you cannot drop this is printed

                for item in inv_lst: # for loop that iterates for each item within the inventory list
                    if item == item_to_drop: # if the item the user wants to take is the item in the list
                        current_room['items'].append(item) # then the current room item list is appended to include the dropped item
                        inventory.remove(item) # the inventory for the player has this item removed from the list
                        mass -= item_to_drop['mass'] # the mass is then updated by taking away the mass of the dropped item (-=)

            else:
                print("You cannot drop that.") # if the item is not in the list, the user is told they cannot drop it
    except KeyError:
        print('I dont\'t quite understand') # if the try fails due to key error, then this message is printed to the user.

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input # returns normalised input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]] # avaiable exits


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        if items["laptop"] in rooms["Tutor"]["items"]: # victory / end statment that means that if the item laptop is in the list of items in the tutor room, then the game will be won and the main game loop broken. as the item isnt there originally, the user will have to drop it here
        	print("You have turned in the lost laptop and won!") #prints out several victory statements
        	print("Well Done!")
        	print("You legend")
        	print("Worth a First")
        	print("Defo passed this module")
        	print("Congrats Again!")
        	input("Press any key to quit") # allows the user to exit, and also means the window for python will remain open and not close
        	break # ends game 
        print_room(current_room) #existing code
        print_inventory_items(inventory) #existing code

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

