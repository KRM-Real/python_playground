def maxVertical_Area(points):
    
    x_values = [point[0] for point in points]
    x_values.sort()
    
    
    max_gap = 0
    for i in range(1, len(x_values)):
        curr_gap = x_values[i] - x_values[i - 1]
        max_gap = max(curr_gap, max_gap)

    return max_gap

xpoints = [[8,7],[9,9],[7,4],[9,7]]
print(maxVertical_Area(xpoints))