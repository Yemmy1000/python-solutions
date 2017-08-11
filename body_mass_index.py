def main():
    repeat = False

    while not repeat:
        try:
            weight = float(input("Enter weight in Kg: "))
        except ValueError as err:
            print(err)
            weight = 1.0

        try:
            height = float(input("Enter Height in meter: "))
        except ValueError as err:
            print(err)
            height = 1.0

        
        bmi = body_mass_index(weight, height)
        check_obesity(bmi)    

        try:
            systolic_pressure = float(input("Enter systolic pressures: "))
        except ValueError as err:
            print(err)
            systolic_pressure = 1.0

        try:
            diastolic_pressures = float(input("Enter diastolic pressures: "))
        except ValueError as err:
            print(err)
            diastolic_pressures = 1.0


        mean_arterial_pr, pulse_pr = map_pressure(systolic_pressure, diastolic_pressures)

        check_map(mean_arterial_pr)

        try:
            repeat_code = int(input("Enter 0 to repeat and 1 otherwise: "))
        except ValueError as err:
            print(err)
            repeat = False

        else:
            if repeat_code == 0 :
                repeat = False

            elif repeat_code == 1 :
                repeat = True            
      
    print("....System Exit..... Bye....")

def body_mass_index(wt, ht):
    return wt/ht**2 




def check_obesity(bmi):
    if bmi < 18.5:
        print("Body Mass Index (BMI) ", bmi, " is Underweight")
    elif bmi == 18.5 or bmi > 18.5 or bmi < 25:
        print("Body Mass Index (BMI) ", bmi, " is Normal")
    elif bmi == 25 or bmi > 25 or bmi < 30:
        print("Body Mass Index (BMI) ", bmi, " is Overweight")
    else:
        print("Body Mass Index (BMI) ", bmi, " is Obese")



def map_pressure(sp,dp):
    pulse_pressure = sp-dp
    mean_arterial_pressure = dp + pulse_pressure/3
    return mean_arterial_pressure, pulse_pressure
    
def check_map(map):
    if map < 70 :
        print("Danger! mean arterial pressure is ", format(map, '.5f'), " less than 70")
    else:
        print("Normal! mean arterial pressure is ", format(map, '.5f'), " 70 or above")
        
    
main()





