from tkinter import *

root = Tk()
root.title("Chat Bot")
root.geometry("800x500")
root.resizable(width=FALSE, height=FALSE)

# Create a Text widget to display chat history
chat_history = Text(root, bd=1, bg="white", width="66", height="20", font=("Helvetica", 18), foreground="#000000")
chat_history.place(x=6, y=6, height=385, width=780)

# Create a Text widget to type in new messages
message_input = Text(root, bd=0, bg="white", width="66", height="4", font=("Helvetica", 18), foreground="#000000")
message_input.place(x=6, y=400, height=88, width=780)

# Create a button to send the message
def send_message():
    message_text = message_input.get("1.0", END).strip()
    if message_text:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, "You: " + message_text + "\n")
        chat_history.config(state=DISABLED)
        message_input.delete("1.0", END)

send_button = Button(message_input, text="Send", width="10", height=3,
                     bd=0, bg="#4b0082", activebackground="#000000", foreground='white', font=("Helvetica", 18),
                     command=send_message)
send_button.place(relx=0.97, rely=0.97, anchor='se')

# Create a new window to display data
data_window = Toplevel(root)
data_window.title("Data")
data_window.geometry("400x200")

# Add some sample chat history
chat_history.insert(END, "Chat Bot: Hi, how can I assist you today?\n")
chat_history.insert(END, "User: Can you recommend a good restaurant?\n")
chat_history.insert(END, "Chat Bot: Yes, there's a great Italian restaurant on Main Street.\n")
chat_history.insert(END, "User: Thanks, I'll check it out!\n")

# Disable editing in the chat history widget
chat_history.config(state=DISABLED)

main_menu = Menu(root)
file_menu = Menu(root)
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

scrollbar = Scrollbar(root, command=chat_history.yview, cursor="star")
scrollbar.place(x=788, y=5, height=385)

root.mainloop()
