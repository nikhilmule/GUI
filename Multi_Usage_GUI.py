import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk  #where pil is pillow used for importing images
from tkinter import filedialog, Text
from tkinter.filedialog import askopenfile
from gtts import gTTS
import os



root = tk.Tk()   #beginning of interface

canvas = tk.Canvas(root, width = 600, height = 300) #for setting the gui interface 
#canvas.pack()
canvas.grid(columnspan=5, rowspan = 5)

#logo edition

logo = Image.open('shield.jpg') #loading image
n_logo = logo.resize((100,100))
n_logo = ImageTk.PhotoImage(n_logo) #converting it into tk image
n_logo_label = tk.Label(image = n_logo)
n_logo_label.image = n_logo
n_logo_label.grid(column = 0, row =0)

# welcome

welcome = tk.Label(root, text = "Welcome and please select the required button", font = "Raleway")
welcome.grid(columnspan = 4, column =1, row =0)


#text_box1 = tk.Entry(root)


#Buttons function
# opening pdf
def open_file():
    #print("is this working?")
    browse_text.set("Loading...")
    file = askopenfile(parent = root, mode = 'rb', title = "Choose a file", filetype = [("Pdf file", "*.pdf")])
    if file:
        #print("file was successful")
        read_pdf = PyPDF2.PdfFileReader(file)
        number_of_pages = read_pdf.getNumPages()
        
        for page_number in range(0,number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()

         # here text box for text apperance
        text_box = tk.Text(root, height = 10, width = 50, padx =15, pady =15)
        text_box.insert(1.0, page_content)
        text_box.grid(column = 2, row =4)

    browse_text.set("Browse")

# for opening the apps
apps = []
def select_file():
    #print("is this working?")
    open_text.set("Loading...")
    file = filedialog.askopenfilename(parent = root, initialdir = "/", title = "Choose a file", filetype = [("executables", "*.exe"), ("all files", "*.*")])

    apps.append(file)
    print(file)
    for app in apps:
        label = tk.Label(text = app, bg = "gray")
        os.startfile(app)
        label.grid (column = 3, row =2)
    open_text.set("Select")

# for manual typing

def man_typ():
    type_text.set("Typing..")

    # entry1 = tk.Entry (root) 
    
    
    #
    # frame = tk.Frame(root, bg = 'Slategray3')
    # frame.place(relwidth = 0.5, relheight = 0.5, relx = 0.4, rely = 0.4)
    frame1 = tk.Label(root, text = "Please enter text below", font = "Raleway" )
    frame1.grid(columnspan = 3, column = 1, row =1)
    frame = tk.Text(root, width = 50, height =10)
    frame.grid(columnspan = 3, column = 1, row =2)
    
    # adding additional button
    
    def save_file():

        file = filedialog.asksaveasfile(initialdir = "C:\\Users\\Nikhi\\Desktop\\Python_prac_files\\Python_git", defaultextension = '.txt', filetypes = [("Text file", ".txt"), ("HTML file", ".html"), ("All files", ".*")])
        if file is None:
            return
        filetext= str(tk.get(1.0, End))
        file.write(filetext)
        file.close()

    save_text = tk.StringVar()
    save_btn = tk.Button(root, textvariable = save_text, command = save_file, fg = "White", bg = 'SteelBlue3', height = 2, width =15) 
    save_text.set("Save")
    save_btn.grid(columnspan = 3, column = 1, row =3)
    #type_text.set("Manual Input")

    def aud_txt():
        
        audio_text.set("Processing")

        language = 'de'

        with open("demo.txt") as file:
            
            myobj = gTTS( file.read(), lang=language, slow = False)
        
        myobj.save('clip.mp3')
        
        os.system("mpg321 clip.mp3")

        from playsound import playsound
        playsound('clip.mp3')

    
        type_text.set("Manual Texting")
        os.remove('clip.mp3')
    
    audio_text = tk.StringVar()
    audio_btn = tk.Button(root, textvariable = audio_text, command = aud_txt, fg = "White", bg = 'SteelBlue3', height = 2, width =15) 
    audio_text.set("Listen")
    audio_btn.grid(column =0 , row =4)


# button adding
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_text, command = lambda:open_file(), fg = "White", bg = 'SteelBlue3', height = 2, width =15) 
browse_text.set("Browse")
browse_btn.grid(column =0 , row =1)

open_text = tk.StringVar()
open_btn = tk.Button(root, textvariable = open_text,command = select_file, fg = "White", bg = 'SteelBlue3', height = 2, width =15) 
open_text.set("Select")
open_btn.grid(column =0 , row =2)

type_text = tk.StringVar()
type_btn = tk.Button(root, textvariable = type_text, command = man_typ, fg = "White", bg = 'SteelBlue3', height = 2, width =15) 
type_text.set("Manual Input")
type_btn.grid(column = 0  , row =3)




# for adding extra space
canvas = tk.Canvas(root, width = 600, height = 250) #for setting the gui interface 
#canvas.pack()
canvas.grid(columnspan=5)


root.mainloop()
