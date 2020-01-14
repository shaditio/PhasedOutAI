from collections import defaultdict

"""This code is to count the scores for cards left in the hand"""

def phasedout_score(hand):
    
    # Initialise variables
    num_dict = defaultdict(int)
    score = 0
    
    # Put values in the dictionary
    for i in range(2, 10):
        num_dict[str(i)] = int(i)
    num_dict['0'] = 10
    num_dict['J'] = 11
    num_dict['Q'] = 12
    num_dict['K'] = 13
    num_dict['A'] = 25
    
    # Call the dictionary and apply it with the values in hand
    for card in hand:
        score += num_dict[card[0]]
    
    return score


if __name__ == '__main__':
    # Example calls to the function.
    print(phasedout_score(['9D', '9S', '9D', '0D', '0S', '0D']))
    print(phasedout_score(['2D', '9S', 'AD', '0D']))
    print(phasedout_score([]))