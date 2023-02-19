import pandas as pd

def dataframe():
    df1 = pd.DataFrame({'Questions': 
            ['reach date pension age',
            'I am disabled',
            'I have a long term medical condition',
            'Recovering from an injury',
            'I have been injured', 
            'I was in hospital',
            'I am pregnant',
            'I have children',
            'I have young children',
            'I have children under the age of',
            'I cannot communicate well',
            'I cannot speak english well',
            'I cannot understand english',
            'I need to use a medical equipment that requires a power supply',
            'My medicine must be stored in the fridge',
            'My medical equipment uses electricity',
            'machine',
            'I have a bad sense of smell',
            'I struggle to hear',
            'I cannot see well',
            'I struggle to answer the door',
            'I cannot get help in an emergency',
            'I live alone',
            'I am by myself',
            'I am chronically ill',
            'I live with a vulnerable person',
            'I look after'
            ]
                       })
        

    df2 = pd.DataFrame({'Category':
                        
            ['family', 'special condition', 'special condition', 'special condition', 'special condition', 'special condition', 'family','family'
             'family','family','special condition', 'special condition', 'special condition', 'medicine', 'medicine', 'medicine', 'special condition',
             'special condition', 'special condition', 'special condition', 'special condition', 'family', 'family', 'special condition', 'family', 'family'
             ]
                       })


    df = pd.concat([df2,df1], axis=1)
    
    return df