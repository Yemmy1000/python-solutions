

correct_answer = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]
stud_ans = []

ans_fObj = open("student_answer.txt", "r")

stud_ans_lst = ans_fObj.readlines()
for item in stud_ans_lst:
    stud_ans.append(item.rstrip('\n'))

print(stud_ans)
print(correct_answer)
ans_fObj.close()

correct = 0
wrong = 0
for item in range(20):
    
    if correct_answer[item] == stud_ans[item]:
        print("Question " , item+1, " - Correct")
        correct += 1      
    else:
        print("Question " , item+1, " - Incorrect")
        wrong += 1 

print("\nTotal Number of Correctly Answered Questions: ", correct)
print("Total Number of Incorrectly Answered Questions: ", wrong)

if correct >= 15:
    print("Student Passed")
else:
    print("Student Failed")
