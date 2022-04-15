# for loop
# You are going to write a program that calculates the average student height from a List of heights.

# student_heights = [180, 124, 165, 173, 189, 169, 146]`

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
    print(total_height)

count_stu = 0
for num_students in student_heights:
    count_stu += 1
print(count_stu)

avg_stu = round(total_height / count_stu)
print("average students:" + str(avg_stu))
