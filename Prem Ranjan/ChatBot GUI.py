from tkinter import *
root = Tk()
root.title('ChatBot')
root.geometry('390x470')

#creating a menu bar
main_menu = Menu(root)

#creating a sub-menu bar
file_menu = Menu(root)
file_menu.add_command(label='New')
file_menu.add_command(label='Save As')
file_menu.add_command(label='Exit')


main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Exit')
root.config(menu=main_menu)


#Creating the chat window
chatwindow = Text(root, bd=1, bg='black', width=50, height=8, yscrollcommand =True)
chatwindow.place(x=6, y=6, height=385, width=370)

#Create a message window
messageWindow = Text(root, bg='black', width=30, height=4)
messageWindow.place(x=6,y=400, height=60, width=260)

#Send button
Button = Button(root, text='Send',activebackground='light blue', width=10, height=5, font=(12))
Button.place(x=275, y=400, height=60, width=100)

#Scroll Bar
scrollbar = Scrollbar(root, command=chatwindow.yview())
scrollbar.place(x=375, y=5, height=385)
root.mainloop()