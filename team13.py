import random
team_name = 'Mok' # Only 10 chars displayed.
strategy_name = 'Only a little cheating'
strategy_description = 'random?'
def move(my_history, their_history, my_score, their_score):
        if (their_score) > (my_score):
            return '1'
        elif random.choice([0,1,2,3,4,5,6,7,8,9,10])<2: 
                return '1'        
        else:
            return 'c' 
        
