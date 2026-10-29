#       SESSION : 8  PROBABILITY (BASICS)


#       TASK - 1



def calculate_probability(event_count, total_outcomes):
    """Calculates and returns the probability of an event."""
    if total_outcomes == 0:
        return 0.0
    return event_count / total_outcomes


heads_count = 1
total_coin_outcomes = 2

prob_heads = calculate_probability(heads_count, total_coin_outcomes)
print(f"Probability of getting 'Heads': {prob_heads}")

#---------------------------------------------------------------------------------


#      TASK - 2 


import random

total_rolls = 100
count_six = 0


for _ in range(total_rolls):
    roll = random.randint(1, 6)
    if roll == 6:
        count_six += 1


experimental_probability = count_six / total_rolls

print(f"Total rolls: {total_rolls}")
print(f"Number of times '6' appeared: {count_six}")
print(f"Experimental probability of getting a '6': {experimental_probability}")


#-----------------------------------------------------------------------------------


#     TASK - 3  




spotify_history = [
    'pop', 'rock', 'pop', 'hiphop', 'pop', 
    'jazz', 'rock', 'pop', 'hiphop', 'pop', 
    'classical', 'pop', 'rock', 'pop', 'hiphop', 
    'pop', 'jazz', 'rock', 'pop', 'hiphop'
]

total_songs = len(spotify_history)
pop_count = spotify_history.count('pop')


prob_pop = pop_count / total_songs

print(f"Total songs: {total_songs}")
print(f"Total 'pop' songs: {pop_count}")
print(f"Probability of picking a 'pop' song: {prob_pop}")


#-----------------------------------------------------------------------------------


#     TASK - 4  


def calculate_joint_probability(food_users, dessert_users):
    
    set_food = set(food_users)
    set_dessert = set(dessert_users)
    
    intersection = set_food.intersection(set_dessert)
    total_unique_users = set_food.union(set_dessert)
    
    if len(total_unique_users) == 0:
        return 0.0
        
    probability = len(intersection) / len(total_unique_users)
    return probability


zomato_food_users = ['user1', 'user2', 'user3', 'user4', 'user5']
zomato_dessert_users = ['user3', 'user4', 'user6', 'user7']

prob_both = calculate_joint_probability(zomato_food_users, zomato_dessert_users)
print(f"Probability that a randomly selected user ordered both: {prob_both:.4f}")


#_----------------------------------------------------------------------------------



#    TASK - 5   



phone_buyers = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9', 'u10']
phone_and_headphone_buyers = ['u2', 'u4', 'u7', 'u10']

def conditional_probability(buyers_a_and_b, buyers_b):
    """
    Calculates P(A | B) = P(A and B) / P(B)
    Here, A = Bought Headphones, B = Bought Phone
    """
    total_b = len(buyers_b)
    if total_b == 0:
        return 0.0
    
    both_count = len(set(buyers_a_and_b).intersection(set(buyers_b)))
    return both_count / total_b


prob_headphones_given_phone = conditional_probability(phone_and_headphone_buyers, phone_buyers)

print(f"Probability of buying headphones given user bought a phone: {prob_headphones_given_phone:.2f}")