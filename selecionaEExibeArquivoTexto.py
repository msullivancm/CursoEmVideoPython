from tkinter import *
from tkinter.filedialog import askopenfilename
root=Tk()

filename=askopenfilename()
lblArquivo=Label(root, text=filename)
lblArquivo.config(text=filename, width="50")
lblArquivo.pack()

my_text=Text(root, height=40, width=60)
file_object=open(filename)
file_content=file_object.read()
file_object.close()
my_text.insert(END, file_content)
my_text.pack(side=LEFT, fill=X, padx=5)

root.mainloop()
