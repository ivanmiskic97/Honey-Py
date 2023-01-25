# To test on a local machine, we recommend installing telnet (brew install telnet, etc.) for testing purposes.
# This program is optimized for linux machines.

# Color Variables
Red='\033[0;31m'            # Red
Yellow='\033[0;33m'         # Yellow
Blue='\033[0;34m'           # Blue
Green='\033[0;32m'          # Green
Purple='\033[0;35m'         # Purple
Cyan='\033[0;36m'           # Cyan
Color_Off='\033[0m'         # Text Reset
On_IYellow = '\033[0;103m'  # High Intensity Yellow Background ; may not convert via colorama if on Windows 
On_IRed = '\033[0;101m'     # High Inensity Red Background ; may not convert via colorama if on Windows 
Red = '\033[0;31m'          # Red text

# Splash / Intro Page =
print (On_IYellow+"                                                                               "+Color_Off)
print (On_IYellow+"  /$$   /$$                                               /$$$$$$$             "+Color_Off)
print (On_IYellow+" | $$  | $$                                              | $$__  $$            "+Color_Off)
print (On_IYellow+" | $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$      | $$  \ $$ /$$   /$$  "+Color_Off)
print (On_IYellow+" | $$$$$$$$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$      | $$$$$$$/| $$  | $$  "+Color_Off)
print (On_IYellow+" | $$__  $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  | $$      | $$____/ | $$  | $$  "+Color_Off)
print (On_IYellow+" | $$  | $$| $$  | $$| $$  | $$| $$_____/| $$  | $$      | $$      | $$  | $$  "+Color_Off)
print (On_IYellow+" | $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$      | $$      |  $$$$$$$  "+Color_Off)
print (On_IYellow+" |__/  |__/ \______/ |__/  |__/ \_______/ \____  $$      |__/       \____  $$  "+Color_Off)
print (On_IYellow+"                                          /$$  | $$                 /$$  | $$  "+Color_Off)
print (On_IYellow+"                                         |  $$$$$$/                |  $$$$$$/  "+Color_Off)
print (On_IYellow+"                                          \______/                  \______/   "+Color_Off)
print (On_IYellow+"                                                                               "+Color_Off+"\n")
print(            "  🐝🥧     Created by Isabella Tantillo, Ivan Miskic, and Derek Fong      🐝🥧   "+"\n")

