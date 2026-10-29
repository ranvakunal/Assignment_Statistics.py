
#       SESSION 1 - INTRODUCTION TO STATISTICS IN DATA SCIENCE


#       TASK - 1


actions = [
    "1. Liking an Instagram post -> Numerical Data (Count of total likes)",
    "2. Selecting a cuisine filter on Zomato (e.g., North Indian) -> Categorical Data",
    "3. Checking the price of shoes on Flipkart -> Numerical Data (Price value)",
    "4. Submitting restaurant star ratings on Zomato -> Numerical Data (Discrete/Ordinal)",
    "5. Selecting music genres on Spotify -> Categorical Data (Genre labels)"
]
for action in actions:
    print(action)


#-----------------------------------------------------------------------


#       TASK -2 



sample_data = ['Pop', 'Rock', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Jazz', 'Pop']

print(f"Sample Data: {sample_data}")
print("Classification: Categorical Data (Specifically Nominal Data)")
print("Reasoning: The sample consists of text labels representing music genres.")
print("Because these values represent distinct categories that cannot be added.")
print("subtracted, or averaged mathematically, they are classified as categorical data.")


#------------------------------------------------------------------------


#       TASK - 3



print("Feature Chosen: Restaurant ratings and review scores on Zomato.")
print("Statistical Analysis:")
print("- By computing descriptive statistics like mean and median ratings, Zomato ranks top-performing eateries.")
print("- Hypothesis testing can determine if interface redesigns significantly increase average customer ratings.")


#------------------------------------------------------------------------


#       TASK - 4



statistical_terms = [
    "1. Mean: Finds the mathematical average to represent central tendencies\n   Example: Calculating the average song duration (e.g., 3.5 minutes) in a user session.",
    "2. Mode: Identifies the most frequently occurring value or preference.\n   Example: Determining that 'Pop' is the genre a user listens to most frequently.",
    "3. Variance: Measures how much individual data points spread out from the overall mean.\n   Example: Measuring daily listening hours spread to check if user engagement is stable."
]
for term in statistical_terms:
    print(term)
  