
proposal_dict = {}


def get_proposal_data():
    ref_code = input("Enter Reference Code: ")
    principal_inv = input("Enter Principal Investigator Name: ")
    dept_code = input("Enter Department Code: ")
    college_code = input("Enter College Code: ")
    fund_agency_code = input("Enter Funding agency Code: ")
    prop_title = input("Enter Proposal title: ")
    amt_req = float(input("Amount Requested: "))
    data_str = principal_inv+", "+dept_code+", "+college_code+", "+fund_agency_code+", "+prop_title.upper()+", "+str(amt_req)

    return ref_code, data_str


def add_proposal_data(ref, prop_data, prop_dict):
   if not search_proposal(ref, prop_dict):
      prop_dict[ref] = prop_data
   else:
      print("Proposal data: ", ref, " is already in the dictionary")

def remove_proposal(ref, prop_dict):
    if search_proposal(ref, prop_dict):
       del prop_dict[ref]
    else:
       print("Proposal code: ", ref, " is not found!")

def display_records(prop_dict):
    for ref in prop_dict:
        print(str(ref)+" : "+prop_dict[ref])

def search_proposal(ref, prop_dict):
   return ref in prop_dict

def search_proposal_by_pi(pi_name, prop_dict):
    result = []
    for k, v in prop_dict.items():
        v = v.split(',')
        if v[0] == pi_name :
            result.append(k)
    return result

def search_proposal_by_dpt(dpt_code, prop_dict):
    result = []
    for k, v in prop_dict.items():
        v = v.split(',')
        if v[1] == dpt_code :
            result.append(k)
    return result

def search_proposal_by_coll(coll_code, prop_dict):
    result = []
    for k, v in prop_dict.items():
        v = v.split(',')
        if v[2] == coll_code :
            result.append(k)
    return result



def menu():
    quit = False
    employee_dict = {}
    while not quit:
          command = int(input('\nEnter a code 0- New Proposal,1-search,2-remove, 3-display, 4-quit '))
          if command == 0:
              ref_code, proposal_data = get_proposal_data()
              add_proposal_data(ref_code, proposal_data, proposal_dict)
          elif command == 1:
              search_command = int(input('\nEnter a code 0-Search by Ref No, 1-Search by PI, 2-Search by Department , 3-College, 4-Cancel '))
              if search_command == 0:
                  ref_code = input("Enter reference code: ")
                  if search_proposal(ref_code, proposal_dict):
                      print("Proposal data: ", proposal_dict[ref_code], " is found")
                  else:
                      print("Proposal ref: ", ref_code, " is not found")

              elif search_command == 1:
                  pi_name = input("Enter Principal Investigator's name: ")
                  result = search_proposal_by_pi(pi_name, proposal_dict)
                  if result:
                      print("Proposal Code: ", result, " is found for ",pi_name )
                  else:
                      print("Proposal Code is not found for ",pi_name )

              elif search_command == 2:
                  dpt_code = input("Enter Department code: ")
                  result = search_proposal_by_dpt(dpt_code, proposal_dict)
                  if result:
                      print("Proposal Code: ", result, " is found for ",dpt_code )
                  else:
                      print("Proposal Code is not found for ",dpt_code )

              elif search_command == 3:
                  coll_code = input("Enter College code: ")
                  result = search_proposal_by_coll(coll_code, proposal_dict)
                  if result:
                      print("Proposal Code: ", result, " is found for ",coll_code )
                  else:
                      print("Proposal Code is not found for ",coll_code )


              elif search_command == 4:
                  exit

              else:
                  print("Wrong Search code")


              
          elif command == 2:
              ref_code = input("Enter reference code: ")
              remove_proposal(ref_code, proposal_dict)
          elif command == 3:
              display_records(proposal_dict)
          elif command == 4:
              quit = True
              print("Goodbye!")
          else:
              print("Wrong code")
           
             
menu()
