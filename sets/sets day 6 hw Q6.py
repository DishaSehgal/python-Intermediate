'''
Question 6: Return a set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:
{20, 70, 10, 60}

'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))
