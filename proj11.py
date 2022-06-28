"""
    This project will take our data from the pokemon pyfile and
    also our csv files, and will be used to simulate a 1 on 1 pokemon battle!
"""
import csv
import random
from random import randint
from random import seed
from copy import deepcopy
from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen

element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================

def open_file(filename):
    '''This function will return a file pointer after taking a filename '''
   
    FileFound=False

    while FileFound==False:
            
        try:
           fp = open(filename)
           return fp
       #try-except for the filenotfound error incase the file does not exist
        except FileNotFoundError:
           break

def read_file_moves(fp):  
    '''This function takes in the file pointer created from opening the 
    moves.csv file and returns a list of move objects. We use csv.reader
    to navigate the csv file provided.'''

    reader=csv.reader(fp) 
    next(reader, None)
    #Skip line

    Move_List=[]
    #empty list to append
    
    for i in reader:
        
        if i[2]!='1':
            #generation ID column does not equal 1, don't add
            continue
        
        if i[9]=='1':
            #attaxk type
            continue
        
        if i[4] and i[6]:
            
            name_value=i[1]
            #name
            element_value=element_id_list[int(i[3])]
            #type id
            power_value=int(i[4])
            #must make int for next 3 because they are numerical values
            accuracy_value=int(i[6])
            
            attack_type_value=int(i[9])
            
            moves=Move(name_value, element_value, power_value, accuracy_value, attack_type_value)
            #Order of items we need
            
            Move_List.append(moves)
            #We will append the object to our main empty list and return it

    return Move_List
        
def read_file_pokemon(fp):
    '''This function will take in the file pointer created from opening the pokemon.csv file 
    and returns a list of pokemon objects.  In this function, we first skip the 
    header line, then iterate through each line of the file creating a pokemon object
    with the contents of the line and adding that pokemon object to the list of pokemon.
    If the Generation column is not equal to 1, we ignore the line '''
  
    Poke_List=[]
    ID_List=[]

    reader=csv.reader(fp) 
    next(reader, None)
    #skip line

    for line in reader:
        
        id_value=int(line[0])
        #2 lines may have same value
        name_value=line[1].lower()
        generation_id=int(line[11])
        element1_value=line[2]
        element2_value=line[3]
        #setting our values at the proper indeces

        hp_value=int(line[5])
        patt_value=int(line[6])
        pdef_value=int(line[7])
        satt_value=int(line[8])
        sdef_value=int(line[9])
        
        if generation_id==1 and id_value not in ID_List:
            #If generation column is 1, we do not ignore the line
              ID_List.append(id_value)
              poke=Pokemon()
              poke.__init__(name =name_value.lower(), element1 =element1_value.lower(), element2 =element2_value.lower(), moves = None,
                 hp = hp_value, patt = patt_value, pdef =pdef_value, satt = satt_value, sdef = sdef_value)
              Poke_List.append(poke)
              #append the Pokemon object we created to the list

    return Poke_List

def choose_pokemon(choice,pokemon_list):
    '''This function will take a user input called choice as a string and the list of available pokemon.
    If the user input is an integer, the integer becomes the index for selecting a pokemon from the
    pokemon_list and a deepcopy of the pokemon object at that index is returned. If the input is a string,
    then we compare it to the name attribute of the pokemon in the list and if a name
    matches then a deepcopy of the pokemon object with that name is returned. If the index is out
    of range or the string is not found, then None is returned. '''
  
    try:
        if choice.isdigit():
            #If the choice is a number
            
            choice = int(choice)
            return deepcopy(pokemon_list[choice-1])
        #return the deep copy with the index subtracted by 1
        elif type(choice) == str:
            #if the choice is a string
            for i,pokemon in enumerate(pokemon_list):
                #enumerate the list to simplify
                if pokemon.get_name() == choice:
                    #if the name got from the list matches the choice, we return the deep copy
                    return deepcopy(pokemon_list[i])
        return None
    except IndexError:
        #if index not found
        
        return None

def add_moves(pokemon,moves_list):
    '''This function will add one random move to the pokemon's move list, then 
    adds three more moves that match one of the elements of this pokemon. Each move 
    will be added using this pokemon's object's add move method.  We will find the first
    random move using a random integer to index the moves_listparameter.  Then we will get 
    three more random moves from moves_list, and add them to this pokemon only if 
    the random move’s element matches either element1 or element2 of this pokemon and
    the move is not already in this pokemon's move list '''
    
    rand_idx = randint(0, len(moves_list)-1) 
    #random int to index 
    
    pokemon.add_move(moves_list[rand_idx])
    #we will add the random index
    tot_attempts=0
    found_moves=0
    #counter values initialized

    while found_moves<3:
        #less than 3 moves
          rand_idx = randint(0, len(moves_list)-1)
          move_check=moves_list[rand_idx]
          move_element=move_check.get_element()
          #need to check element

          if (move_element==pokemon.get_element1().lower()) or (move_element==pokemon.get_element2().lower()):
              if move_check not in pokemon.get_moves():
                  #if not in the pokemons moves     
                  pokemon.add_move(move_check)
                  #we add the move we checked and increase the counter
                  found_moves+=1
  
          tot_attempts=tot_attempts+1
          if tot_attempts > 200:
              #If attempts greater then 200 total
              return False
    return True

