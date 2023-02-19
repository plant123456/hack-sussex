# -*- coding: utf-8 -*-
"""
Overall
"""
#import Chatbox
import pandas as pd
import naive_bayes_model
import naive_bayes_high_risk
#import #chatbot created

#create pandas dataframe
data = {'user': [], 'problem statement': [], 'problem category': []}
data_to_show = pd.DataFrame(data)

#create an instance of Chatbox

'''in first textbox
(
 Create an instance of chatbot
 get the chatbot to interact with the user 
 - give appropriate response
 if no response:
 call naive bayes model using the chatbox stored response as input
 naive bayes model outputs group 
- give appropriate response based on group
 else if response is high risk:
     call naive_bayes_high risk
     add text to dataframe
     add user name to dataframe
     add classification to dataframe
 )  

in second textbox:
    show pandas dataframe'''
    