#!/usr/bin/env python3

def main():
    
    #list of 3 protocolos
    proto = ["ssh", "http", "https"]
    
    #prints list
    print(proto)
    
    #prints second item of list
    print(proto[1])

    #adds item to list
    proto.extend("dns")

    #prints list
    print(proto)


if __name__ == "__main__":
        main()
