#!/usr/bin/python3
import os, csv
from bullet import Bullet
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def Clear():
    os.system('clear')


def CreateBulletList(mainMessage, listOfChoice):
    return(Bullet(
        prompt = mainMessage,
        choices = listOfChoice, 
        indent = 0,
        align = 5, 
        margin = 2,
        shift = 0,
        bullet = "",
        pad_right = 5,
        return_index = True
    )).launch()[0]


def main_menu():
    """Return string
    Main menu function. Simply asks a question that determines the next action for the program."""

    return CreateBulletList("\nChoose an option: ", ["Use an existing IP address", "Add an IP address", "Remove an IP address"])


def add_new_address():
    """Here, we get a new session that we save in sessions.csv 
    file. We also copy our public ssh key to the remote device."""

    try:
        Clear()

        while True:
            Clear()

            if username := input('Username: ').strip():
                if ip := input('IP: ').strip(): 
                    client = username + "@" + ip

                    #Protection for dupplicates
                    if client in ReadCSV(0): 
                        Clear()
                        input("This user already exists...\nPress ENTER")
                        return

                    #Manage the identify file
                    while True:
                        identityFile = input('Identify file: ')

                        if os.path.isfile(identityFile) or identityFile.strip() == "": #If the identify file exist
                            break
                        
                        Clear()
                        
                    break

        WriteCSV(client, identityFile, "")

    except: pass


def WriteCSV(client, identityFile, password):
    try:
        with open(ROOT_DIR + '/sessions.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([client, identityFile, password]) #Write in the .csv
    except:
        print("There's an error in the csv file")


def ReadCSV(col): #What col of the csv we want to print (0=client, 1=identityFile, 2=password, all=all)
    try:
        with open(ROOT_DIR + '/sessions.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')

            if col != "all":
                return list(row[col] for row in reader)
            return list(row for row in reader)

    except:
        print("There's an error in the csv file")


def RetrieveInfoFromClient(client): #Retrieve the row in the .csv from the user@ip
    for row in ReadCSV("all"):
        if row[0] == client:
            return row


def address_selection():
    """Return dict
    
    we fetch existing sessions from csv file and display them. 
    Gotta let the user choose which session he wants to use but also let him go back to the main menu."""

    Clear()
    
    choice = CreateBulletList("\nChoose the ssh session: ", list(ReadCSV(0)))

    return RetrieveInfoFromClient(choice)


def launch_ssh_session(session):
    """
    Establises an ssh connection using the 2 keys of the dictionnary received, eg. username and ip_address.
    """

    Clear()

    if session[1]:
            returnCode = os.system("ssh " + session[0] + " -i " + session[1])
    else:
        returnCode = os.system("ssh " + session[0])

    #Handle problems with ssh (Return code 0 = GOOD)
    if returnCode == 0: exit() #Exit the program here because the ssh connection has been made
    else: input("There was an error with the ssh session...\nPress ENTER")  


def RemoveClient():
    Clear()

    csvContent = ReadCSV("all") #Save the .csv content before deleting it
    clientToDel = CreateBulletList("\nChoose the ssh session: ", list(ReadCSV(0)))

    open(ROOT_DIR + '/sessions.csv', 'w').close() #Erase the .csv file

    for i in csvContent:
        if i[0] != clientToDel:
            WriteCSV(i[0], i[1], i[2])


def main():
    """main function"""    
    try:
        while True:
            Clear()         

            choice = main_menu()
            
            if "Add" in choice: #Si le mot "Add" se trouve dans l'option choisie par l'utilisateur
                add_new_address()
            elif "Remove" in choice: #Si le mot "Add" se trouve dans l'option choisie par l'utilisateur
                RemoveClient()
            else: #Return to the main_menu if we've successfully added a new session, else, launch in the address_selection menu
                try: launch_ssh_session(address_selection()) 
                except: pass #When we Ctrl+C
    except:  
        Clear()
        exit()


if __name__== "__main__":
    main()