import random
import string

dct = string.ascii_letters + string.digits + "_~`:;!@#$%^&*?<>|=+-()"
pword = ""

def genmenu():
    global pword
    while True:

        print("==============(Menu)==============")
        print("""1)Default-gen
2)Add-exceptions
3)Add-custom-chars
4)Shuffle
5)Save-latest
6)Check-strength
7)Exit""")
       
        try:
            option = int(input())
        except ValueError:
           print("Enter-a-number!")
           continue
    
        if option == 1:
            DefaultGen()
        elif option == 2:
            AddExceptions()
        elif option == 3:
            AddCustom()
        elif option == 4:
            Shuffle()
        elif option == 5:
            SavePasswordToFile()
        elif option == 6:
            CheckPasswordStrength()
        elif option == 7:
            print("Bye")
            return
        else:
            print("No-such-option")

def printp():
    print(f"Generated: {pword}")

def DefaultGen():
    global pword
    l = int(input("Enter-password-length: "))
    pword = ''.join(random.choices(dct, k=l))
    printp()
    Regen()
    return pword

def AddExceptions():
    global pword
    edct = dct

    while True:
        print("==============(What-to-except?)==============")
        print("Current-available-chars:", len(edct))
        print("""1)All-digits
2)All-letters
3)All-special-symbols
4)Custom
5)Done""")
    
        try:
            option = int(input())
        except ValueError:
            print("Please enter a number!")
            continue

        if option == 1:
            edct = ''.join(ch for ch in edct if ch not in string.digits)
            print(f"Remove-digits. Now {len(edct)} chars-available")
        elif option == 2:
            edct = ''.join(ch for ch in edct if ch not in string.ascii_letters)
            print(f"Removed-letters. Now {len(edct)} chars-available")
        elif option == 3:
            specials = "_~`:;!@#$%^&*?<>|=+-()"
            edct = ''.join(ch for ch in edct if ch not in specials)
            print(f"Removed-special-symbols. Now {len(edct)} chars-available")
        elif option == 4:
            expt = input("Excepting(without-separators): ")
            edct = ''.join(ch for ch in edct if ch not in expt)
            print(f"Removed {edct}. Now {len(edct)} chars-available")
        elif option == 5:
            break
        else:
            print("No-such-option")
    
    while not edct:
        print("Error: No characters left!")
        retry = input("Use default set? (Y/N): ").upper()
        if retry == "Y":
            edct = dct
            print("Using default set")
        else:
            print("Returning to main menu")
            return

    l = int(input("Enter-password-length: "))
    pword = ''.join(random.choices(edct, k=l))
    printp()
    Regen()
    return pword

def AddCustom():
    global pword, dct
    added = input("What-to-add(without-separators): ")
    dct += added
    dct = ''.join(dict.fromkeys(dct))
    print(f"Added '{added}'. Total-unque-chars: {len(dct)}")
    l = int(input("Enter-password-length: "))
    pword = ''.join(random.choices(dct, k=l))
    printp()
    Regen()
    return pword

def Shuffle():
    global pword, dct
    print("What-to-shuffle?")
    print("""1)Previous-password
2)Custom-char-set""")
    
    option = int(input())

    if option == 1:
        if pword:
            pword_list = list(pword)
            random.shuffle(pword_list)
            pword = ''.join(pword_list)
            print("Password-shuffled")
            printp()
            Regen()
        else:
            print("No-password-generated-yet")
            Shuffle()
    elif option == 2:
        custom = input("Shuffling(without-separators): ")
        if custom:
            custom_list = list(custom)
            random.shuffle(custom_list)
            pword = ''.join(custom_list)
            print("Custom-set-shuffled")
            printp()
            Regen()
        else:
            print("No-characters-entered")
            Shuffle()
    else:
        print("No-such-option-or-no-password-generated-yet")
        Shuffle()
    return pword

def SavePasswordToFile():
    if pword:
        with open("passwords.txt", "a") as f:
            from datetime import datetime
            f.write(f"{datetime.now()}: {pword}\n")
        print(">>Password-saved-to [passwords.txt]")
    else:
        print("No-password-to-save! Generate-first")

def CheckPasswordStrength():
    if pword:
        score = 0
        if len(pword) >= 8: score += 1
        if len(pword) >= 12: score += 1
        if any(c.islower() for c in pword): score += 1
        if any(c.isupper() for c in pword): score += 1
        if any(c.isdigit() for c in pword): score += 1
        if any(c in "_~`:;!@#$%^&*?<>|=+-()" for c in pword): score += 1
        
        strengths = ["Very Weak", "Weak", "Medium", "Good", "Strong", "Excellent"]
        print(f"\n{'='*30}")
        print(f"Password: {pword}")
        print(f"Length: {len(pword)}")
        print(f"Strength: {strengths[min(score, 5)]} ({score}/6)")
        print(f"{'='*30}")
    else:
        print("No password to check! Generate one first.")
     
def Regen():
    while True:
        choice = input("Regenerate? (Y/N): ")
        choice = choice.upper()
        if choice == "Y":
            genmenu()
            return
        elif choice == "N":
            print("All-done")
            print(f"Final-password: {pword}")
            return
        else:
            print("No-such-option. Y-or-N-only")

print("==============[Password-Generator-V1.8.1]==============")
genmenu()