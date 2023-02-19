# -*- coding: utf-8 -*-
import pandas as pd

def dataframe():
    df1 = pd.DataFrame({'Questions': [
            'I need to contact someone about my boiler',
            'I need to contact someone about my storage heater',
            'I need to contact someone about my insulation',
            'I need to contact someone about my heat pump',
            'Faulty or damaged in-home display thermostat',
            'I have a problem with my HeatSmart or Netamo smart thermostat',
            'Electricity supply',
            'Gas supply',
            'Neither, I need a new supply',
            'My top-up card',
            'Topping up',
            'Emergency credit',
            'Disconnection (no energy supply)',
            'Faulty or damaged meter',
            'Faulty or damaged in-home display',
            'Meter readings',
            'Help accessing MyAccount',
            'Change my personal or account details'
            'I can\'t view my bill in MyAccount',
            'I\'ve downloaded the EDF app for my Apple device, but it keeps crashing',
            'Help with a payment that\'s due',
            'Help with a recent payment',
            'I want a refund of my account credit',
            'Help with the Energy Bills Support Scheme',
            'Reduce energy costs',
            'Maximise household income',
            'Paying my bills',
            'Managing my energy as I have an illness, disability, or mental health issue',
            'General debt advice',
            'live with a child under five years old',
            'live alone or with others and have reached state pension age',
            'live alone or with others and are disabled or chronically ill',
            'live with others who have reached state pension age or are disabled chronically ill or under 18 years old', 
            'medicine refrigerator problem',
            'elderly have problem reading their bills',
            'elderly have problem with hearing on the phone',
            'elderly have problem with using electronic payments'
            ]
                       })
        

    df2 = pd.DataFrame({'Category':[
                'boiler heater','boiler heater','boiler heater','boiler heater',
                 'thermostat','thermostat',
                 'supply','supply','supply',
                 'meter','meter','meter','meter','meter','meter','meter','meter',
                 'account','account','account','account',
                 'payment','payment','payment','payment',
                 'struggling to pay','struggling to pay','struggling to pay','struggling to pay','struggling to pay',
                'high risk','high risk','high risk','high risk','high risk','high risk','high risk','high risk'
                ]
                       })
    
    df = pd.concat([df2,df1], axis=1)
    
    return df
