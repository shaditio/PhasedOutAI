from collections import defaultdict

"""This code is to check if a certain play is valid"""

def phasedout_is_valid_play(play, player_id, table, turn_history, phase_status,
                            hand, discard):
    
    # ------------- IMPORT GROUP 2 ----------------
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
                # Check if all the cards excluding the initial 
                # card is equal to the initial suit
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

    
    # ------------- THE CODE FOR THIS QUESTION ------------------
    
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
        
        # Check if the card placed on the phase on table matches the phase type        
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
                        initial_value = num_dict[phase_on_table[group][i][0]]
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
