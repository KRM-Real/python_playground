def count_change(change):
    
    total = sum(change) / 100 
    return f"${total:.2f}"

values = [25, 10, 5, 1, 25, 25, 25]
print(count_change(values))