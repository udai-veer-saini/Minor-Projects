import os
import msvcrt as msv
import sys

RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
NEON_GREEN  = "\033[38;2;57;255;20m"
SKY_BLUE = "\033[38;2;135;206;235m"



data = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]

def oneCharacter():
    os.system("cls")
    print(NEON_GREEN + "\n" + "*"*10 + " ASCII ART PROJECT " + "*"*10 + RESET)
    print(SKY_BLUE + "\n" + "*"*10 + " One Character Module " + "*"*10 + RESET + "\n")
    text = input(YELLOW + "Enter a Character (Only One Character) -- " + RESET).upper()

    if len(text) != 1:
        print(RED + "\n\nPlease Enter Only One Letter -- \n\n" + RESET)
        oneCharacter()
    else:
        print(YELLOW + f"\n\nYou Entered -- {text}\n\n" + RESET)
        n = (ord(text)-17)*6 if ord(text)>=48 and ord(text) <= 57 else 26*6 if text ==" " else 27*6 if text=="@" else 28*6 if text=="_" else 29*6 if text=="-" else 30*6 if text=="." else ((ord(text)-64)-1)*6
        for i in data:
            for j in range(n, n+6):
                print(SKY_BLUE + i[j] + RESET, end="")
            print()

def alphaNumWords():
    os.system("cls")
    print(NEON_GREEN + "\n" + "*"*10 + " ASCII ART PROJECT " + "*"*10 + RESET)
    print(SKY_BLUE + "\n" + "*"*10 + " Alpha Numeric Words Module " + "*"*10 + RESET)
    
    text = input(YELLOW + "\n" + "Enter String (Only <= 15 Character) -- " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(RED + "\n\nPlease Enter Only <=15 Letter -- \n\n" + RESET)
        alphaNumWords()
    else:
        print(YELLOW + f"\n\nYou Entered -- {text}\n\n" + RESET)
        for i in data:
            for x in text:
                n = (ord(x)-17)*6 if ord(x)>=48 and ord(x)<=57 else 26*6 if x==" " else 27*6 if x=="@" else 28*6 if x=="_" else 29*6 if x=="-" else 30*6 if x=="." else ((ord(x)-64)-1)*6
                for j in range(n, n+6):
                    print(SKY_BLUE + i[j] + RESET, end="")
            print()

def alphaRange():
    os.system("cls")
    print(NEON_GREEN + "\n" + "*"*10 + " ASCII ART PROJECT " + "*"*10 + RESET)
    print(SKY_BLUE + "\n" + "*"*10 + " Alpha Range Module " + "*"*10 + RESET)

    text = input(YELLOW + "\n" + "Enter Range (A-D) -- " + RESET).upper()

    if len(text) != 3:
        print(RED + "\n\nPlease Enter Valid Range -- \n\n" + RESET)
        alphaRange()
    else:
        print(YELLOW + f"\n\nYou Entered -- {text}\n\n" + RESET)
        sr = ord(text[0]) - 64
        er = ord(text[2]) - 64

        if sr > er or abs(er-sr) >= 15:
            print(RED + "\n\nPlease Enter Valid Range in Sequence -- \n\n" + RESET)
            msv.getch()
            alphaRange()
        else:
            for i in data:
                for x in range(sr, er+1):
                    n = (x-1) * 6
                    for j in range(n, n+6):
                        print(SKY_BLUE + i[j] + RESET, end="")
                print()

def onlyAlpha():
    os.system("cls")
    print(NEON_GREEN + "\n" + "*"*10 + " ASCII ART PROJECT " + "*"*10 + RESET)
    print(SKY_BLUE + "\n" + "*"*10 + " Only Alphabets Module " + "*"*10 + RESET)

    text = input(YELLOW + "\n" + "Enter String (Only <= 15 Character) -- " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(RED + "\n\nPlease Enter Only <=15 Letter -- \n\n" + RESET)
        msv.getch()
        onlyAlpha()
    elif not text.isalpha():
        print(RED + "\n\nPlease Enter Only Alphabets -- \n\n" + RESET)
        msv.getch()
        onlyAlpha()
    else:
        print(YELLOW + f"\n\nYou Entered -- {text}\n\n" + RESET)
        for i in data:
            for x in text:
                n = ((ord(x)-64)-1)*6
                for j in range(n, n+6):
                    print(SKY_BLUE + i[j] + RESET, end="")
            print()

def onlyNum():
    os.system("cls")
    print(NEON_GREEN + "\n" + "*"*10 + " ASCII ART PROJECT " + "*"*10 + RESET)
    print(SKY_BLUE + "\n" + "*"*10 + " Only Numbers Module " + "*"*10 + RESET)

    text = input(YELLOW + "\n" + "Enter String (Only <= 15 Character) -- " + RESET).upper()

    if not (1 <= len(text) <= 15):
        print(RED + "\n\nPlease Enter Only <=15 Letter -- \n\n" + RESET)
        onlyNum()
    elif not text.isnumeric():
        print(RED + "\n\nPlease Enter Only Numbers -- \n\n" + RESET)
        msv.getch()
        onlyNum()
    else:
        print(YELLOW + f"\n\nYou Entered -- {text}\n\n" + RESET)
        for i in data:
            for x in text:
                n = (ord(x)-17)*6
                for j in range(n, n+6):
                    print(SKY_BLUE + i[j] + RESET, end="")
            print()

def mainUI():
    os.system("cls")
    print(NEON_GREEN + "\n" + "*"*10 + " ASCII ART PROJECT " + "*"*10 + RESET + "\n")
    print(BLUE + "OPTIONS -- \n")
    print(SKY_BLUE + "1. One Character")
    print(SKY_BLUE + "2. Words (Maximum 15 Letters)")
    print(SKY_BLUE + "3. Range (input in Sequence - Max 15 Letters)")
    print(SKY_BLUE + "4. Only Alphabets")
    print(SKY_BLUE + "5. Only Numbers")
    print(SKY_BLUE + "6. Exit")
    print(YELLOW + "\nEnter Your Choice -- " + RESET, end="")

    ch = msv.getch()

    if ch.decode() == "1":
        oneCharacter()
    elif ch.decode() == "2":
        alphaNumWords()
    elif ch.decode() == "3":
        alphaRange()
    elif ch.decode() == "4":
        onlyAlpha()
    elif ch.decode() == "5":
        onlyNum()
    elif ch.decode() == "6":
        return

    print(NEON_GREEN + "\n\nDo you want to continue Project.. Press X else any key..." + RESET)
    ch = msv.getch()

    if ch.decode().lower() == "x":
        mainUI()

mainUI() 