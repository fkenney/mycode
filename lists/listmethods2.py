#!/usr/bin/env python3
    
def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    
    print(proto)
    
    proto.append("dns") # this line will add "dns" to the end of our list
    
    protoa.append("dns") # this line will add "dns" to the end of our list
    
    print(proto)
    proto2 = [ 22, 80, 443, 53 ] # a list of common ports
    
    proto.extend(proto2) # pass proto2 as an argument to the extend method
    print(proto)
    
    protoa.append(proto2) # pass proto2 as an argument to the append method
    
    #copys proto2 list into mylist
    mylist = proto2.copy()
    
    #prints the count of number 4 
    print(mylist.count(443))
    
    #pints my list
    print(f"my list - {mylist}")
    
    #pints protoa list
    print(protoa)

if __name__ == "__main__":
        main()
