#       SESSION 4 : SKEWNESS (BASICS)

#    TASK : 1   

"""
1.
Given the daily order counts for a Swiggy delivery partner over 10 days: [12, 15, 17, 14, 13, 16, 200, 18, 14, 15], plot a simple graph (hand-drawn or using any tool) and describe whether the data is left skewed, right skewed, or symmetrical. Explain your reasoning based on the shape
"""

import matplotlib.pyplot as plt

orders = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]

plt.figure(figsize=(8, 4))
plt.plot(orders, marker='o', color='purple', linestyle='-', linewidth=2, markersize=8)
plt.title('Swiggy Delivery Partner Daily Orders (Outlier Test)', fontsize=13)
plt.xlabel('Days', fontsize=11)
plt.ylabel('Order Count', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#--------------------------------------------------------------------------------------------


#   TASK : 2    

"""
2.
Take the following list of Instagram influencer follower counts (in thousands): [5, 7, 8, 8, 9, 10, 12, 15, 95]. Calculate the mean and median, then state which is higher and what that tells you about the skewness of the data.<br><br><em><strong>Hint:</strong> If the mean is pulled away from the median, the data is skewed in that direction
"""


import numpy as np

followers = [5, 7, 8, 9, 10, 12, 15, 95]

mean_val = np.mean(followers)
median_val = np.median(followers)

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")

#--------------------------------------------------------------------------------------------


#          TASK - 3

"""
3.
Find a real-world example of right-skewed data from any app you use (like Zomato order amounts, Paytm wallet balances, or YouTube video views). Briefly describe the dataset and explain why you think it is right skewed.
"""


#A perfect real-world example of right-skewed data is YouTube video views.


#The dataset consists of the total view counts for every video uploaded to YouTube. The data points range from 0 views to billions of views.

#Why it is Right-Skewed :

# 1)    Natural Floor: The data is bounded on the lower end by zero. A video cannot have negative views.
# 2)    The Majority (The Peak): The vast majority of videos uploaded by everyday users, small creators, or dead accounts struggle to get traction. Most videos sit at the lower end of the scale, usually between 0 and a few thousand views.
# 3)    The Long Tail (The Outliers) :There is no upper limit on the maximum number of views. A tiny fraction of videos—such as viral memes, major music videos, or content from top creators (like MrBeast)—explode into millions or billions of views.

#Because the mean is heavily pulled to the right by these ultra-viral videos while the median remains much lower, the data creates a long tail stretching toward the right side of the graph.


#--------------------------------------------------------------------------------------------


#          TASK : 4

"""
4.
Given this dataset of Flipkart product ratings: [3, 3, 4, 4, 4, 5, 5, 5, 5, 5], draw a rough graph and state if the distribution is symmetrical, left skewed, or right skewed. Justify your answer in one line
"""

import matplotlib.pyplot as plt

ratings = [3, 3, 4, 4, 4, 5, 5, 5, 5]

plt.figure(figsize=(7, 4))
plt.hist(ratings, bins=[2.5, 3.5, 4.5, 5.5], color='teal', edgecolor='black', align='mid')
plt.title('Flipkart Product Ratings Distribution', fontsize=13)
plt.xlabel('Rating Stars', fontsize=11)
plt.ylabel('Frequency', fontsize=11)
plt.xticks([3, 4, 5])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
