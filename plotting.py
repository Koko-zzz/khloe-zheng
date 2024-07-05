
# Function to calculate the average of exam marks
def calculate_average(marks):
    total = 0
    valid_marks = []
    average = 0
    for mark in marks:
        if type(mark) != int:
            print(mark, 'is not a valid mark')
        elif mark < 0 or mark > 100:
            print(mark, 'is not between 0 and 100')
        else:
            valid_marks.append(mark)
            total = total + mark
    if len(valid_marks) > 0:
        average = total / len(valid_marks)
    else:
        print('No valid marks were found')
        average = 0
    return average
        

# Normal data - a variety of realistic integer marks
normal_marks = [88, 72, 90, 65, 76, 85, 91, 79, 84, 77]

# Abnormal data - includes non-numeric, negative, and overly high marks
abnormal_marks = [88, 'A', -72, 90, '!', 105, 76, None, 200, 77]

# Boundary conditions - marks at the boundary and just outside
boundary_marks = [0, 100, -1, 101, 0, 100, 1, 99, 0, 100]

# Calculate averages for each set of data
average_normal = calculate_average(normal_marks)
average_abnormal = calculate_average(abnormal_marks)
average_boundary= calculate_average(boundary_marks)

# Display the results
print(f"Average of normal data: {average_normal}")
print(f"Average of abnormal data: {average_abnormal}")
print(f"Average of boundary data: {average_boundary}")
