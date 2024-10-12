'''Notes on the sum function and built in functions'''

student_scores = [180, 124, 165, 173, 189, 169, 146]

# This built in function
total_exam_score = sum(student_scores)
print(total_exam_score)

# Is the same as..
final = 0
for score in student_scores:
    final += score
    print(final)

# The max function built in
print(max(student_scores))

# Creating the max function with a for loop
HIGH = 0
for score in student_scores:
    if score > HIGH:
        HIGH = score

print(HIGH)
