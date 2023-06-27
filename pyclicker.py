# Py-Clicker
# By: MrMidnight


import pyautogui, keyboard

def leftclick():
    x,y=pyautogui.position()
    pyautogui.click(x,y)

def rightclick():
    x,y=pyautogui.position()
    pyautogui.rightClick(x,y)

def doubleclick():
    x,y=pyautogui.position()
    pyautogui.doubleClick(x,y)

def select():
    print("Please choose an action:\n1=leftclick\n2=rightclick\n3=doubleclick\n4=exit\n")


def __init__():


    print("██████╗ ██╗   ██╗      ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗\n██╔══██╗╚██╗ ██╔╝     ██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗\n██████╔╝ ╚████╔╝█████╗██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝\n██╔═══╝   ╚██╔╝ ╚════╝██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗\n██║        ██║        ╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║\n╚═╝        ╚═╝         ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n")
    print("A small python auto-clicker script with 'Pyautogui'")
    print("By: MrMidnight\n")

    select()
    userselect=input("Input>")


    if userselect=="1" or userselect=="2" or userselect=="3":
        pass

    elif userselect=="4":
        print("Thx 4 using me!")
        exit()
    else:
        print("\nInvalid selection!\n")
        select()
        userselect = input("Input>")


    print("\nPress ^C or move the mouse to the right top corner of the screen to abort!\n")

    while userselect=="1":
        leftclick()

    while userselect=="2":
        rightclick()

    while userselect=="3":
        doubleclick()

__init__()
