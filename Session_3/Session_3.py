#       SESSION 3: VARIANCE, STANDARD DEVIATION

#    TASK : 2


import numpy as np

def calculate_standard_deviation(scores):
   
    if len(scores) <= 1:
        return 0.0
    
    std_dev = np.std(scores, ddof=1)
    return round(float(std_dev), 2)

exam_scores = [78, 85, 90, 65, 88, 92, 76]
result = calculate_standard_deviation(exam_scores)
print(f"Exam Scores: {exam_scores}")
print(f"Standard Deviation: {result}")

#------------------------------------------------------------


#   TASK : 3    


import numpy as np

a = [200, 200, 200, 200, 200]
b = [100, 300, 150, 400, 50]

std_a = np.std(a, ddof=0)
std_b = np.std(b, ddof=0)
print(f"Population STD - A: {std_a}, B: {std_b}")

std_a_s = np.std(a, ddof=1)
std_b_s = np.std(b, ddof=1)
print(f"Sample STD - A: {std_a_s}, B: {std_b_s}")



#------------------------------------------------------------


#   TASK : 4


import numpy as np

salaries = [28000, 29000, 27000, 60000, 26500, 27500]


variance = np.var(salaries, ddof=1)
std_dev = np.std(salaries, ddof=1)

print(f"Variance: {variance:,.2f}")
print(f"Standard Deviation: {std_dev:,.2f}")