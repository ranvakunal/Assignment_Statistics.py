#       SESSION - 11


#       TASK - 1



song_durations = [210, 180, 245, 200, 175]


total_duration = sum(song_durations)

print(f"Song Durations: {song_durations}")
print(f"Total duration of the playlist: {total_duration} seconds")


#------------------------------------------------------------------



#       TASK - 2


swiggy_ratings = [
    [4, 5, 3],  
    [2, 4, 5],  
    [5, 3, 4]   
]

print("Swiggy Ratings Matrix:")
for row in swiggy_ratings:
    print(row)


print("\nRatings for the second food item:")
for i, row in enumerate(swiggy_ratings, start=1):
    print(f"Friend {i}: {row[1]}")


#----------------------------------------------------------------


#       TASK - 3


import numpy as np


orders_matrix = np.array([
    [10, 25, 15, 30], 
    [12, 30, 20, 25],  
    [15, 22, 18, 35]  
])


total_orders_per_dish = np.sum(orders_matrix, axis=0)

print("Total orders for each dish:")
for i, total in enumerate(total_orders_per_dish, start=1):
    print(f"Dish {i}: {total} orders")

#----------------------------------------------------------


#       TASK - 4


flipkart_products = [
    [15000, 40], 
    [450, 250],  
    [2999, 100],  
    [899, 75],    
    [45000, 10]   
]

def calculate_product_revenue(product_matrix):
    """
    Calculates and prints total revenue for each product 
    by multiplying price (index 0) and quantity sold (index 1).
    """
    print("--- Flipkart Product Revenues ---")
    for i, row in enumerate(product_matrix, start=1):
        price = row[0]
        quantity = row[1]
        revenue = price * quantity
        print(f"Product {i}: Price = ₹{price}, Quantity = {quantity} | Total Revenue = ₹{revenue:,}")


calculate_product_revenue(flipkart_products)