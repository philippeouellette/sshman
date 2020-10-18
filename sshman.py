#!/usr/bin/python3
import json,os, getpass
os.system('clear')

def main_menu():
    """Main menu function. Simply asks a question that determines the next action for the program."""
    return input("Do you wanna 1) add an ip address or 2) use an existing one")

def new_address():
    """Here, we get a new session that we save in sessions.json 
    file. We also copy our public ssh key to the remote device."""
    public_key=open('/home/' + getpass.getuser() + '/.ssh/id_rsa.pub','r').read()
    username = input('username: ')
    ip = input('ip: ')
    

def existing_address():
    """we fetch existing sessions from json file and display them. 
    Gotta let the user choose which session he wants to use but also let him go back to the main menu."""


    #   asdsdasdas ads asd 


    with open('sessions.json') as file:
        data = json.load(file)

    for session in data['sessions']:
        print(session['username'])

def main():
    """main function"""
    print(new_address())

if __name__=="__main__":
    main()