# Main code as function
def honeypot_project_main_code () :
    # Variables defined here to ensure they work throughout loops.
    from datetime import datetime, timedelta    # For converting end / start time of honeypot
    import time                                 # For sleep function to work
    import socket                               # For honeypot to define ports and connections
    honeypot_loop = False                       # If set True, enables honeypot mode
    firewall_loop = False                       # If set True, enables firewall creator mode
    help_loop = False                           # If set True, goes to help / man page.
    snort_loop = False                          # If set True, enables snort mode
    import os                                   # For determining desktop path
    import sys                                  # For determining desktop path
    from sys import platform                    # For determining desktop path
    from threading import Timer                 # Allows honeypot to close after N seconds
    ### emoji_remover = False                   # DO NOT ENABLE, LEAVE COMMENTED. If set True, disables Emojis.

    try :                 
        if platform.lower() == "linux" or platform.lower() == "linux2":  # Linux Desktop path with slash added for file support when opening log file.
            download_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/')
        if platform.lower() == "darwin":  # Mac OSX Desktop path with slash added for file support when opening log file.
            download_dir = os.path.join(os.path.expanduser('~'), 'Desktop/')
        if platform.lower() == "win32":  # Windows Desktop path with slash added for file support when opening log file.
            download_dir = f"{os.getenv('USERPROFILE')}\\Desktop\\"
            try : 
                import colorama     # On Windows specifically, this allows for colors to be interperted correctly.      
                colorama.init()     # On Windows specifically, this allows for colors to be interperted correctly. 
            except : 
                pass
    except :
        save_location_warning = True    # If OS can not be detected, files save in current working directory. 

    # INTRO SELECTION CODE
    while True:
        try : 
            if save_location_warning == True :
                print (On_IRed+" WARNING! Can not determine OS environment. Log files will be saved in current working directory, not the Desktop as intended. Type HELP for more info or use the manual_save option. "+Color_Off) 
        except : 
            pass 
        print ("\n")
        user_input = input("Select a mode to run Honey Py in = ( "+Yellow+"HONEYPOT"+Color_Off+" / "+Red+"FIREWALL"+Color_Off+" / "+Purple+"SNORT"+Color_Off+" / "+Blue+"HELP"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
        if user_input.lower() == "honeypot" :
            honeypot_loop = True
            break
        if user_input.lower() == "firewall" :
            firewall_loop = True
            break
        if user_input.lower() == "snort" :
            snort_loop = True
            break
        if user_input.lower() == "help" :
            help_loop = True
            break
        if user_input.lower() == "quit":
            print ("Thank you for using Honey Py!")
            sys.exit()
        if user_input.lower() == "disable_emoji" :
            print ("Emojis are now disabled. You will need to manually set this each time you restart."+"\n")
            emoji_remover = True
        if user_input.lower() == "enable_emoji" :
            print ("Emojis are now enabled 👍. They are enabled by default at the start of the program."+"\n")
            emoji_remover = False
        if user_input.lower() == "manual_save" :
            while True :
                download_location = input("Where would you like to save log files? Please specifify the ABSOLUTE path with a forwardslash or backslash at the end (ex: ~/Desktop/ wont work)"+"\n")
                print ("Is this correct? Please note it MUST have a forwardslash or backslash at the end of the path="+"\n")
                print (download_location)
                download_decision = input ("( "+Green+"YES"+Color_Off+" / "+Red+"NO"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
                if download_decision.lower() == "yes" :
                    download_dir = download_location
                    print ("Log files will now be saved in",download_location)
                    break
                if download_decision.lower() == "no" :
                    pass
                if download_decision.lower() == "quit" :
                    print ("Thank you for using Honey Py!")
                    sys.exit()
        else :
            print ("Please input either ( HONEYPOT / FIREWALL / HELP / QUIT ).")

    # HONEYPOT CODE
    if honeypot_loop == True : 
        try :
            if emoji_remover == True :
                print("                           "+Yellow+"Starting Honeypot Mode"+Color_Off+"\n")
        except :
            print("\n")
            print("                         🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯")
            print("                         🍯 "+Yellow+"Starting Honeypot Mode"+Color_Off+" 🍯")
            print("                         🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯🍯"+"\n")
        HOST = ''   # Left blank as this will be defined by our attacker's IP address
        while True : 
            user_input = input( "Please select a port for the Honeypot (23 is recommended) ( "+Purple+"<PORT NUMBER>"+Color_Off+" / "+Cyan+"BACK"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
            if user_input.lower() == "quit" :
                print ("Thank you for using Honey Py!")
                sys.exit()
            if user_input.lower() == "back" :
                while True:
                    honeypot_project_main_code()
            try : 
                if int(user_input) > 0 and int(user_input) <= 6535:
                    PORT = int(user_input)
                    break
                else : 
                    print(Red+"Please input a valid port number (0-65535)"+Color_Off) # Error if a casting to int causes no errors (Ex: 123456789)
            except : 
                print (Red+"Please input a valid port number (0-6535)"+Color_Off) # Error if casting to int is invalid (ex: "five" or a non numeric value as a str)
        try : 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, PORT))
            s.listen(5)
        except : 
            print (Red+"FATAL ERROR! TRY A DIFFERENT PORT."+Color_Off)
            sys.exit()
        print ("")
        print("To test locally, type the following in a terminal="+"\n")
        print("telnet localhost",str(PORT)+"\n")         
        #__________________________________________________
        def exitfunc():     # Closes the Honeypot foricibly with os._exit(0). exit(),etc., does not end it.
            print("")
            try : 
                if save_location_warning == True :
                    
                    print ("A log file called Honeypot_Log.txt will be created in the current directory if traffic was found.")
                    print ("Thank you for using Honey Py!")
            except : 
                print ("A log file called Honeypot_Log.txt will be created at "+download_dir[:-1]+" if traffic was found.")
                print ("Thank you for using Honey Py!")
            os._exit(0)
            
        while True: 
            user_input = input("How many minutes would you like to run the Honeypot? ( "+Purple+"<MINUTES>"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
            if user_input == "quit" :
                print ("Thank you for using Honey Py!")
                sys.exit()
            try :
                run_timer_in_seconds = int(user_input)*60   # converts minutes to seconds
                break
            except : 
                print ("Please input a valid number!")

        # Time variables for determing start / exit of Honeypot. Defined here so current time is accurate. 
        now = datetime.now()                                                # Current time
        Starting_Date_String = now.strftime("%m/%d/%Y %H:%M:%S")            # Current time converted to readable format
        later = datetime.now() + timedelta(seconds=run_timer_in_seconds)    # Time plus user input of seconds
        Later_Date_String = later.strftime("%m/%d/%Y %H:%M:%S")             # New time covnerted to readable format
        print ("")
        print ("Honeypot started  at  = ", Starting_Date_String)            
        print ("Honeypot will end at  = ", Later_Date_String)
        print ("\n")

        Timer(run_timer_in_seconds, exitfunc).start() # calls exit function in N seconds.
        while True:
            from datetime import datetime 
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
            connect, addr = s.accept() # While loop will idle here until a connection is made, and then will proceeed below.
            try : 
                if save_location_warning == True :
                    log = open("Honeypot_Log.txt", "a") # Creates log file in current directory; allows it to be ammended 
            except :
                log = open(download_dir+"Honeypot_Log.txt", "a") # Creates log file in desktop or a user defined path; allows it to be ammended  
            try :
                log.write(dt_string+" ")    # Prints the date and time for the log 
                log.write(str(addr[0]+" ")) # Writes to log file the IP address and not the random port 
                log.write("\n")             # Startes a newline for the log. 
                log.close()                 # Closes log file (necessary for program,apparently)
                print(On_IRed+" ALERT! "+Color_Off+" Connected by: ", str(addr[0]), " on ", dt_string)
                connect.send(("Welcome to Microsoft Client").encode())
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("Escape Character is 'CTRL+]'").encode())
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("You are about to send your password information to a remote").encode())
                connect.send(("\r\n").encode())
                connect.send(("computer in Internet zone. This might not be safe.").encode())
                connect.send(("\r\n").encode())
                connect.send(("Do you want to send anyway(y/n):").encode())
                time.sleep(3)  # Timer here to give the illusion of a fake login
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("Telnet server could not log you in using NTLM authentication.").encode())
                connect.send(("\r\n").encode())
                connect.send(("Your password may have been expired. Login using username and password").encode())
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("Welcome to Microsoft Telnet Service").encode())
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("login:").encode())
                time.sleep(3)   # Timer here to give the illusion of a fake login
                connect.send(("\r\n").encode())
                connect.send(("\r\n").encode())
                connect.send(("password:").encode())
                time.sleep(3)   # Timer here to give the illusion of a fake login
                connect.close() # Ends attacker's connection, regardless of input. 
            except :
                pass

    # FIREWALL CODE
    if firewall_loop == True:
        try : 
            if emoji_remover == True :
                print("                           "+Red+"Starting Firewall Mode"+Color_Off+"\n")
        except :
            print ("\n")
            print("                         🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
            print("                         🔥 "+Red+"Starting Firewall Mode"+Color_Off+" 🔥")
            print("                         🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥"+"\n")
        def intro():
            print("Firewall mode will assist you in creating a new rule from information we gathered")
            print("from our Honeypot (see Honeypot_Log.txt saved on the Desktop).")
            print("")
            print("An IP address was detected within our Honeypot system. We have identified the")
            print("machine in question and found that they may have malicious intent.")
            print("")
            print("")
        #__________________________________________________
        def make_firewall():
            while True:
                print("Would you like to create a new firewall rule?")
                print("")
                choose = input("Please enter ( "+Green+"YES"+Color_Off+" / "+Red+"NO"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
                print("")
                choose = choose.lower()
                if choose == "yes":
                    print("Please choose a permission for your firewall rule.")
                    print("ALLOW")
                    print("DENY")
                    permission = input(">")
                    permission = permission.upper()
                    if (permission == "ALLOW") or (permission =="DENY"):
                        print(f"You have chosen {permission}.")
                        break
                if choose == "no":
                    print("Exiting out of Firewall Mode.")
                    while True : 
                        honeypot_project_main_code()
                if choose == "quit" : 
                    print ("Thank you for using Honey Py!")
                    sys.exit()
        #____________________________________________________
            while True:
                print("")
                print("Please choose a protocol:")
                print("IP")
                print("TCP")
                print("UDP")
                print("TCP/UDP")
                print("ICMP")
                protocol = input(">")
                protocol = protocol.upper()
                if (protocol == "IP") or (protocol == "TCP") or (protocol == "UDP") or (protocol == "TCP/UDP") or (protocol == "ICMP"):
                    print(f"You have chose {protocol} as your protocol.")
                    break
                else:
                    print("That is not one of the above protocols. Please choose again.")
                print()
        #__________________________________________________
            while True:
                print("Please enter source IP.")
                src = input(">")
                print(f"The source IP is {src}")
                print("")
                print("Please enter the source port or use (any) to include all ports.")
                src_port = input(">")
                print(f"You have chosen {src_port} as your source port.")
                print("")
                print("Please enter destination IP.")
                dest = input(">")
                print(f"The destination IP is {dest}")
                print("")
                print("Please enter the destination port or use (any) to include all ports.")
                dest_port = input(">")
                print(f"You have chosen {dest_port} as your destination port.")
                print("")
                print("")
                print("Here is your completed firewall rule:")
                print("")
                print(f"{permission} | {protocol} | {src} | {src_port} | {dest} | {dest_port}")
                break

        #___________________________________________________

        while True:
            intro()
            make_firewall()
            print()
            print("Does this look correct? ( "+Green+"YES"+Color_Off+" / "+Red+"NO"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
            correct = input(">")
            correct = correct.lower()
            if correct == "yes":
                print("Thank you, your firewall rule has been created.")
                break
            if correct == "quit" :
                print ("Thank you for using Honey Py!")
                sys.exit()
            if correct == "no":
                print("Please redo firewall rule.")

    # SNORT CODE
    if snort_loop == True :
        try :
            if emoji_remover == True :
                print("                           "+Purple+"Starting Snort Mode"+Color_Off+"\n")
        except :
            print("\n")
            print("                         🐷🐷🐷🐷🐷🐷🐷🐷🐷🐷🐷🐷")
            print("                         🐷 "+Purple+"Starting Snort Mode"+Color_Off+"🐷")
            print("                         🐷🐷🐷🐷🐷🐷🐷🐷🐷🐷🐷🐷"+"\n")

        def snort_intro():
            print("An IP address was detected within our Honeypot system. We have identified the")
            print ("machine in question and found that they may have malicious intent.")
            print()
            print("Here you can create a snort rule.")
            print()
            print("")        
        #__________________________________________________
        def make_snort():
            while True:
                print("Would you like to create a new Snort rule?")
                print("")
                choose = input("Please enter ( "+Green+"YES"+Color_Off+" / "+Red+"NO"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
                print("")
                choose = choose.upper()
                if choose == "YES" :
                    print("Please choose an action for your Snort rule.")
                    print("alert")
                    print("log")
                    print("pass")
                    print("activate")
                    print("dynamic")
                    print("drop")
                    print("reject")
                    print("sdrop")
                    action = input(">")
                    action = action.lower()
                    if (action == "alert") or (action =="log") or (action == "pass") or (action == "activate") or (action == "dynamic") or (action == "drop") or (action == "reject") or (action == "sdrop"):
                        print(f"You have chosen {action}.")
                        break
                    else:
                        print("That is not an option. Please choose an option listed above.")
                if choose == "NO" :
                    print("Exiting out of Snort Mode."+"\n")
                    while True:
                        honeypot_project_main_code()
                if choose == "QUIT" :
                    print ("Thank you for using Honey Py!")
                    sys.exit()                
        #____________________________________________________
            while True:
                print("")
                print("Please choose a protocol:")
                print("IP")
                print("TCP")
                print("UDP")
                print("ICMP")
                protocol_snort = input(">")
                protocol_snort = protocol_snort.upper()
                if (protocol_snort == "IP") or (protocol_snort == "TCP") or (protocol_snort == "UDP") or (protocol_snort == "TCP/UDP") or (protocol_snort == "ICMP"):
                    print(f"You have chose {protocol_snort} as your protocol.")
                    break
                else:
                    print("That is not one of the above protocols. Please choose again.")

            print()
        #__________________________________________________
            while True:
                print("Please enter source IP.")
                src_snort = input(">")
                print(f"The source IP is {src_snort}")
                print("")
                print("Please enter the source port or use (any) to include all ports.")
                src_port_snort = input(">")
                print(f"You have chosen {src_port_snort} as your source port.")
                print("")
                while True:
                    print("Please choose which way you would like the flow of traffic to go.")
                    print("A. ->")
                    print("B. <>")
                    flow = input(">")
                    flow = flow.upper()
                    if flow == "A":
                        flow = "->"
                        print("You have chosen A. -> for your flow")
                        print()
                        break
                    elif flow == "B":
                        flow = "<>"
                        print("You have chosen B. <> for your flow")
                        print()
                        break
                    else:
                        print("That is not an option. Please choose A or B to choose flow")
                        print()
                print("Please enter destination IP.")
                dest_snort = input(">")
                print(f"The destination IP is {dest_snort}")
                print("")
                print("Please enter the destination port or use (any) to include all ports.")
                dest_port_snort = input(">")
                print(f"You have chosen {dest_port_snort} as your destination port.")
                print("")
                print("")
                break
            #__________________________________________________
            while True:
                print("Please enter a 'message' for the content of the snort rule.")
                print ("EX: 'Honeypot Capture'. Note, msg: is automatically included.")
                print()
                message = input(">")
                print()
                print(f"You're inputted message is: msg: {message}")
                print()
                break
            #_________________________________________________
            while True:
                print("Please enter an 'SID number' to uniquely identify the snort rule.")
                print ("SIDs will start at 1000000 so inputting '1' will give an SID of 1000001")
                print()
                sid = input(">")
                try :
                    sid = int(sid)
                    sid = 1000000 + sid
                except : 
                    print (On_IRed+" ERROR! Not a valid number. "+Color_Off)
                print()
                print(f"You have chosen {sid} as your sid number")
                print()
                print()
                print("Here is your completed snort rule:")
                print("")
                print(f"{action} {protocol_snort} {src_snort} {src_port_snort} {flow} {dest_snort} {dest_port_snort} (msg: '{message}'; sid: {sid});")
                break
        #___________________________________________________
        while True:
            snort_intro()
            make_snort()
            print()
            print("Does this look correct? ( "+Green+"YES"+Color_Off+" / "+Red+"NO"+Color_Off+" / "+On_IRed+" QUIT "+Color_Off+" )"+"\n")
            correct = input(">")
            correct = correct.upper()
            if correct == "YES":
                print("Thank you, your snort rule has been created.")
                break
            if correct == "QUIT" :
                print ("Thank you for using Honey Py!")
                sys.exit()
            if correct == "NO":
                print("Please redo snort rule.")

    # HELP PAGE CODE
    if help_loop == True :
        try : 
            if emoji_remover == True :
                print ("                                  "+Blue+"HELP PAGE"+Color_Off+"\n")
        except :
            print ("                                📗 "+Blue+"HELP PAGE"+Color_Off+" 📗")
        print ("                                                                               ")
        print ("Created by Isabella Tantillo, Ivan Miskic, and Derek Fong during their time at")
        print ("Fullstack Academy in 2022 for the Cyber Security program.")   
        print ("")
        print ("This program has three parts: A Honeypot, Firewall guide, and Snort generator.")
        print ("🍯")
        print ("The Honeypot works by diverting all traffic from a defined port towards it. It")
        print ("records the attacker's IP address in the process, and traps them inside the")       
        print ("Honeypot. After one second, they will automatically be disconnected from you.")
        print ("To allow traffic to actually occur within a specified port (ex: to keep SSH or") 
        print ("Telnet still active) we recommend that you change the actual SSH or Telnet port")
        print ("to an uncommonly used high port (ex : 2244) and let the attackers use the common") 
        print ("port that are known to attackers. Once they have entered the Honeypot the")
        print ("attackers will see a generic Telnet interface, but will not be able to log in or")
        print ("do damage to you. Once they have entered the Honeypot, the IP address will be logged")
        print ("to a file called Honeypot_Log.txt that will be saved on the user's Desktop along")
        print ("with the date and time of the attack. From there, we recommend running our firewall")
        print ("creator tool that will help you create a firewall rule to block the malicious traffic.")
        print ("")
        print ("Port 23 is recommended because malicious actors will see a fake log in screen if they")
        print ("use this protocol. While ports such as 22 (SSH) can be used, they will not send the")
        print ("the attacker any feedback due to the secure nature of the port. Regardless, the IP")
        print ("address will still be logged once they start the connection to your honeypot.")
        print ("🔥")
        print ("The Firewall guide helps give a guide for firewalls. Once you have viewed the logs") 
        print ("and found the malicious IP addresses, you can use the Firewall generator to help create")
        print ("show you what a firewall rule should look like. We recommend blocking all IP addresses") 
        print ("that are found in the log. If you have users that will be using SSH During the activation")
        print ("of the Honeypot, be sure not to exclude them in the firewall / make sure they use a port")
        print ("you have defined for real traffic to flow through (ex: port 2244 instead of 22).")
        print ("🐷")
        print ("The Snort generator helps you create Snort rules based off of the malicious traffic you")
        print ("have found with Honey Py. After viewing the log files, you will be able to determine which")
        print ("IP addresses you would like to add to your Snort rule.")
        print ("🚨")
        print ("If you get a "+Red+"FATAL ERROR! TRY A DIFFERENT PORT."+Color_Off+" error this is likely")
        print ("because the port is still in use. If you are testing this on a local machine this is")
        print ("because your machine is still trying to connect via Telnet, etc. Be sure to close")
        print ("the CLI to cleanly stop the connection to prevent errors from happening. This error")
        print ("can also happen if you close the python script incorrectly and leave the service running")
        print ("without properly closing it. If this happens, reset your environment or use a different")
        print ("port until the port becomes available again for use. This may take a while, however.")
        print ("")
        print ("Note that if the log file is moved out of the Desktop, a new one will be put in place")
        print ("of it and the counter will be reset. This program will continually write to the log")
        print ("as long as it remains in the target area of the user's Desktop. If the Desktop can not")
        print ("be determined (ex: OS issues), it will be saved to the current directory.")
        print ("If you wish to change the output of the log, type manual_save then type the absolute path.")
        print ("⍰")
        print ("NOTE = if you see a ⍰ instead of an emoji, you are using this program in an environment")
        print ("that does not support emojis (ex: Powershell). During the initial phase, type either")
        print ("disable_emoji or enable_emoji. You will need to do this if you restart the program.")
        print ("If you see unusal inputs such as 033[0;31m, this means your terminal does not support")
        print ("color codes. Currently, there is no support for disabling this function, as we recommend")
        print ("using a modern CLI when using Honey Py for the best compatibility.")
        while True :
            honeypot_project_main_code()
# Main CODE
while True: 
    honeypot_project_main_code()
    # Thank you for using our code! - Isabella Tantillo, Ivan Miskic, and Derek Fong