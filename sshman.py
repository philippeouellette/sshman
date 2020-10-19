#!/usr/bin/python3
import json,os, getpass
from bullet import Bullet
from collections import OrderedDict

os.system('clear')

def main_menu():
    """Return string
    
    Main menu function. Simply asks a question that determines the next action for the program."""
    choice=''
    while choice not in ['1','2']:
        choice = input("Do you wanna 1) add an ip address or 2) use an existing one: ")
    return choice


def add_new_address():
    """Here, we get a new session that we save in sessions.json 
    file. We also copy our public ssh key to the remote device."""

    public_key=open('/home/' + getpass.getuser() + '/.ssh/id_rsa.pub','r').read()
    username=input('username: ')
    ip=input('ip: ')
    
    #add to json file
    #return to main menu


def address_selection():
    """Return dict
    
    we fetch existing sessions from json file and display them. 
    Gotta let the user choose which session he wants to use but also let him go back to the main menu."""
    os.system('clear')
    with open('sessions.json') as file:
        data = json.load(file)
    
    return(Bullet(
        prompt = "\nChoose the ssh session: ",
        choices = list(OrderedDict.fromkeys(session['username']+'@'+session['ip_address'] for session in data['sessions'])), 
        indent = 0,
        align = 5, 
        margin = 2,
        shift = 0,
        bullet = "",
        pad_right = 5,
        return_index = True
    ).launch()[0])
    
    #session selection and then we return the session the user chooses as a dict.

def launch_ssh_session(session):
    """
    Establises an ssh connection using the 2 keys of the dictionnary received, eg. username and ip_address.
    """
    print("\nLaunching connection to " + session +" ...")
    

def main():
    """main function"""

    while main_menu() == "1":
        add_new_address()
    
    launch_ssh_session(address_selection())
    


if __name__== "__main__":
    main()