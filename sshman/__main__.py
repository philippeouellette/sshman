#!/usr/bin/python3
import json, os
from bullet import Bullet
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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

    try:
        #Clear()

        public_key = open(os.path.expanduser("~") + '/.ssh/id_rsa.pub','r').read()

        while True:
            #Clear()
            if username := input('username : '):
                if ip := input('ip: '): 
                    break

        #Get the JSON file content to modify
        data = GetInfoFromJSON()

        #Adding the new username and IP
        data['sessions'].append({"username": username, "ip_address": ip})
        
        with open('sessions.json', 'w') as f:
            json.dump(data, f) #Writing in the JSON file

    except:
        pass


def address_selection():
    """Return dict
    
    we fetch existing sessions from json file and display them. 
    Gotta let the user choose which session he wants to use but also let him go back to the main menu."""

    #Clear()
    
    return(Bullet(
        prompt = "\nChoose the ssh session: ",
        choices = list(session['username'] + '@' + session['ip_address'] for session in GetInfoFromJSON()['sessions']), 
        align = 5, 
        margin = 2,
        bullet = "",
        pad_right = 5,
        return_index = True
    ).launch()[0])


def GetInfoFromJSON():
    try:
        with open(ROOT_DIR + '/sessions.json') as file:
            return json.load(file)
    except:
        print("There's an error with the \"sessions.json\" file, exiting...")
        exit()


def launch_ssh_session(session):
    """
    Establises an ssh connection using the 2 keys of the dictionnary received, eg. username and ip_address.
    """
    #Clear()

    returnCode = os.system("ssh " + session)

    if returnCode == 0:
        exit() #Exit the program here because the ssh connection has been made


def main():
    """main function"""    
    try:
        while True:
            #Clear()            
            if "Add" in main_menu(): #Si le mot "Add" se trouve dans l'option choisie par l'utilisateur
                add_new_address()
            else: #Return to the main_menu if we've successfully added a new session, else, launch in the address_selection menu
                try:
                    launch_ssh_session(address_selection())
                except:
                    pass
    except:
        #Clear()
        pass


if __name__== "__main__":
    main()