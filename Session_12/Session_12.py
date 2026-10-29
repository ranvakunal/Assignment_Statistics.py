#       SESSION - 12  MATRIX MULTIPLICATION AND LINEAR REGRESSION MATH INTUITION


#       TASK - 1



import numpy as np


matrix_a = np.array([
    [150, 12],
    [300, 25]
])


matrix_b = np.array([
    [2, 1],
    [1, 3]
])


result_matrix = np.matmul(matrix_a, matrix_b)

print("Resulting Matrix after Multiplication:")
print(result_matrix)

#----------------------------------------------------------------


#       TASK - 2



def linear_regression_predict(x, m, c):
    """
    Calculates and returns the predicted output y for a linear regression equation.
    Formula: y = mx + c
    """
    y = (m * x) + c
    return y


slope = 4
intercept = 10
input_x = 5

predicted_y = linear_regression_predict(input_x, slope, intercept)
print(f"Predicted output (y) for x = {input_x}: {predicted_y}")



#--------------------------------------------------------------------------


#       TASK - 3


def linear_regression_predict(x, m, c):
    return (m * x) + c


m = 4   
c = 10  
distances = [2, 5, 8]  

print("--- Zomato Delivery Time Predictions ---")
for dist in distances:
    predicted_time = linear_regression_predict(dist, m, c)
    print(f"Distance: {dist} km | Predicted Delivery Time: {predicted_time} minutes")