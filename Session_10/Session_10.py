#              SESSION - 10  BAYER'S THEOREM (BASICS)


#             TASK - 1  

"""
1.
Write a Python function bayes_posterior(prior, likelihood, evidence) that calculates and returns the posterior probability using Bayes theorem formula for given values
"""


def bayes_posterior(prior, likelihood, evidence):
 
    if evidence == 0:
        return 0.0
    return (likelihood * prior) / evidence


prior_val = 0.1
likelihood_val = 0.8
evidence_val = 0.28

posterior = bayes_posterior(prior_val, likelihood_val, evidence_val)
print(f"Calculated Posterior Probability: {posterior:.4f}")


#--------------------------------------------------------------------


#            TASK - 2   

"""
2.
Given the following scenario: On Swiggy, 10% of restaurants are 'premium', and 80% of premium restaurants offer a discount, while only 20% of regular restaurants do. If you see a discount, use Bayes theorem in code to find the probability that the restaurant is premium.
"""



p_premium = 0.10 
p_regular = 0.90  


p_discount_given_premium = 0.80  
p_discount_given_regular = 0.20  


p_discount = (p_discount_given_premium * p_premium) + (p_discount_given_regular * p_regular)


p_premium_given_discount = (p_discount_given_premium * p_premium) / p_discount

print(f"Total Evidence P(Discount): {p_discount:.4f}")
print(f"Probability that the restaurant is premium given it offers a discount: {p_premium_given_discount:.4f}")


#--------------------------------------------------------------------------------------


#       TASK - 3


"""
3.
Simulate a basic spam detection filter: Given a list of 20 email subjects (some spam, some not), and the probability that 'free' appears in spam vs non-spam emails, write code to calculate the probability an email is spam if it contains 'free', using Bayes theorem.
"""


email_subjects = [
    "Win a free iPhone now", "Meeting schedule for tomorrow", "Claim your free gift card",
    "Project update and status report", "Exclusive free trial inside", "Weekly newsletter",
    "Get rich quick with this free trick", "Lunch plans today?", "Free cash bonus waiting for you",
    "Code review feedback", "Limited time free access", "Team sync notes",
    "Free vacation package winner", "Reminder: Dentist appointment", "100% free download here",
    "Invoice for your subscription", "Free cryptocurrency air-drop", "Flight booking confirmation",
    "Claim your free voucher", "Quarterly financial review"
]

total_emails = len(email_subjects)


spam_like_count = sum(1 for subject in email_subjects if 'free' in subject.lower())
clean_count = total_emails - spam_like_count


p_spam = spam_like_count / total_emails
p_non_spam = clean_count / total_emails


p_free_given_spam = 0.90      
p_free_given_non_spam = 0.10  


p_free = (p_free_given_spam * p_spam) + (p_free_given_non_spam * p_non_spam)


if p_free > 0:
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free
else:
    p_spam_given_free = 0.0

print(f"Total Emails: {total_emails}")
print(f"Probability an email is spam given it contains 'free': {p_spam_given_free:.4f}")


#-------------------------------------------------------------------------


#       TASK - 4

"""
4.
Use ChatGPT or Copilot to generate a real-world Bayes theorem example related to any app you use (Instagram, Zomato, Flipkart, etc.), then write code to solve it and submit both the prompt you used and your code
"""


# Bayes' Theorem: Instagram Spam Detection

# Given probabilities
p_spam = 0.20
p_detect_spam = 0.90
p_false_positive = 0.10

# Probability of a genuine message
p_genuine = 1 - p_spam

# Probability that a message is flagged as spam
p_flagged = (
    p_detect_spam * p_spam
    + p_false_positive * p_genuine
)

# Bayes' Theorem
p_spam_given_flagged = (
    p_detect_spam * p_spam / p_flagged
)

print("Probability that a message is actually spam:")
print(round(p_spam_given_flagged * 100, 2), "%")
