g =  9.8067

def displacement(velocity, t_travel):
    return velocity + 0.5*g*t_travel**2

def main():
    velocity, time_travel = float(input("Enter velocity: ")), float(input("Enter time travel: "))
    displ = displacement(velocity, time_travel)
    print (format(displ, '.3f'))

main()
