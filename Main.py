# Contact Manager Group Project #
import random
import os
import math

def main():
    #main accepts no arguments
    #calls menu() for options and choice
    #use choice to call functions or exit program
    try: 
        #welcome message
        print('Welcome to Contact Manager')
        
        #call options
        choice = menu()
        
        #find function to match choice
        while choice >= 1 and choice <= 5
        
            if choice == 1:
                add_contact()
            
            if choice == 2:
                search_contact()
                
            if choice == 3:
                edit_contact()
                
            if choice == 4:
                delete_contact()
                
            if choice == 5:
                display_contacts()
            
        if choice != 6:
            #invalid input
            print('Please enter a number 1-6.')
            
            main()
            
        else:
            #exit message
            print('Thank you for using Contact Manager.')
            
    #error check
    except ValueError as err:
        print(err)
        
    except IOError as err:
        print(err)
        
    except:
        print('An error has occoured, try again later.')
    
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
    
def search_contact():
    #search contact accepts no arguments
    #prompts for a contact tot search for
    #search contacts.txt for contact
    #when found, print
    #if not found display error
    
    try:
        
        #bool for search
        found = False
        
        #get input
        search = input('Enter a Contact to search for: ')
        
        #open
        infile = open('contacts.txt', 'r')
        
        #get desc from file
        name = infile.readline()
        
        #loop
        while desc != '':
            address = infile.readline()
            phone = infile.readline()
            email = infile.readline()
            
            
            #strip \n
            name = name.rstrip('\n')
            
            #determine if record is found
            if name.lower() == search.lower():
                print('\nRecord Found\n')
                print('Name:', name)
                print('Street Address:', address)
                print('Phone Number:', phone)
                print('Email Address:', email)
                found = True
                
            #read next record
            name = infile.readline()
            
        #close
        infile.close()
        
        if not found:
            print('\nThe Contact was not found.')
            
    #error check
    except ValueError as err:
        print(err)
        
    except IOError as err:
        print(err)
        
    except:
        print('An error has occoured, try again later.')
    
def edit_contact(): #kyle
    #edit contact accepts no arguments
    #prompts for a contact to find
    #if not found display error
    #when found prompt for what info to edit
    #use temp to edit contacts.txt
    
    pass
    
def delete_contact():
    #delete conatct accepts no arguments
    #prompts for a contact to delete
    #use temp to remove contact from contacts.txt
    
    pass
    
def display_contacts(): #nolan
    #display contacts accepts no arguments
    #print all contacts in contacts.txt
    
    pass
    