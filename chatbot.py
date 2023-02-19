import random  #prefinal code
import re
flag=0
class Chatbot:
    def __init__(self):
        self.message = []
        self.intro = "Hello, I'm a chatbot. How can I help you?"
        
    def chat(self, user_message):
      while True:
          words1=["boiler","storage heater","insulation","heat pump","contact someone on my boiler","contact someone on my storage heater","contact someone on my insulation","contact someone on my heat pump"]
          words2=["faulty thermostat", "damaged thermostat", "display thermostat","HeatSmart", "Netamo smart thermostat"]
          words3=["electricity supply","gas supply","new connection","new supply","supply disruption","electricity disruption","gas disruption"]
          words4=["MyAccount", "personal details", "account details", "edf app"]
          words5=["payment", "payment due","recent payment", "refund", "Energy Bills", "Support Scheme", "Help with the Energy Bills Support Scheme"]
          words6=["Reduce energy costs", "energy costs", "Maximise household income", "household income", "Paying my bills", "Paying bills", "General debt advice", "debt"]
          words7=["Illness","disability","mental health issue"]
          words8=["child", "live with a child", "children", "live alone", "reached state pension age", "live alone or with others and have reached state pension age","disabled",
          "chronically ill state", "pension age or are disabled","pension age or are disabled", "pensionable age or are disabled","chronically ill or under 18 years old", 
          "under 18 years old", "medicine refrigerator problem", "medicine refrigerator", "elderly have problem reading their bills","elder", "elderly have problem with hearing on the phone",
          "elderly have problem with using electronic payments"," child under five years old"]
          if re.compile('|'.join(words1),re.IGNORECASE).search(user_message):
             return(["Is your Storage Heater, Boiler, Insulation or Heat Pump not working properly? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue. If the issue persist you can visit this website https://www.edfenergy.com/heating/boilers/new-boiler."])
             flag=0
             break
          elif re.compile('|'.join(words2),re.IGNORECASE).search(user_message):
             return(["Is your Smart in-home device, in-home display thermostat or HeatSmart/Netamo smart thermostat Boiler not working properly? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue."])
             flag=0
             break
          elif re.compile('|'.join(words3),re.IGNORECASE).search(user_message):
             return(["Do you have an issue with supply disruption or need a new connection? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue."])
             flag=0
             break
          elif re.compile('|'.join(words4),re.IGNORECASE).search(user_message):
             return(["Do you have any issue in MyAccount or need a new connection? You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue."])
             flag=0
             break
          elif re.compile('|'.join(words5),re.IGNORECASE).search(user_message):
             return(["Do you have any issue with Payments, Refunds, Energy Bills or want to know about Support Scheme?  You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue."])
             flag=0
             break
          elif re.compile('|'.join(words6),re.IGNORECASE).search(user_message):
             return(["Do you have any issue with Paying your bills or want to know to reduce energy costs/Maximize household income ?  You can visit our website https://www.edfenergy.com/for-home/help-support/help-centre to get relevant information on how to fix the issue."])
             flag=0
             break
          elif re.compile('|'.join(words7),re.IGNORECASE).search(user_message):
             return(["We are sorry to hear this. We'd like to offer our support and help. Although I am just a robot, we can assist you by encouraging you to seek professional help. You are eligible for our priority services. Please visit https://www.ofgem.gov.uk/information-consumers/energy-advice-households/getting-extra-help-priority-services-register to register. These are the resources: https://www.nhs.uk/nhs-services/mental-health-services/ . You can get in touch with them "])
             break
            #elif re.compile('|'.join(words8),re.IGNORECASE).search(usermessage):
              #print("We are aware of your vulnereble circumstance, we'd like to help via these goverment resources. Please visit https://www.nhs.uk/conditions/social-care-and-support-guide/caring-for-children-and-young-people/.")      
          else:
             (self.message).append(user_message)
        
        
        
        #if __name__ == "__main__":
          #  chat()