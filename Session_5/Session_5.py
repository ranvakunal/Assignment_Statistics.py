#       SESSON 5 : SAMPLING

#    TASK : 2

import random


user_ids = [f"user{i}" for i in range(1, 1001)]


sampled_users = random.sample(user_ids, 50)


print("Selected 50 random users for survey:")
print(sampled_users)