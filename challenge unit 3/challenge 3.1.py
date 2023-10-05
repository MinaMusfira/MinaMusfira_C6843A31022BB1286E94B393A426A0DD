def linear_search_product(product_list, target_product):
# Initialize an empty list to store occurrences of the target product
  occurrences = []
# Loop through the product_list 
  for index, product in enumerate(product_list):
# Check if the current product matches the target product
    if product == target_product:
# If it matches, add the index to the occurrences list
     occurrences.append(index)
     return occurrences
# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(products, target)

if result:
 print(f"The product '{target}' was found at the following indices: {result}")
else:
 print(f"The product '{target}' was not found in the list.")