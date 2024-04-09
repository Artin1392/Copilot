# Imports


# Variables
app = True
Commands = ["write a song", "echo", "read", "create", "exit", "help"]

# Introduce
print("Hello! I am Copilot, your friendly AI assistant.")
print('What can I do for you?')

# Functions

# Write a song
def was():
    song = "I'm a great singer.\nBut what about you?\nYeah,Yeah you are a bad singer.\n Ha, Ha, Ha, HaHaHaHa"
    print(song)

# Echo
def Echo():
    text = input('Just say something:\n')
    print(text)

# Read
def Read():
    directory = input('Enter directory:\n')
    try:
        file = open(directory, "r")
        print(file.read())
    except:
        print("Error: Invalid directory.")

# Create
def Create():
    print(' Important point: format of your file will be .txt!\n')
    directory = input('Enter directory:\n')
    text = input('Enter text:\n')
    try:
        file = open( directory + ".txt", "w")
        file.write(text)
        print("Successfully created " + file.name)
    except:
        print(" An error occured.")

# Exit
def Exit():
    app = False
    return app
    
# Help
def Help():
    print(" These are all of our commands: ")
    for command in Commands:
        print("\n//-" + command + "-//")

# While loop
while(app):
    inp = input()
    try: 
        
        if inp.lower() == "write a song":
            was()

        elif inp.lower() == "echo":
            Echo()

        elif inp.lower() == "read":
            Read()

        elif inp.lower() == "create":
            Create()

        elif inp.lower() == "exit":
            print("Bye :)")
            break
        
        elif inp.lower() == "help":
            Help()

        else:
            print("Sorry, an error occured\n")
    except:
        break
