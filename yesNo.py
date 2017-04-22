# http://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input

def getyn(message):
    reply = str(input(message+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return getyn("Uhhhh... please enter ")

def pause(message):
    reply = str(input(message)).lower().strip()

if __name__ == "__main__":
    print("getyn coming...")
    result = getyn("Get a yes or no.")
    if result:
        print("got a yes")
    else:
        print("got a no")
    print("getyn done...")

    print("pause coming...")
    pause("Tap ENTER to continue...")
    print("pause done...")
