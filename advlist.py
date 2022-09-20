#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #display list1[1] which is arista_eos
    print(list1[1])

    #a second list
    list2 =["juniper"]
    
    #adds list2 to the end of list1
    list1.extend(list2)
    
    #prints list 1
    print(list1)
    
    # create list 3 of ips
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    #appends list1 with list3
    list1.append(list3)


    #prints list1
    print(list1)

    #pints out 5th item on list
    print(list1[4])

    #prints the first item in the nested list
    print(list1[4][0])

if __name__ == "__main__":
        main()

