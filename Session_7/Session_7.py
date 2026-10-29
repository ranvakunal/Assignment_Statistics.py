#       SESSON 7 : CORRELATION


#       TASK : 1

"""
1.
Create two Python lists: one representing the number of hours you spend on Instagram each day for a week, and another for the number of posts you make each day. Plot these as a scatter plot using matplotlib and visually describe whether the relationship looks like a positive, negative, or zero correlation
"""


import matplotlib.pyplot as plt


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
instagram_hours = [1.5, 2.0, 1.0, 2.5, 3.0, 4.0, 3.5]  
posts_made = [0, 1, 0, 1, 2, 3, 2]                    


plt.figure(figsize=(8, 5))
plt.scatter(instagram_hours, posts_made, color='purple', s=100, zorder=3)


plt.title('Instagram Hours vs. Posts Made Daily', fontsize=14)
plt.xlabel('Hours Spent on Instagram', fontsize=12)
plt.ylabel('Number of Posts Made', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)


plt.show()

#--------------------------------------------------------------------------------------


#      TASK : 2

"""
2.
Given the following data for 6 friends: their monthly Zomato order count and their monthly Swiggy order count, calculate the correlation coefficient between the two lists using numpy's corrcoef(). Print the result and explain if the correlation is positive, negative, or zero.
"""

import numpy as np


zomato_orders = [4, 8, 2, 6, 10]
swiggy_orders = [5, 7, 1, 8, 12]


correlation_matrix = np.corrcoef(zomato_orders, swiggy_orders)
correlation_coefficient = correlation_matrix[0, 1]

print(f"Correlation Coefficient: {correlation_coefficient:.4f}")


#--------------------------------------------------------------------------------------


#       TASK - 3

"""
3.
Think of two variables from your daily life (for example, number of YouTube videos watched per day and daily study hours). Write a short paragraph describing whether you expect a positive, negative, or zero correlation between them, and why

"""


#Example: Daily Study Hours and Exam Scores

#I expect a positive correlation between daily study hours and exam scores. Generally, when students spend more time studying, they may understand the topics better and achieve higher marks. However, this relationship is not guaranteed because factors such as study quality, concentration, and sleep also affect exam performance.






#---------------------------------------------------------------------------------
#     TASK : 4

"""
4.
Use ChatGPT to generate a small dataset (10 pairs of numbers) that shows a strong negative correlation between time spent on Spotify and marks scored in a test. Paste the dataset and plot it as a scatter plot using matplotlib
"""

import matplotlib.pyplot as plt


spotify_hours = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
test_marks = [92, 88, 85, 78, 70, 65, 58, 50, 42, 35]


plt.figure(figsize=(8, 5))
plt.scatter(spotify_hours, test_marks, color='crimson', s=100, zorder=3)


plt.title('Spotify Listening Time vs. Test Marks (Strong Negative Correlation)', fontsize=13)
plt.xlabel('Time Spent on Spotify (Hours/Day)', fontsize=12)
plt.ylabel('Test Marks (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)


plt.show()