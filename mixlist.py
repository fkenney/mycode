#!/usr/bin/env python3

def main():
    #creats list of three items
    my_list = [ "192.168.0.5", 5060, "UP" ]

    #creates list of IPs
    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1"]

    #prints first item in list
    print(f"The first item in the list (IP): {my_list[0]}")
    
    #prints second  item in list
    print(f"The second item in the list (port): {my_list[1]}")

    #prints last item in the list
    print(f"The last item in the list (state): {my_list[2]}")

    #prints last two IPs
    print(f"Last two IPs of iplist are {iplist[-2: ]} ")

if __name__ == "__main__": 
        main()
