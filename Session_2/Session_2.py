#       SESSION 2: MEAN, MEDIAN, MODE

#       TASK : 1


import numpy as np
from scipy import stats

play_counts = [120, 135, 150, 200, 120, 90, 200]


mean_play_count = np.mean(play_counts)


print("--- Spotify Playlist Statistics ---")
print(f"Play Counts: {play_counts}")
print(f"Mean Play Count: {mean_play_count:.2f}")




#-------------------------------------------------------------


#       TASK : 2


import numpy as np


delivery_times = [30, 25, 40, 35, 30, 45, 30]

median_time = np.median(delivery_times)

print(f"Delivery Times (mins): {delivery_times}")
print(f"Median Delivery Time: {median_time} minutes")

#-------------------------------------------------------------


#      TASK : 3 


from scipy import stats

def most_common_rating(ratings):
    
    if not ratings:
        return None
    
    mode_result = stats.mode(ratings, keepdims=True)
    return mode_result.mode[0]


flipkart_ratings = [5, 4, 4, 3, 5, 4, 2, 4]
mode_rating = most_common_rating(flipkart_ratings)

print(f"Flipkart Ratings: {flipkart_ratings}")
print(f"Most Common Rating (Mode): {mode_rating} stars")

#----------------------------------------------------------------


#      TASK : 4 


import numpy as np
from scipy import stats


channel_a = [100, 120, 110, 105, 5000]  
channel_b = [500, 520, 480, 510, 490]   
channel_c = [200, 300, 200, 250, 200]   

channels = {
    "Channel A (Viral Outlier)": channel_a,
    "Channel B (Consistent)": channel_b,
    "Channel C (Frequent Repeat)": channel_c
}

for name, views in channels.items():
    mean_v = np.mean(views)
    median_v = np.median(views)
    mode_v = stats.mode(views, keepdims=True).mode[0]
    
    print(f"--- {name} ---")
    print(f"Views: {views}")
    print(f"Mean: {mean_v:.2f} | Median: {median_v:.2f} | Mode: {mode_v}\n")

#------------------------------------------------------------


#       TASK : 5


import pandas as pd
from scipy import stats


data = {
    'restaurant_name': ['Agashiye', 'Rajwadu', 'Gordhan Thal', 'Ghee-Gud', 'Vishalla', 'Patang', 'Iskon Thal'],
    'rating': [4.2, 4.5, 4.5, 4.8, 3.9, 4.1, 4.5],
    'cost_for_two': [2000, 1500, 1000, 600, 1200, 3000, 750]
}

df = pd.DataFrame(data)

ratings_column = df['rating']

mean_rating = ratings_column.mean()
median_rating = ratings_column.median()
mode_rating = ratings_column.mode()[0] 

print("--- Swiggy Dataset Column Analysis: Restaurant Ratings ---")
print(df[['restaurant_name', 'rating']])
print("\nResults:")
print(f"Mean Rating: {mean_rating:.2f}")
print(f"Median Rating: {median_rating:.2f}")
print(f"Mode Rating: {mode_rating:.2f}")