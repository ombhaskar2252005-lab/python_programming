num_student  = int(input("Enter number of student: "))
scores =[]
for i in range(num_student):
    score = int(input("Enter score: "))
    scores.append(score)

   
passed =0
for score in scores:
    if score>40:
        passed += 1
print("Student passed: " , passed)

lowest = min(scores)
highest = max(scores)
total = sum(scores)
average = total/num_student
print("Lowest Score: ",lowest)
print("Highest Score: ", highest)
print("Total Score: ", total)
print("Average: ", average)
