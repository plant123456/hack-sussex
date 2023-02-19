# -*- coding: utf-8 -*-
"""
Overall
"""
from tkinter import *
import pandas as pd
import tkinter.ttk as ttk
import nb_hr as predict_hr
import nb_general as predict_general
from chatbot import Chatbot
from random import *

#import #chatbot created

#create pandas dataframe
data = {'user_id': [], 'problem statement': [], 'problem category': []}
data_to_show = pd.DataFrame(data)

#create chatbot
bot = Chatbot()

#create an instance of Chatbox
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
#list of user messages
message_list = []

sent_message = False
# Create a button to send the message
def send_message():
    global sent_message
    message_text = message_input.get("1.0", END).strip()
    if message_text:
        chat_history.config(state=NORMAL)
        chat_history.insert(END, "You: " + message_text + "\n")
        chat_history.config(state=DISABLED)
        message_list.append(str(message_text))
        print(message_list)
        message_input.delete("1.0", END)
        sent_message = True
        print(sent_message)
    

send_button = Button(message_input, text="Send", width="10", height=3,
                     bd=0, bg="#4b0082", activebackground="#000000", foreground='white', font=("Helvetica", 18),
                     command=send_message)
send_button.place(relx=0.97, rely=0.97, anchor='se')


# create a new window
root = Tk()
root.title("DataFrame Window")

# create a TreeView widget to display the dataframe
tree = ttk.Treeview(root, columns=list(data_to_show.columns), show='headings')
for col in data_to_show.columns:
    tree.heading(col, text=col)
for i, row in data_to_show.iterrows():
    tree.insert('', 'end', values=list(row))

# add a scrollbar to the TreeView widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')
tree.pack(side='left', fill='both', expand=True)

#inserts initial message
chat_history.insert(END, f"Chat Bot: {bot.intro} \n")
responses = ['Is your Storage Heater, Boiler, Insulation or Heat Pump not working properly? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue. If the issue persist you can visit this website https://www.edfenergy.com/heating/boilers/new-boiler.',
             "Do you have an issue with supply disruption or need a new connection? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue.",
             "Do you have any issue in MyAccount or need a new connection? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue.",
             "Do you have any issue with Payments, Refunds, Energy Bills or want to know about Support Scheme?  You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue.",
             "Do you have any issue with Paying your bills or want to know to reduce energy costs/Maximize household income ?  You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue."]
#main loop
if (sent_message == True):
    print(sent_message)
    response_1 = bot.chat(message_list[0])

    if len(response_1) > 0:
        chat_history.insert(END, response_1)
    else:
        general_category = predict_general.naive_bayes(message_list)
        if general_category == 'boiler heater':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[0]}')
        elif general_category == 'thermostat':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[0]}')
        elif general_category == 'supply':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[1]}')
        elif general_category == 'meter':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[1]}')
        elif general_category == 'account':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[2]}')
        elif general_category == 'payment':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[3]}')
        elif general_category == 'struggling to pay':
            chat_history.insert(END, f'Based on the topic of your problem here is the following advice {responses[4]}')
        elif general_category == 'high risk':
            hr_category = predict_hr.naive_bayes_hr(message_list)
            if hr_category == 'family': 
                data_to_show['user id'].append(randint())
                data_to_show['problem statement'] = message_list[0]
                data_to_show['problem category'] = hr_category
                chat_history.insert(END, 'Your problem has identified you as a Priority Risk customer')
            elif hr_category == 'special_condition':
                data_to_show['user id'].append(randint())
                data_to_show['problem statement'] = message_list[0]
                data_to_show['problem category'] = hr_category
                chat_history.insert(END, 'Your problem has identified you as a Priority Risk customer')
            elif hr_category == 'medicine':
                data_to_show['user id'].append(randint())
                data_to_show['problem statement'] = message_list[0]
                data_to_show['problem category'] = hr_category
                chat_history.insert(END, 'Your problem has identified you as a Priority Risk customer')

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
#End of chatbox creation

#words


root.mainloop()