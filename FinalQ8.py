import numpy as np
sales = np.array([ [120, 150, 135, 170], [ 80, 95, 110, 105],[200, 180, 220, 240]])
total_sales_product = np.sum(sales,axis=1)
total_sales_month = np.sum(sales,axis=0)
print("Total sales of each product: ",total_sales_product)
print("Total sales of each month: ",total_sales_month)
print("Product with highest total sales: ",np.argmax(total_sales_product))
print("Product with lowest total sales: ",np.argmin(total_sales_product))

z=sales.copy()
z[sales<100]=0
print("New sales: ",z)
print("Sales: ",sales)