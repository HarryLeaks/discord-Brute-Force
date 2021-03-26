import ctypes, os, threading, strgen, base64
tokenid = "USER ID HERE"
isSame = False

class Discord:
    def __init__(self):
        self.regularExpression = ".([a-zA-Z0-9]{6})\.([a-zA-Z0-9-\/+_]{27})" # This is the regular expression for discord.
        self.generated = 0

    def generate(self):
        global isSame
        discordToken = strgen.StringGenerator(self.regularExpression).render()
        discordToken = discordToken.replace("..", ".")
        discordToken = str(id) + discordToken 
        if os.path.isfile("./tokens.txt"):
            self.check_is_in(discordToken)
        if isSame == False:
            print(discordToken)
            self.generated += 1
            self.write(discordToken)
            self.title()
        else:
            isSame = False

    def check_is_in(self, discordToken):
        file = open("./tokens.txt", "r")
        Lines = file.readline()
        while True: 
            if(discordToken == Lines):
                isSame = True
                break
            Lines = file.readline()
            if not Lines:
                break
        if os.path.isfile("./tokens.txt"):
            file.close()

    def new_method(self):
        return self.regularExpression
    
    def write(self, discordToken):
        if os.path.isfile("./tokens.txt"):
            writeToken = open("./tokens.txt", "a")
            writeToken.write(f"{discordToken}\n")
        else:
            open("./tokens.txt", "w").close() # Simply create the file.

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"Created by Calastrophe#5752 && HarryLeaks: {self.generated}")


open("./tokens.txt", "w").close() # Create and clear our token file each time
token = Discord()

amountToGen = 30 #It will create 30000 tokens

id = base64.b64encode(tokenid.encode("ascii"))
id = str(id)[2:-1]

for _ in range(amountToGen):
    threading.Thread(target=token.generate).start()