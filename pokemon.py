"""
    CSE 231 Project 11, pokemon file. This project will generate the methods we use in
    our main inputs to simulate a pokemon battle.
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            WRITE DOCSTRING HERE!!!
        '''        
        return self.name

    def __repr__(self):
        return self.__str__()
    
    def get_name(self):
        return self.name
    
    def get_element(self):
        return self.element
    
    def get_power(self):
        return self.power
       
    def get_accuracy(self):
        return self.accuracy
    
    def get_attack_type(self):
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
       
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''The function will return the string self in the proper format, we use this
        in the main for pokemon name and info'''
        
        
           
        s = "{:<15s}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}".format(self.name, self.hp, self.patt, self.pdef, self.satt, self.sdef)
        s += "\n{:<15s}{:<15s}\n".format(self.element1, self.element2)
        #We use this to display the info of the pokemon
        for move in self.moves:
                
            s+= "{:<15s}".format(str(move))
            #pokemon moves
                
        return s
     
        

    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.name

    def get_element1(self):
        return self.element1
    
    def get_element2(self):
        return self.element2
    
    def get_hp(self):
        return self.hp
    
    def get_patt(self):
        return self.patt      

    def get_pdef(self):
        return self.pdef
    
    def get_satt(self):
        return self.satt

    def get_sdef(self):
        return self.sdef
    
    def get_moves(self):
        return self.moves
    #these all return some form of the self 
        

    def get_number_moves(self):
        return len(self.moves)
      

    def choose(self,index):
        ArrayMoves=self.moves
        try:
            
            move_selected=ArrayMoves[index]
            return move_selected
        #for choosing the moves, if index invalid we will return None 
        
        except IndexError:
            
            return None
        
    def show_move_elements(self):
        
        element_string=''
        moves=self.moves

        for value in moves:
            #formatting the moves element
            element_string += "{:<15s}".format(value.get_element())
            print(element_string)

    def show_move_power(self):
        power_string=''
        moves=self.moves

        for value in moves:
            #formatting to show the power
            power_string += "{:<15d}".format(value.get_power())
            print(power_string)

    def show_move_accuracy(self):
        accuracy_string=''
        moves=self.moves

        for value in moves:
            #formatting to show the moves accuracy
            accuracy_string += "{:<15d}".format(value.get_accuracy())
            print(accuracy_string)
        
        
    def add_move(self, move):
        
        if len(self.moves) < 4:
            #append the move if the pokemon does not  have 4 moves
            self.moves.append(move)
       
      
    def attack(self, move, opponent):
        '''This function will generate the values for our attacks, using an equation
        and a modifier. If the attack is super effective, we double the value of the damage. 
        If it is not very effective, we halve the damage value. If no effect, we return no damage.
        This function will also add 1.5 times damage to the modifier if attack is same type as pokemon
        This function will also generate a value for the accuracy. Lastly and most importantly,
        this function will calculate the damage the attack does to the pokemon and its leftover hp'''
        #Get power of the move
        mp=move.get_power()
        attack_type=move.get_attack_type()
        move_element=move.get_element()
        
              
        if attack_type==2:
            
           A = self.patt
           D = opponent.pdef
          
        elif attack_type==3:
            
           A = self.satt
           D = opponent.sdef
           
        else:
            
           print("Invalid attack_type, turn skipped.")
           #If not a valid attack type
           return

    
        random_accuracy=randint(1,100)
        #generating our accuracy
        accuracy_value=move.get_accuracy()
        if random_accuracy>accuracy_value:
           print("Move missed!")
           return

        modifier=1
        #modifier initialized
        opponent_element1=opponent.get_element1()
        
        if opponent_element1 in is_effective_dictionary[move.get_element()]:
            
            modifier=modifier*2
            #If super effective move
            
        elif opponent_element1 in not_effective_dictionary[move.get_element()]:

            modifier=modifier/2
            #If not very effective move
            
        elif opponent_element1 in no_effect_dictionary[move.get_element()]:

            print("No effect...")
            #if no effect
            return

        opponent_element2=opponent.get_element2()
        
        if opponent_element2 in is_effective_dictionary[move.get_element()]:
            
            modifier=modifier*2
           
        elif opponent_element2 in not_effective_dictionary[move.get_element()]:
            
            modifier=modifier/2
                           
        elif opponent_element2 in no_effect_dictionary[move.get_element()]:
            
            print("No effect...")
            #same steps for the second pokemon
            return

            #modifier=0 in case of no effect
        if (move_element==self.get_element1()) or (move.element==self.get_element2()):  
            #STAB for pokemon moves of the same type as the pokemon
               
            modifier=modifier*1.5 
                
        if modifier > 1:
            #If mod is greater than 1 we print the super cool message
            
            print("It's super effective!!!!")
        else: #modifier < 1: we print the sad message
            
           print("Not very effective...")

        
        damage=int(((mp*(A/D)*20)/50 + 2) * modifier )
        #our equation for calculating the damage and then for calculating the leftover hp
        
        opponent.subtract_hp(damage)
      
            
        
    def subtract_hp(self,damage):
        '''This is the function used in attack method to calculate the hp
        leftover after an attack with damage is used'''
                
        a=self.hp-damage
        
        if a<=0:
            
            self.hp=0
        else:
            
            self.hp=(a)
        
     

        
