
def amort(p, r, n):
    a = p * (1+r /1200)**(12*n)
    return a

def main():
    principal, annual_perc_rate, years = float(input("Enter principal: ")), float(input("Enter annual rate in percentage: ")), float(input("Enter number of years: "))
    amortization = amort(principal, annual_perc_rate, years)
    print("The total investment is", format(amortization, '.2f'))

main()