def turn (player_num, player_pokemon, opponent_pokemon):
    '''This function is looking for a player number 1 or 2, and the
    player and opponent's pokemon are of type Pokemon. This function will
    return true or false depending on the outcome of the turn, and eventually
    the battle'''
    #Print Player's 1 turn
    print('Player {}’s turn'.format(player_num))
    player_pokemon_string=player_pokemon.__str__()
    #the players pokemon will be a stringn displayed
    print(player_pokemon_string)
    print("Show options: 'show ele', 'show pow', 'show acc'")
    #show the options
    selection=input("Select an attack between 1 and 4 or show option or 'q': ")
    while (selection!='q'):
        #while they continue rather than quit
        if selection=='show pow':
           player_pokemon.show_move_power()
        elif selection=='show acc':
           player_pokemon.show_move_accuracy()
        elif selection=='show ele':
           player_pokemon.show_move_elements()
           #show the selections if they want to see options
           
        elif selection.isdigit():
            #if the selection is a number
            if int(selection)>0:
                #greater than 0
                
                attack_choice=player_pokemon.choose(int(selection))
                print("selected move:",attack_choice.name)

                print("{} hp before:{}".format(opponent_pokemon.name,opponent_pokemon.hp))
           
                player_pokemon.attack(attack_choice,opponent_pokemon)
                #we use the attack method here
           
                print("{} hp after:{}".format(opponent_pokemon.name,round(opponent_pokemon.hp)))
                #Print the hp after the attack
                print()
                if opponent_pokemon.hp==0:
                    #if their hp falls to 0, they faint
                    player_fainted=0
                    player_won=0
                    if player_num==2:
                        player_fainted=1
                        #if the player 1 pokemon faints or vice versa, we declare the winner!
                        player_won=2
                    elif player_num==1:
                        player_fainted=2
                        player_won=1
                  
                        print('Player {}''s pokemon fainted, Player {} has won the pokemon battle!'.format(player_fainted,player_won))
                        return False
        
                else:
                    return True
        print("Show options: 'show ele', 'show pow', 'show acc'")
        selection=input("Select an attack between 1 and 4 or show option or 'q': ")
        #relooping

def main():
    '''The main function will simulate a 1-on-1 battle between 2 opponents' pokemon.
    We add the relevant moves to the respective list by caling the read file functions.
    Then, we ask the user if they would like to have a pokemon battle, and prompt until a valid
    choice is entered. The player will then pick a pokemon and so will the other player.
    Then, they will each pick a move, unless the first move knocks the pokemon out.
    If the pokemon is damaged or not damaged, we print the hp after the attack, and 
    if the move was effective. We do this through the attack method in the pokemon file.
    If someone faints the other's pokemon, we declare a winner, or if the player quits
    we end the battle.'''
        
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
        
    while usr_inp=='y':
        fp=open_file('moves.csv')
        #open and read the moves files
        Move_List=read_file_moves(fp)
        fp=open_file('pokemon.csv')
        #open and read the pokemon file
        Poke_List=read_file_pokemon(fp)

        player_pokemon=''
        opponent_pokemon=''
        #empty strings to add whichever pokemon the users pick

        choice=input("Player {}, choose a pokemon by name or index: ".format(1))

        valid_pokemon=False
        while valid_pokemon==False:
            player_pokemon=choose_pokemon(choice,Poke_List)
            try:
                if player_pokemon.name=='':
                   choice=input("Player {}, choose a pokemon by name or index: ".format(1))
                   #if they enter an empty string
                else:
                   valid_pokemon=True
                   #if the pokemon entered was valid
            except:
                choice=input("Player {}, choose a pokemon by name or index: ".format(1))
            
        print("pokemon1:\n")
        
        player_pokemon_string=player_pokemon.__str__()
        #need the string of the pokemon
        print(player_pokemon_string)       

        Found_Move=add_moves(player_pokemon,Move_List)
        #if the move found

        choice=input("Player {}, choose a pokemon by name or index: ".format(2))

        valid_pokemon=False
        while valid_pokemon==False:
            opponent_pokemon=choose_pokemon(choice,Poke_List)
            try:
                if opponent_pokemon.name=='':
                   choice=input("Player {}, choose a pokemon by name or index: ".format(2))
                else:
                   valid_pokemon=True
            except:
                choice=input("Player {}, choose a pokemon by name or index: ".format(2))
                #repeat steps for player one for player two

        print("pokemon2:\n")
        player_pokemon_string=opponent_pokemon.__str__()
        print(player_pokemon_string)
            
        Found_Move=add_moves(opponent_pokemon,Move_List)
 
        validturn=turn(1,player_pokemon,opponent_pokemon)
        
        if (validturn):
            validturn=turn(2,opponent_pokemon,player_pokemon)
            if (validturn)==False:
                #if the turn has been quit or after the player wins(else)
                usr_inp=input("Battle over, would you like to have another? ").lower()
                
        else:
            usr_inp=input("Battle over, would you like to have another? ").lower()

    if usr_inp != 'y':
        #if they do not input that they would like to have another battle, we print the goodbye
        print("Well that's a shame, goodbye")
        return    
   
if __name__ == "__main__":
    main()
