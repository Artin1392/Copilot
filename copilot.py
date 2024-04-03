# While key
app = True

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

# Exit
def Exit():
    app = False
    return app
    


# While loop
while(app):
    inp = input()
    try: 
        
        if inp.lower() == "write a song":
            was()

        elif inp.lower() == "echo":
            Echo()

        elif inp.lower() == "exit":
            break
    
    except:
        print("Sorry, an error occured\n")

