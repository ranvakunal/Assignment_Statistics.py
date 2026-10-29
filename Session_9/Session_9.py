#       SESSION - 9 NORMAL DISTRIBUTION (BASICS)


#       TASK - 1


import numpy as np
import matplotlib.pyplot as plt


mu, sigma = 50, 10
data = np.random.normal(mu, sigma, 100)


plt.figure(figsize=(9, 5))
count, bins, ignored = plt.hist(data, bins=15, density=True, color='skyblue', edgecolor='black', alpha=0.7)


p = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)*2 / (2 * sigma*2))
plt.plot(bins, p, linewidth=2, color='crimson', label='Normal Curve ($\mu=50, \sigma=10$)')

plt.title('Normal Distribution Bell Curve (100 Samples)', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#_--------------------------------------------------------------------



#      TASK - 2 



import numpy as np
from scipy import stats


step_counts = np.array([
    7200, 8100, 6900, 7500, 7800, 
    8000, 7400, 7600, 7700, 7300, 
    7500, 7900, 7100, 8200, 7400, 
    7600, 7800, 7500, 7000, 7900
])


mean_val = np.mean(step_counts)
median_val = np.median(step_counts)
mode_result = stats.mode(step_counts, keepdims=True)
mode_val = mode_result.mode[0]

print(f"Mean Step Count: {mean_val:.2f}")
print(f"Median Step Count: {median_val:.2f}")
print(f"Mode Step Count: {mode_val}")


if abs(mean_val - median_val) < 200:
    print("\nConclusion: The mean, median, and mode are approximately equal, reflecting the characteristics of a normal distribution.")
else:
    print("\nConclusion: The values diverge, indicating potential skewness.")


#------------------------------------------------------------------------------------


#     TASK - 3


import numpy as np


np.set_printoptions(precision=2)
mean_score, std_score = 70, 15
num_players = 200

player_scores = np.random.normal(mean_score, std_score, num_players)


lower_bound = mean_score - std_score  
upper_bound = mean_score + std_score  

within_one_sd = [score for score in player_scores if lower_bound <= score <= upper_bound]
count_within = len(within_one_sd)
percentage = (count_within / num_players) * 100

print(f"Total Players: {num_players}")
print(f"Players scoring within 1 SD ({lower_bound} to {upper_bound}): {count_within}")
print(f"Actual Percentage: {percentage:.2f}%")
print(f"Expected Percentage (Empirical 68-95-99 Rule): ~68%")


#-------------------------------------------------------------------------------------------


#       TASK - 4

"""
4.
Pick any real-world scenario (like delivery times for Zomato orders or playlist song durations on Spotify) and explain in 3-4 lines why the normal distribution might be a good fit for modeling this data
"""

#For this scenario, let's analyze food delivery times (like Zomato or Swiggy orders).

#Food delivery times follow a normal distribution because they have a consistent average time (e.g., 30 minutes) under normal conditions,
#  which forms the peak of the curve. The variations from this average are driven by many independent, 
# random factors working together—such as kitchen preparation speed, traffic light timings, 
# and elevator waits. 
# 
# According to the Central Limit Theorem, the cumulative effect of these small, 
# random variables naturally shapes the data into a symmetric, bell-shaped curve where extreme early or late deliveries become progressively rare.