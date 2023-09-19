def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example usage
product_list = ["apple", "banana", "orange", "banana", "grape", "banana"]
target = "banana"
result = linear_search_product(product_list, target)
print(result)