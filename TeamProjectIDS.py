# Contact Manager Group Project #
import random
import os
import math

def main(): #mason
    #main accepts no arguments
    #calls menu() for options and choice
    #use choice to call functions or exit program
    
    pass
    
def menu(): #nolan
    #menu accepts no arguments
    #outputs list of options
    #prompts for option chosen
    #return choice
    
    pass
    
def add_contact(): #kyle
    #add contact accepts no arguments
    #use file contacts.txt
    #adds a name, address, phone, and email for each contact record
    #ask if more than one contact is being made
    
    another = 'y'
    
    contacts_file = open('contacts.txt', 'a')
    
    while another.lower() == 'y':
        print("Please enter your contact's information:")
        name = input('Name: ')
        st_ad = input('Street Address: ')
        phone = input('Phone Number: ')
        email = input('Email Address: ')
        
        contacts_file.write(name + '\n')
        contacts_file.write(st_ad + '\n')
        contacts_file.write(phone + '\n')
        contacts_file.write(email + '\n')
        
        another = input('Do you wish to add another contact? (y to continue): ')
        
    contacts_file.close()
    
    print('\nAll data added to contacts.txt.')
    
    
def search_contact(): #mason
    #search contact accepts no arguments
    #prompts for a contact tot search for
    #search contacts.txt for contact
    #when found, print
    #if not found display error
    
    pass
    
def edit_contact(): #kyle
    #edit contact accepts no arguments
    #prompts for a contact to find
    #if not found display error
    #when found prompt for what info to edit
    #use temp to edit contacts.txt
    
    pass
    
def delete_contact(): #mason
    #delete conatct accepts no arguments
    #prompts for a contact to delete
    #use temp to remove contact from contacts.txt
    
    pass
    
def display_contacts(): #nolan
    #display contacts accepts no arguments
    #print all contacts in contacts.txt
    
    pass
    