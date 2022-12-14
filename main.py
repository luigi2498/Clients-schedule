import os   # File management library.

DIRECTORY = 'Contacts/'     # Contacts directory.
EXTENSION = '.txt'          # File extension.

class Contact:          # Contact class.
    def __init__(self, name, phone, category):
        self.name = name
        self.phone = phone
        self.category = category

def app():      # Main function.
    os.system('cls')
    makeDir()       # Check if the directory exists.
    displayMenu()   # Display main menu.

    # Input.
    ask = True
    while ask:
        option = int(input('Insert your option: '))
        
        # Execute options.
        if option == 1:
            os.system('cls')
            addNewContact()
            ask = False

        elif option == 2:
            os.system('cls')
            editContact()
            ask = False

        elif option == 3:
            os.system('cls')
            viewContacts()
            ask = False

        elif option == 4:
            os.system('cls')
            searchContact()
            ask = False

        elif option == 5:
            os.system('cls')
            deleteContact()
            ask = False
        
        elif option == 6:
            ask = False
            print('Goodbye...')
        
        else:
            print('Wrong option, try again...')
            input('Press enter to continue.')

def addNewContact():
    print('Add new contact')
    name = input('Contact name: ')

    exists = contactExists(name)

    if not exists:
        with open(DIRECTORY + name + EXTENSION, 'w') as file:
            phone = input('Phone: ')
            category = input('Category: ')

            contact = Contact(name, phone, category)

            file.write('Name: ' + contact.name + '\n')
            file.write('Phone: ' + contact.phone + '\n')
            file.write('Category: ' + contact.category)

            print(f'Contact {contact.name} added successfully.')
    
    else:
        print(f'Contact {name} already exists.')
        input('Press enter to continue...')

    app()   # Restart program...

def editContact():
    print('Edit contact')
    name = input('Contact name: ')

    exists = contactExists(name)

    if exists:
        with open(DIRECTORY + name + EXTENSION, 'w') as file:
            newName = input('Type new name: ')
            newPhone = input('Type new phone: ')
            newCategory = input('Type new category: ')

            contact = Contact(newName, newPhone, newCategory)

            file.write('Name: ' + contact.name + '\n')
            file.write('Phone: ' + contact.phone + '\n')
            file.write('Category: ' + contact.category)

            file.close()    # Close before renaming.

            os.rename(DIRECTORY + name + EXTENSION, DIRECTORY + newName + EXTENSION)

            print('Contact edited successfully...')

    else:
        print(f'Contact {name} doesn\'t exists...')
        input('Press enter to continue...')
    
    app()   # Restart program...

def viewContacts():
    files = os.listdir(DIRECTORY)
    txtFiles = [i for i in files if i.endswith(EXTENSION)]

    for file in txtFiles:
        with open(DIRECTORY + file) as contact:
            for line in contact:
                print(line.rstrip())    # Print content.

            print('\n')                 # Separate contacts.

    input('Press enter to continue...')
    app()
        
def searchContact():
    name = input('Type a contact to search: ')

    try: 
        with open(DIRECTORY + name +  EXTENSION) as contact:
            for line in contact:
                print(line.strip())

            print('\n')
        input('Press enter to continue...')
    
    except IOError:
        print(IOError)
        print('Contact doesn\'t exists.')        
        input('Press enter to continue...')

    app()

def deleteContact():
    name = input('Type the name of a contact to delete: ')

    try:
        os.remove(DIRECTORY + name + EXTENSION)
        print(f'Contact {name} has been deleted successfully!')
        input('Press enter to continue...')

    except:
        print(f'Contact {name} doesn\'t exists...')
        input('Press enter to continue...')

    app()

def displayMenu():
    print('Choose an option')
    print('1. Add new contact.')
    print('2. Edit existing contact.')
    print('3. View contacts.')
    print('4. Search contact.')
    print('5. Delete contact.')
    print('6. Exit.')

def makeDir():  # Function that create a directory.
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)        # Make directory.

def contactExists(name):
    return os.path.isfile(DIRECTORY + name + EXTENSION)

# Main program.
if __name__ == '__main__':
    app()