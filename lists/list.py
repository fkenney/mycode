#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
   
    # create a list called list1
    wordbank= ["indentation", "spaces"] 

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
    
    # appends 4 to wordbank
    wordbank.append(4)
    
    #gets input of num from user
    num = int(input("pick a number between 0 and 18: "))
    
    #uses input to slice student list
    student_name = tlgstudents[num: num + 1]

    #pints some stuff out
    print(f"{student_name} always uses {num} {wordbank[1]} to indent")


if __name__ == "__main__":
        main()

