def get_input():
    a = str(input("Enter a string: "))
    return a

def echo(txt):
    a_len = len(txt)  #or a.__len__()
    print("echoing")
    for index in range(a_len):
       print(txt[index], end='')

def r_echo(txt):
    a_len = len(txt)
    for index in range(-1, -a_len-1, -1):
        print('\n',txt[index], end='')

def main():
    txt = get_input()
    echo(txt)
    r_echo(txt)
    
main()








