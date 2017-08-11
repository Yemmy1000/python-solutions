def swap(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp
    return val1, val2

def main():
    val1, val2 = float(input("Enter value 1: ")), float(input("Enter value 2: "))
    print("Your input is in the order ", val1, val2)
    print("Your input order is swapped to ", swap(val1, val2))

main()
