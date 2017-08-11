correct_answer = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]
stud_ans = []

try:
    ans_fObj = open("student_answer_file.txt", "r")
except Exception as err:
    print(err)

else:
    stud_ans_lst = ans_fObj.readlines()

for item in stud_ans_lst:
    stud_ans.append(item.rstrip('\n'))

print("The List of Correct Answers: \n", correct_answer)



print("The List of Student Supplied Answers: \n",stud_ans)


ans_fObj.close()

correct = 0
wrong = 0
lis_of_wrongly_answered_no = []
for item in range(20):
    
    if correct_answer[item] == stud_ans[item]:
        print("No. " , item+1, " - Correct")
        correct += 1      
    else:
        print("No. " , item+1, " - Incorrect")
        wrong += 1
        lis_of_wrongly_answered_no.append(item+1)

print("\nTotal Number of Correctly Answered Questions: ", correct)
print("Total Number of Incorrectly Answered Questions: ", wrong)
print("The Wrongly Answered Question No.: ", lis_of_wrongly_answered_no)

if correct >= 15:
    print("Student Passed")
else:
    print("Student Failed")
