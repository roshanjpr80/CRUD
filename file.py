# CRUD Operations in a File


from pathlib import Path
import os



def readFileLandFolder():
    path = Path("")
    items = list(path.rglob('*'))
    print("\n\nList of Files and Folders:\n")
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")



def createFile():
    try:
        readFileLandFolder()
        file_name = input("\nPlease tell your file name :- ")
        p = Path(file_name)

        if not p.exists():
            with open(p, 'w') as f:
                data = input("\nWhat do you want to write in this file and empty file press enter :- ")
                f.write(data)

            print(f"\n\n=====  FILE CREATED SUCCESSFULLY  =====\n\n ")


        else:
            print("\n\n This file already exists. \n\n")


    except Exception as err:
        print(f"\nAn error occured as {err}\n")





def readFile():
    try:
        readFileLandFolder()
        file_name = input("\nWhich file do you want to read :- ")
        p = Path(file_name)

        if p.exists() and p.is_file():
            with open(p, 'r') as f:
                data = f.read()
                print("\nFile Content:\n")
                print(data)

            print("\n\n=====  FILE READ SUCCESSFULLY  =====\n\n")
        

        else:
            print("\nThis file does not exist. Please check the name and try again.\n")

        

    except Exception as err:
        print(f"\nAn error occured as {err}\n")



def updateFile():
    try:
        readFileLandFolder()
        file_name = input("\nWhich file do you want to update :- ")
        p = Path(file_name)

        if p.exists() and p.is_file():

            print("\nPress 1 for changing the name of your file.")
            print("Press 2 for appending the some content in your file.")
            print("Press 3 for overwriting the data of your file.")

            press = int(input("\nPlease tell your response :- "))

            if press == 1:
                name_file_new = input("\nPlease enter the new name of your file :- ")
                p2 = Path(name_file_new)
                p.rename(p2)

                print(f"\n\n=====  FILE NAME UPDATED SUCCESSFULLY  =====\n\n ")
            

            elif press == 2:
                data_append = input("\nPlease enter the content you want to append :- ")
                with open(p, 'a') as f:
                    f.write(" "+data_append)

                print(f"\n\n=====  FILE UPDATED SUCCESSFULLY  =====\n\n ")
            

            elif press == 3:
                data_overwrite = input("\nPlease enter the content you want to overwrite :- ")
                with open(p, 'w') as f:
                    f.write(data_overwrite)

                print(f"\n\n=====  FILE OVERWRITTEN SUCCESSFULLY  =====\n\n ")

            else:
                print("\n\n=====  INVALID RESPONSE  =====\n\n ")
            


        else:
            print("\nThis file does not exist. Please check the name and try again.\n")

    

    except Exception as err:
        print(f"\nAn error occured as {err}\n")



def deleteFile():
    try:
        readFileLandFolder()
        file_name = input("\nWhich file do you want to delete :- ")
        p = Path(file_name)

        if p.exists() and p.is_file():
            confirm = input("\nAre you sure you want to delete this file? (yes/no): ").strip().lower()

            if confirm == "yes":
                os.remove(p)
                print(f"\n\n=====  FILE DELETED SUCCESSFULLY  =====\n\n ")

            else:
                print("\nDelete operation cancelled.\n")
        

        else:
            print("\nThis file does not exist. Please check the name and try again.\n")


    except Exception as err:
        print(f"\nAn error occured as {err}\n")



print("=====  WELCOME TO FILE HANDLING PROGRAM (CRUD Operations in a File)  =====\n\n")

print("Press 1 for creating a file.")
print("Press 2 for reading a file.")
print("Press 3 for updating a file.")
print("Press 4 for deleting a file.")


check = int(input("\nPlease tell your response :- "))

if check == 1:
    createFile()

elif check == 2:
    readFile()

elif check == 3:
    updateFile()

elif check == 4:
    deleteFile()

else:
    print("\n\n=====  INVALID RESPONSE  =====\n\n")