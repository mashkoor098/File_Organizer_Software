from tkinter import *
import os
from tkinter import messagebox

count= 1
def cleaner():
    if logs_text_area.get("1.0",END) != "":
        logs_text_area.delete("1.0",END)
    def move(files, destinationDirectory,path):
        for file in files:
            if not os.path.exists(f"{path}\\{destinationDirectory}\\{file}"):
                os.replace(f"{path}\\{file}", f"{path}\\{destinationDirectory}\\{file}")

            else:
                global source_file
                source_file = file
                destination_directory = f"{path}\\{destinationDirectory}"
                destination_file = os.path.join(destination_directory, os.path.basename(source_file))
                counter = 1
                while True:
                    if not os.path.exists(destination_file):
                        break  # File with same name doesn't exist, proceed with move

                    unique_name = f"{os.path.splitext(os.path.basename(destination_file))[0]}({counter}){os.path.splitext(os.path.basename(destination_file))[1]}"
                    destination_file = os.path.join(destination_directory, unique_name)
                    counter += 1  # Increment the counter for the next iteration

                os.rename(f"{path}\{source_file}", destination_file)
                print("Source path renamed to destination path successfully.")


        logs_text_area.insert(END,f"\nSource path renamed to destination path successfully. "
                                  f"\n destinationDirectory:  {destinationDirectory}")

        global count
        while count:
            messagebox.showinfo('Completed','Operation Completed')
            count -= 1
            print(count)

    def CreateIfNotExist(folderName,path):
        if not os.path.exists(f"{path}/{folderName}"):
            os.mkdir(f"{path}/{folderName}")
            print(f"{path}/{folderName}")

    if pathEntry.get() == "":
        files = os.listdir()
        path = os.getcwd()

    else:
        path =str(f"{pathEntry.get()}")
        files = os.listdir(path)

    CreateIfNotExist("images",path)
    CreateIfNotExist("docs",path)
    CreateIfNotExist("medias",path)
    CreateIfNotExist("programs",path)
    CreateIfNotExist("sofwares",path)
    CreateIfNotExist("Others",path)

    imgExts = [".png", ".jpg", ".jpeg",".gif",".ico"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".doc", ".docx", ".xlsx", ".txt", ".pdf",".pptx",".csv"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".flv", ".mp4", ".mp3",".wav"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    programExts = [".py",".java",".class",".cpp",".c",".php",".html",".css",".js",".sql",".swift",".R",".kt"]
    programs = [file for file in files if os.path.splitext(file)[1].lower() in programExts]

    softwareExts = [".exe"]
    softwares = [file for file in files if os.path.splitext(file)[1].lower() in softwareExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in programExts) and (ext not in softwareExts) and (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)

    move(images, "Images",path)
    move(docs, "Docs",path)
    move(medias, "Medias",path)
    move(softwares, "softwares",path)
    move(programs, "programs",path)
    move(others, "Others",path)

# GUI
main_window = Tk()
main_window.title("FO Software")
main_window.geometry("1140x750")
# main_window.geometry("1550x850")
main_window.iconbitmap("icon.ico")

Software_name = Label(main_window,text = "Files Organizer", font=("times new roman",36,"bold"),fg="white",bg="dodger blue",  bd=12, relief=GROOVE)
Software_name.pack(fill=X,pady=16)

desti_detals = LabelFrame(main_window, text="Enter Destination Path",font=('times new roman',15 , 'bold'),fg="blue4",bg="azure2",bd=12, relief=GROOVE)
desti_detals.pack(fill=X,pady=20)

pathLable = Label(desti_detals, text="Path :",font=('times new roman',15 , 'bold'),bg="azure2")
pathLable.grid(row=0, column=0,padx=30)
pathEntry = Entry(desti_detals,font=('arial',15),bd=1,width=70,highlightcolor="black",relief="solid")
pathEntry.grid(row=0,column=1,padx=28)

ClearButton = Button(desti_detals,text="Sort",font=('arial',16,'bold'),bd=7,bg="red",fg="white",width=8 ,pady=8,command=cleaner)
ClearButton.grid(row=0,column=4,pady=20,padx=9)

logs_fram = LabelFrame(main_window, text="System Logs",font=('times new roman',15 , 'bold'),fg="blue4",bg="azure2",bd=12, relief=GROOVE)
logs_fram.pack(fill=X,pady=20)

logs_text_area = Text(logs_fram,font=('times new roman',12 ),height=17,width=120,relief="solid")
logs_text_area.grid(row=0,column=0,padx=40,pady=20)

main_window.mainloop()
