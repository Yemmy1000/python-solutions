acc_cr = 0
acc_pt = 0
code, cr, grade = input('enter course code: '), input('enter credits:'), input('enter grade: ') #enter grade as 0 for F, 1 for E, 2 for D,  3 for C, 4 for B and 5 for A
acc_cr += cr
acc_pt += cr*grade
code, cr, grade = input('enter course code: '), input('enter credits:'), input('enter grade: ') #enter grade as 0 for F, 1 for E, 2 for D,  3 for C, 4 for B and 5 for A
acc_cr += cr
acc_pt += cr*grade
print('cumulative grade point average is ', format(acc_pt/acc_cr, '.2f'))
