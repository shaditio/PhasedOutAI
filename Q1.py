from collections import defaultdict

""" This code is used to find out the certain group of a group of cards"""

def phasedout_group_type(group):
    # Create variables
    num_dict = defaultdict(int) 
    natural = 0
    ret = None
    
    # Check if natural cards in group appropriate
    for val in group:
        if val[0] != 'A':
            natural += 1   
    if natural < 2:
        return None
    
    # Create a dictionary to store cards' values
    for i in range(2, 10):
        num_dict[str(i)] = int(i)
    num_dict['0'] = 10
    num_dict['J'] = 11
    num_dict['Q'] = 12
    num_dict['K'] = 13
    num_dict['A'] = 14
    
    # Initialise the initial value and suit to be used
    initial_value = num_dict[group[0][0]]
    initial_suit = group[0][1]

            
    # GROUP 1
    if len(group) == 3:    
        
        # Check if all the cards excluding the initial card is equal to the
        # initial value
        for cards1 in group[1:]:
            if num_dict[cards1[0]] == initial_value:
                ret = 1
            else:    
                
                # If it is an ace, we still accept it
                if cards1[0] == 'A':
                    ret = 1
                else:
                    return None
                
    # GROUP 2   
    if len(group) == 7:
        
        # Check if all the cards excluding the initial card is equal to the
        # initial suit
        for cards2 in group[1:]:
            if cards2[1] == initial_suit:
                ret = 2
            else:
                
                # Accept it if it is an ace
                if cards2[0] == 'A':
                    ret = 2
                else:
                    return None
                
    # GROUP 3 AND GROUP 5 (RUN)
    if len(group) == 4:
        for cards3 in group[1:]:
            
            # Check if the value of the cards is same to the intial value;
            # and set to return 3
            if num_dict[cards3[0]] == initial_value:
                ret = 3
            
            # If the cards are 1 value above, set to return 5
            elif num_dict[str(cards3[0])] == initial_value + 1:
                initial_value += 1
                ret = 5
            else:
                
                # This code is to exempt any aces
                if cards3[0] == 'A' and ret == 3:
                    ret = 3
                elif num_dict[str(cards3[0])] == 14:
                    initial_value += 1
                    ret = 5
                else:
                    return None
    
    
    # GROUP 5 (SUIT)
    # If the flag set is 5 from the code earlier, begin this segment
    if ret == 5:
        
        # If the initial suit is red
        if initial_suit == 'D' or initial_suit == 'H':  
            for suit5 in group[1:]:
                if suit5[1] == 'D' or suit5[1] == 'H':
                    ret = 5
                else:
                    if suit5[0] == 'A': 
                        ret = 5
                    else:
                        return None
                    
        # If the initial suit is black
        else:
            for suit5 in group[1:]:
                if suit5[1] == 'C' or suit5[1] == 'S':
                    ret = 5
                else:
                    if suit5[0] == 'A': 
                        ret = 5
                    else:
                        return None
    
    
    # GROUP 4
    if len(group) == 8:
        # Check if the next value of the group is 
        # 1 value above the previous one
        for cards4 in group[1:]:  
            if num_dict[str(cards4[0])] == initial_value + 1:
                initial_value += 1
                ret = 4
            else:
                if num_dict[str(cards4[0])] == 14:
                    initial_value += 1
                    ret = 4
                else:
                    return None
            
    
    # return all set flags
    return ret


if __name__ == '__main__':
    # Example calls to the function.
    print(phasedout_group_type(['2C', '2S', '2H']))
    print(phasedout_group_type
          (['AC', 'AC', '4C', 'KC', '9C', 'AH', 'JC']))
    print(phasedout_group_type(['4H', '4S', 'AC', '4C']))
    print(phasedout_group_type
          (['AH', '5S', '6C', '7C', 'AH', '9H', 'AS', 'AC']))
    print(phasedout_group_type(['AH', '5D', 'AC', '7H']))
    print(phasedout_group_type(['4H', '5D', '7C', 'AC']))