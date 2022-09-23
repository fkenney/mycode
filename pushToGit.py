#!/usr/bin/env python3

from git import Repo

repo = Repo('~/mycode/')

def main():
    
    message = input("What is your commit: ") 

    repo.git.add('--all')
    
    repo.git.commit('-m', message , author='fkenney')
    
    origin = repo.remote(name='origin')
    
    origin.push()

if __name__ == "__main__":
        main()
