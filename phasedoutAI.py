from itertools import combinations
from collections import defaultdict

""" This code is to check which play made is the best by using functions
    from Q1, Q2, Q3"""

def phasedout_play(player_id, table, turn_history, phase_status, hand,
                   discard):
    
    # -- Q 1 CODES -- 
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
    
    #-------------- Q 2 CODES -------------
    def phasedout_phase_type(phase):
        
        for group in phase:

            # Create variables
            initial_value = group[0][0]
            initial_suit = group[0][1]
            num_dict = defaultdict(int)  
            natural = 0
            ret = None
            flag = None

            # Check if natural cards in group are appropriate
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
                for j in range(len(group)):
                    initial_value = group[0][0]
                    initial_suit = group[0][1]
                    if group[0][0] == 'A':
                        initial_value = group[j][0]
                        initial_suit = group[j][1]

                # Check if all the cards excluding the initial 
                # card is equal to the initial value
                for cards1 in group[1:]:
                    if cards1[0] == initial_value:
                        ret = 1
                    else:
                        if cards1[0] == 'A':
                            ret = 1
                        else:
                            return None


            # GROUP 2   
            if len(group) == 7:
                # Check if all the cards excluding the 
                # initial card is equal to the initial suit
                for cards2 in group[1:]:
                    if cards2[1] == initial_suit:
                        ret = 2
                    else:
                        if cards2[0] == 'A':
                            ret = 2
                        else:
                            return None


            # GROUP 3 AND GROUP 5 (RUN)
            if len(group) == 4:
                # Check if the value of the cards is same to the intial value;
                # and set to return 3
                for cards3 in group[1:]:
                    if num_dict[cards3[0]] == initial_value:
                        ret = 3

                    # If the cards are 1 value above, set to return 5 and
                    # create a flag to check the other groupin phase 5
                    elif num_dict[str(cards3[0])] == initial_value + 1:
                        initial_value += 1
                        ret = 5
                        flag = 5

                    else:
                        if cards3[0] == 'A' and ret == 3:
                            ret = 3
                        elif num_dict[str(cards3[0])] == 14:
                            initial_value += 1
                            ret = 5
                            flag = 5
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
                else:
                    for suit5 in group[1:]:

                        # If the initial suit is black
                        if suit5[1] == 'C' or suit5[1] == 'S':
                            ret = 5
                        else:
                            if suit5[0] == 'A': 
                                ret = 5
                            else:
                                return None

            # GROUP 5 (SAME VALUE)
            # If the flag exists, perform check for the last group
            if flag:
                for same in phase[1][1:]:
                    initial_value = phase[1][0][0]
                    if same[0] == initial_value:
                        ret = 5
                    else:
                        if same[0] == 'A':
                            ret = 5
                        else:
                            return None
                return ret     

            # GROUP 4
            # Check if the next value of the group is 
            # 1 value above the previous one
            if len(group) == 8:
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


        return ret

    
    # --------------- Q 3 CODES ---------------
    def phasedout_is_valid_play(play, player_id, table,
                                turn_history, phase_status, hand, discard):
     
        # --- PLAY 1 ---
        if play[0] == 1:

            # Check if card picked up is only a card or None
            if len(play[1:]) > 1 or not play[1]:
                return False

            return True

        # --- PLAY 2 ---
        if play[0] == 2:
            card_picked = play[1]

            # If discard doesn't match picked up card
            if card_picked != discard:
                return False

            # If discard is none
            if not discard:
                return False

            return True

        # --- PLAY 3 ---
        if(play[0] == 3):
            card_phase = phasedout_phase_type(list(play[1]))
            # Check if the cards about to be placed are of a correct phase type
            if not card_phase:
                return False

            # Check if the cards about to be placed are all in their hand
            for group in play[1]:
                for cards in group:
                    if cards not in hand:
                        return False

            # Check if the player has already placed a phase on the table       
            if table[player_id][0] or table[player_id][1]:
                return False

            # Check the corresponding phase status whether it is correct
            if card_phase - 1 != phase_status[player_id]:
                return False

            return True


        # --- PLAY 4 --- 
        if(play[0] == 4):
            if len(play[1][1]) != 3 or not play[1][0]:
                return False

            # Get data in the tuples from 'play'
            card_placed = play[1][0]
            player_id_place = play[1][1][0]
            group = play[1][1][1]
            index = play[1][1][2]
            phase_on_table = table[player_id_place][1]
            num_dict = defaultdict(int)  

            # Create dictionary to store numbers
            for i in range(2, 10):
                num_dict[str(i)] = int(i)
            num_dict['0'] = 10
            num_dict['J'] = 11
            num_dict['Q'] = 12
            num_dict['K'] = 13
            num_dict['A'] = 14

            # Check if placed player has a phase on the table 
            if not phase_on_table:
                return False

            # Set initial values
            initial_value = num_dict[phase_on_table[0][0][0]]
            initial_suit = phase_on_table[0][0][1]



            # Check if the turn's player has a phase and is appropriate
            if not table[player_id][1]:
                return False

            # Check if the group where the cards have to be placed is valid
            if int(group) > len(phase_on_table):
                return False

            # Check if the card placed on the phase on table matches 
            # the phase type        
            if table[player_id_place][0]:
                phase_type = phase_status[player_id_place]
                phase_on_table[group].insert(index, card_placed)
            else:
                phase_type = phasedout_phase_type(phase_on_table)
                phase_on_table[group].insert(index, card_placed)

            # If phase type is 1
            if phase_type == 1:
                for i in range(len(phase_on_table)):

                    # Set an initial value
                    initial_value = num_dict[phase_on_table[group][0][0]]
                    initial_suit = phase_on_table[group][0][1]
                    if phase_on_table[group][0][0] == 'A':
                        initial_value = num_dict[phase_on_table[group][i][0]]
                        initial_suit = phase_on_table[group][i][1]

                for cards1 in hand:
                    if str(cards1[group][0]) == str(initial_value):
                        pass
                    else:
                        if cards1[group][0] == 'A':
                            pass
                        else:
                            return False

            # If phase type is 2
            if phase_type == 2:
                for cards2 in hand:  
                    if cards2[1] == initial_suit:
                        pass
                    else:
                        if cards2[0] == 'A':
                            pass
                        else:
                            return False

            # If phase type is 3
            if phase_type == 3:
                initial_value = num_dict[phase_on_table[group][0][0]]
                initial_suit = phase_on_table[group][0][1]
                for cards3 in hand:
                    if str(cards3[group][0]) == str(initial_value):
                        pass
                    else:
                        if cards3[group][0] == 'A':
                            pass
                        else:
                            return False   

            # If phase type is 4
            if phase_type == 4:
                for cards4 in hand:   
                    if num_dict[str(cards4[0])] == initial_value + 1:
                        initial_value += 1
                        pass
                    else:
                        if num_dict[str(cards4[0])] == 14:
                            initial_value += 1
                            pass
                        else:
                            return False

            # If phase type is 5
            if phase_type == 5:

                # Perform the usual check for the 1st group
                if group == 0:
                    for cards5 in hand:         
                        if num_dict[str(cards5[0])] == initial_value + 1:
                            initial_value += 1
                            pass
                        else:
                            if num_dict[str(cards5[0])] == 14:
                                initial_value += 1
                                pass
                            else:
                                return False 

                    if initial_suit == 'D' or initial_suit == 'H':  
                        for suit5 in phase_on_table[0][1:]:
                            if suit5[0][1] == 'D' or suit5[0][1] == 'H':
                                pass
                            else:
                                if suit5[0][0] == 'A': 
                                    pass
                                else:
                                    return None
                    else:
                        for suit5 in phase_on_table[0][1:]:
                            if suit5[0][1] == 'C' or suit5[0][1] == 'S':
                                pass
                            else:
                                if suit5[0][0] == 'A': 
                                    pass
                                else:
                                    return None

                # And perform this check for the second one
                elif group == 1:
                    for i in range(len(phase_on_table)):
                        initial_value = num_dict[phase_on_table[group][0][0]]
                        initial_suit = phase_on_table[group][0][1]
                        if phase_on_table[group][0][0] == 'A':
                            initial_value = num_dict[phase_on_table
                                                     [group][i][0]]
                            initial_suit = phase_on_table[group][i][1]

                    for cards5 in phase_on_table[group][1:]:
                        if str(cards5[group][0]) == str(initial_value):
                            pass
                        else:
                            if cards5[group][0] == 'A':
                                pass
                            else:
                                return False 


            return True

        # --- PLAY 5 ---
        if play[0] == 5:
            discarded_card = play[1]

            # Check if the discarded card is in hand
            if discarded_card not in hand:
                return False

            return True

    
    
    
    
    
    # ---------------------- THE CODE --------------------------
    # Perform play 1 / play 2
    
    # If the turn history states that it is the player's turn
    if turn_history == [] or turn_history[-1][-1][-1][0] == 5:
        new_hand = hand.copy()
        ret_val = ()
        
        # Create a new hand if the discard card were to be in the player's hand
        new_hand.append(discard)
        
        # Check if the player has no phase yet
        if not table[player_id][0]:
            phase_type = phase_status[player_id] + 1

            
            # Phase type 1
            if phase_type == 1:
                for rand in combinations(new_hand, 3):
                    if phasedout_group_type(rand) == 1:
                        ret_val = (2, discard)
                    else:
                        ret_val = (1, None)
                return ret_val
                
            # Phase type 2
            if phase_type == 2:
                for rand in combinations(new_hand, 7):
                    if phasedout_group_type(rand) == 2:
                        ret_val = (2, discard)
                    else:
                        ret_val = (1, None)
                return ret_val
            
            # Phase type 3
            if phase_type == 3:
                for rand in combinations(new_hand, 4):
                    if phasedout_group_type(rand) == 3:
                        ret_val = (2, discard)
                    else:
                        ret_val = (1, None)
                return ret_val
                    
            # Phase type 4
            if phase_type == 4:
                for rand in combinations(new_hand, 8):
                    if phasedout_group_type(rand) == 4:
                        ret_val = (2, discard)
                    else:
                        ret_val = (1, None)
                return ret_val
                   
            # Phase type 5
            if phase_type == 5:
                for rand in combinations(new_hand, 4):
                    if phasedout_group_type(rand) == 5:
                        ret_val = (2, discard)
                    else:
                        for random in combinations(new_hand, 4):
                            if phasedout_group_type == 3:
                                ret_val = (2, discard)
                            else:
                                ret_val = (1, None)
                return ret_val
            
        if table[player_id][0]:
                return 1, None
    
    # Perform play 3
    if turn_history[-1][-1][-1][0] == 1 or turn_history[-1][-1][-1][0] == 2:
        
        # An empty phase is required to perform play 3
        if not table[player_id][0]:
            phase_type = phase_status[player_id] + 1
            list1 = []
            list2 = []
            list_check = []
            
            # Phase 1
            if phase_type == 1:
                for com in combinations(hand, 6):
                    list1 = []
                    list2 = []
                    list_check = []
                    for cards1 in com[:3]:
                        list1.append(cards1)
                        
                    list_check.append(list1)
                    
                    for cards2 in com[3:]:
                        list2.append(cards2)
                        
                    list_check.append(list2)
                                        
                    if phasedout_phase_type(list_check) == 1:
                        return 3, list_check
                        
            # Phase 2
            if phase_type == 2:
                for com in combinations(hand, 7):
                    list_check = []
                    list_check.append(com)
                    if phasedout_phase_type(list_check) == 2:
                        return 3, list_check
                    
            # Phase 3
            if phase_type == 3:
                for com in combinations(hand, 8):
                    list1 = []
                    list2 = []
                    list_check = []
                    for cards1 in com[:4]:
                        list1.append(cards1)
                        
                    list_check.append(list1)
                    
                    for cards2 in com[4:]:
                        list2.append(cards2)
                        
                    list_check.append(list2)
                                        
                    if phasedout_phase_type(list_check) == 3:
                        return 3, list_check
             
            # Phase 4
            if phase_type == 4:
                for com in combinations(hand, 8):
                    list_check = []
                    list_check.append(com)
                    if phasedout_phase_type(list_check) == 4:
                        return 4, list_check
                    
            # Phase 5
            if phase_type == 5:
                for com in combinations(hand, 8):
                    list1 = []
                    list2 = []
                    list_check = []
                    for cards1 in com[:4]:
                        list1.append(cards1)
                        
                    list_check.append(list1)
                    
                    for cards2 in com[4:]:
                        list2.append(cards2)
                        
                    list_check.append(list2)
                                        
                    if phasedout_phase_type(list_check) == 5:
                        return 5, list_check                    
                                    
                                
    # Play 4
    # Play 4 is performed when the previous play is 1, 2 or 5
    if (turn_history[-1][-1][-1][0] == 1 or
        turn_history[-1][-1][-1][0] == 2 or
            turn_history[-1][-1][-1][0] == 5):  
        
        # Iterate through the entire cards and place it for each location
        # in the phases on the table and use function from Q3 to check
        # if it is valid
        if table[player_id][0]: 
            for cards in hand:
                for players in range(4):
                    if phasedout_is_valid_play((4, (cards, (players, 0, -1))),
                                               player_id, table, turn_history,
                                               phase_status, hand, discard):
                        return (4, (cards, (players, 0, 0)))
                    
                    # Check for the second group if the phases are 
                    # phase 1, 3, 5
                    if (phase_status[players] == 1 or
                        phase_status[players] == 3 or
                            phase_status[players] == 5):
                        if phasedout_is_valid_play((4, (cards,
                                                        (players, 1, -1))),
                                                   player_id, table,
                                                   turn_history, phase_status,
                                                   hand, discard):
                            return (4, (cards, (players, 1, 0)))
                        
      
    
    # Play 5
    # Play 5 is done when the previous plays are 1, 2, 3 or 4
    if (turn_history[-1][-1][-1][0] == 1 or
        turn_history[-1][-1][-1][0] == 2 or
        turn_history[-1][-1][-1][0] == 3 or
            turn_history[-1][-1][-1][0] == 4):
        
        # If there is one card left
        if len(hand) == 1:
            return 5, hand[0]
        
        else:
            if not table[player_id][0]:
                phase_done = phase_status[player_id] + 1

                # If phase 1 or 3
                if phase_done == 1 or phase_done == 3:
                    # Count the numbers in hand; discard the least
                    count_dict = defaultdict(int)
                    store = []
                    for card in hand:
                        if card[0]:
                            count_dict[card[0]] += 1

                    # Append all the values with lowest values in a list
                    for key in count_dict:
                        if count_dict[key] == min(count_dict.values()):
                            store.append(key)
                    
                    # Discard a non-A value which is the highest
                    if sorted(store)[-1] == 'A' and len(store) > 1:
                        discarded = sorted(store)[-2]
                    else:
                        discarded = sorted(store)[-1]
                    
                    # Locate card with corresponding value
                    for card in sorted(hand):
                        if card[0] == discarded:
                            return 5, card
                        
                # If phase 2
                if phase_done == 2:
                    # Count the suits in hand; discard the least
                    count_dict = defaultdict(int)
                    store = []
                    for card in hand:
                        if card[1]:
                            count_dict[card[1]] += 1

                    # Append all the values with ones in a list
                    for key in count_dict:
                        if count_dict[key] == min(count_dict.values()):
                            store.append(key)
                    
                    # Locate card with corresponding value
                    for card in sorted(hand, reverse=True):
                        if card[1] == store[0]:
                            return 5, card
                
                # If phase 4 or 5
                if phase_done == 4 or phase_done == 5:
                    # Count the numbers in hand; discard the most
                    count_dict = defaultdict(int)
                    store = []
                    for card in hand:
                        if card[0]:
                            count_dict[card[0]] += 1

                    # Append all the values with highest values in a list
                    for key in count_dict:
                        if count_dict[key] == max(count_dict.values()):
                            store.append(key)

                    # Discard a non-A value which is the highest
                    if sorted(store)[-1] == 'A' and len(store) > 1:
                        discarded = sorted(store)[-2]
                    else:
                        discarded = sorted(store)[-1]
                    
                    # Locate card with corresponding value
                    for card in sorted(hand):
                        if card[0] == discarded:
                            return 5, card        
                        
                if sorted(hand)[-1][0] == 'A':
                    return 5, sorted(hand)[-2]
                else:
                    return 5, sorted(hand)[-1]
                
            else:
                # Return the highest-valued card
                if sorted(hand)[-1][0] == 'A':
                    return 5, sorted(hand)[-2]
                else:
                    return 5, sorted(hand)[-1]
    
    
