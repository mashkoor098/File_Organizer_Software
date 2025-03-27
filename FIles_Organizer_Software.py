from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox

count = 1
def cleaner():
    if logs_text_area.get("1.0", END) != "":
        logs_text_area.delete("1.0", END)
    
    def move(files, destinationDirectory, path):
        total_files = len(files)  # Total number of files to move
        progress['maximum'] = total_files  # Set the max value of the progress bar
        
        for index, file in enumerate(files):
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
                        break  # File with the same name doesn't exist, proceed with move

                    unique_name = f"{os.path.splitext(os.path.basename(destination_file))[0]}({counter}){os.path.splitext(os.path.basename(destination_file))[1]}"
                    destination_file = os.path.join(destination_directory, unique_name)
                    counter += 1  # Increment the counter for the next iteration

                os.rename(f"{path}\\{source_file}", destination_file)

            progress['value'] = index + 1  # Update progress bar with the number of files processed
            main_window.update_idletasks()  # Refresh the GUI
        
        print(f"All files moved successfully!")
        logs_text_area.insert(END, f"\nAll files have been moved successfully to {destinationDirectory}")
        messagebox.showinfo("Completed", "File sorting process completed.")
        ClearButton.config(state=NORMAL)  # Enable the button after the process is complete

    def CreateIfNotExist(folderName, path):
        if not os.path.exists(f"{path}/{folderName}"):
            os.mkdir(f"{path}/{folderName}")
            print(f"{path}/{folderName}")

    # Other code for creating directories, getting files, etc...
    # Don't forget to disable the Sort button during the process
    ClearButton.config(state=DISABLED)
    files = os.listdir(path)
    
    CreateIfNotExist("images", path)
    CreateIfNotExist("docs", path)
    CreateIfNotExist("medias", path)
    CreateIfNotExist("programs", path)
    CreateIfNotExist("sofwares", path)
    CreateIfNotExist("Others", path)
    
    # Filter files based on extensions
    move(images, "Images", path)
    move(docs, "Docs", path)
    move(medias, "Medias", path)
    move(softwares, "softwares", path)
    move(programs, "programs", path)
    move(others, "Others", path)

# GUI Setup
main_window = Tk()
main_window.title("FO Software")
main_window.geometry("1140x750")
main_window.iconbitmap("icon.ico")

Software_name = Label(main_window, text="Files Organizer", font=("times new roman", 36, "bold"), fg="white", bg="dodger blue", bd=12, relief=GROOVE)
Software_name.pack(fill=X, pady=16)

desti_detals = LabelFrame(main_window, text="Enter Destination Path", font=('times new roman', 15, 'bold'), fg="blue4", bg="azure2", bd=12, relief=GROOVE)
desti_detals.pack(fill=X, pady=20)

pathLable = Label(desti_detals, text="Path :", font=('times new roman', 15, 'bold'), bg="azure2")
pathLable.grid(row=0, column=0, padx=30)
pathEntry = Entry(desti_detals, font=('arial', 15), bd=1, width=70, highlightcolor="black", relief="solid")
pathEntry.grid(row=0, column=1, padx=28)

ClearButton = Button(desti_detals, text="Sort", font=('arial', 16, 'bold'), bd=7, bg="red", fg="white", width=8, pady=8, command=cleaner)
ClearButton.grid(row=0, column=4, pady=20, padx=9)

logs_fram = LabelFrame(main_window, text="System Logs", font=('times new roman', 15, 'bold'), fg="blue4", bg="azure2", bd=12, relief=GROOVE)
logs_fram.pack(fill=X, pady=20)

logs_text_area = Text(logs_fram, font=('times new roman', 12), height=17, width=120, relief="solid")
logs_text_area.grid(row=0, column=0, padx=40, pady=20)

progress = ttk.Progressbar(main_window, length=300, mode='determinate')
progress.pack(pady=10)

main_window.mainloop()
