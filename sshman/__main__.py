#!/usr/bin/python3
import os, csv
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
    """Here, we get a new session that we save in sessions.csv 
    file. We also copy our public ssh key to the remote device."""

    try:
        Clear()

        #public_key = open(os.path.expanduser("~") + '/.ssh/id_rsa.pub','r').read()

        while True:
            Clear()
            if username := input('username : '):
                if ip := input('ip: '): 
                    break

        WriteCSV(username, ip, "keyfile", "password")

    except:
        pass


def WriteCSV(username, ip, keyfile, password):
    try:
        with open(ROOT_DIR + '/sessions.csv', 'a') as f:
            writer = csv.writer(f)

            #Each rows in the .csv
            client = username + "@" + ip
            keyfile = ""
            password = ""

            writer.writerow([client, keyfile, password]) #Write in the .csv
    except:
        print("There's an error in the csv file")


def ReadCSV(col): #What col of the csv we want to print (0=client 1=keyfile 2=password)
    try:
        with open(ROOT_DIR + '/sessions.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')

            return list(row[col] for row in reader)
    except:
        print("There's an error in the csv file")


def address_selection():
    """Return dict
    
    we fetch existing sessions from csv file and display them. 
    Gotta let the user choose which session he wants to use but also let him go back to the main menu."""

    Clear()

    return(Bullet(
        prompt = "\nChoose the ssh session: ",
        choices = list(ReadCSV(0)), 
        align = 5, 
        margin = 2,
        bullet = "",
        pad_right = 5,
        return_index = True
    ).launch()[0])


def launch_ssh_session(session):
    """
    Establises an ssh connection using the 2 keys of the dictionnary received, eg. username and ip_address.
    """

    returnCode = os.system("ssh " + session)

    if returnCode == 0:
        exit() #Exit the program here because the ssh connection has been made
    else:
        #We could output an error message to the user saying that the connection to the ssh server has been lost
        pass


def main():
    """main function"""    
    try:
        while True:
            Clear()            
            if "Add" in main_menu(): #Si le mot "Add" se trouve dans l'option choisie par l'utilisateur
                add_new_address()
            else: #Return to the main_menu if we've successfully added a new session, else, launch in the address_selection menu
                try:
                    launch_ssh_session(address_selection())
                except:
                    pass
    except:      
        Clear()
        exit()


if __name__== "__main__":
    main()