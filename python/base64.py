import base64
import os

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def base64_encode(filedata):
    data = filedata
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    addToClipBoard(encodedStr)
    print()
    print("Encoded String:")
    print(encodedStr)
    print()

def base64_decode(filedata):
    data = filedata
    decodedBytes = base64.b64decode(data.encode("utf-8"))
    decodedStr = str(decodedBytes, "utf-8")
    addToClipBoard(decodedStr)
    print()
    print("Decoded String:")
    print(decodedStr)

def base64_encode_save(filedata):
    data = filedata
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    addToClipBoard(encodedStr)
    print()
    print("Encoded String:")
    print(encodedStr)
    print()
    desktoppath = os.environ['USERPROFILE']
    desktoppath = desktoppath + "\Desktop"
    desktoppath = desktoppath + "\encoded.txt"
    f = open(desktoppath, "w+")
    f.close()
    save = open(desktoppath, "r+")
    save.write(encodedStr)


def base64_decode_save(filedata):
    data = filedata
    decodedBytes = base64.b64decode(data.encode("utf-8"))
    decodedStr = str(decodedBytes, "utf-8")
    addToClipBoard(decodedStr)
    print()
    print("Decoded String:")
    print(decodedStr)
    desktoppath = os.environ['USERPROFILE']
    desktoppath = desktoppath + "\Desktop"
    desktoppath = desktoppath + "\decoded.txt"
    f = open(desktoppath, "w+")
    f.close()
    save = open(desktoppath, "r+")
    save.write(decodedStr)

def askforpath_encode():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_encode(filedata)

def askforpath_decode():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_decode(filedata)

def askforpath_encode_save():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_encode_save(filedata)

def askforpath_decode_save():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_decode_save(filedata)

def menue_encode():
    save = input("Do you want to save it to the Desktop? [y|n] ")
    if save == "y":
        askforpath_encode_save()
        print("Copied to clipboard!")
        print("Saved to Desktop!")
        print()
        print("Press Enter to exit!")
        input()
    elif save == "n":
        askforpath_encode()
        print("Copied to clipboard!")
    else:
        clear()
        print("That is not a option!")
        print()
        menue()

def menue_decode():
    save = input("Do you want to save it to the Desktop? [y|n] ")
    if save == "y":
        askforpath_decode_save()
        print("Copied to clipboard!")
        print("Saved to Desktop!")
        print()
        print("Press Enter to exit!")
        input()
    elif save == "n":
        askforpath_decode()
        print("Copied to clipboard!")
    else:
        clear()
        print("That is not a option!")
        print()
        menue()

def menue():
    clear()
    print("Base64 Encoder/ Decoder - Phoenixthrush v.1.0")
    print("Made by my asian cat")
    print()

    choice = input("Do you want to encode or decode the file? [e|d] ")
    if choice == "e":
        menue_encode()
    elif choice == "d":
        menue_decode()
    else:
        clear()
        print("That is not a option!")
        print()
        menue()

if __name__ == "__main__":
    menue()
