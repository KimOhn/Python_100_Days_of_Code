#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt","r") as names:
    guests = names.readlines() # creates lists for each new line

with open("./Input/Letters/starting_letter.txt","r") as letter:
   draft = letter.read() # creates a single string, not a list
#Replace the [name] placeholder with the actual name.

output_path = "./Output/ReadyToSend/"
for guest in guests:
    guest = guest.strip()
    new_string = draft.replace("[name]", guest)
    with open(f"{output_path} letter to {guest}.txt","w") as invite:
        invite.write(new_string)
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp