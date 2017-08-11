
def search_doc(term, search_file):
    no_of_item = 0
    rec_found = False
    fileObj = open(search_file, 'r')
    file_rec =fileObj.readlines()
    for rec in range(len(file_rec)) :
        if term in file_rec[rec] :
             no_of_item += 1
    fileObj.close()

    return no_of_item



def main():
    term = input("Enter the name of employee to search: ")
    no_found = search_doc(term, 'Reference.txt')
    print("Employee ",term , "is found!", no_found)
            


main()
