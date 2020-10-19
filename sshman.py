#!/usr/bin/python3
import json,os, getpass
from bullet import Bullet
from collections import OrderedDict


def Clear():
    os.system('clear')


def main_menu():
    """Return string
    Main menu function. Simply asks a question that determines the next action for the program."""

    return(Bullet(
        prompt = "\nChoose an option: ",
        choices = ["Use an existing IP address", "Add an IP address"], 
        indent = 0,
        align = 5, 
        margin = 2,
        shift = 0,
        bullet = "",
        pad_right = 5,
        return_index = True
    ).launch()[0])


def add_new_address():
    """Here, we get a new session that we save in sessions.json 
    file. We also copy our public ssh key to the remote device."""

    public_key = open('/home/' + getpass.getuser() + '/.ssh/id_rsa.pub','r').read()
    username = input('username: ')
    ip = input('ip: ')
    
    #add to json file
    #return to main menu


def address_selection():
    """Return dict
    
    we fetch existing sessions from json file and display them. 
    Gotta let the user choose which session he wants to use but also let him go back to the main menu."""

    Clear()
    
    return(Bullet(
        prompt = "\nChoose the ssh session: ",
        choices = list(OrderedDict.fromkeys(session['username'] + '@' + session['ip_address'] for session in GetInfoFromJSON()['sessions'])), 
        align = 5, 
        margin = 2,
        bullet = "",
        pad_right = 5,
        return_index = True
    ).launch()[0])
    
    #session selection and then we return the session the user chooses as a dick.


def GetInfoFromJSON():
    try:
        with open('sessions.json') as file:
            return json.load(file)
    except:
        print("There's an error with the \"sessions.json\" file, exiting...")
        exit()


def launch_ssh_session(session):
    """
    Establises an ssh connection using the 2 keys of the dictionnary received, eg. username and ip_address.
    """
    Clear()
    os.system("ssh " + session)
    

def main():
    """main function"""

    Clear()

    if "Add" in main_menu(): #Si le mot "Add" se trouve dans l'option choisie par l'utilisateur
        add_new_address()
    
    launch_ssh_session(address_selection())
    

if __name__== "__main__":
    main()