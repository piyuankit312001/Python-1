#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import pyttsx3 as tts
tts.speak("\tWelcome, please select the application you would like to use or run from the available options listed below. You can enter Quit or Exit anytime to step out of the program")
print("\tWelcome, please select the application you would like to use or run from the available options listed below. You can enter Quit or Exit anytime to step out of the program")
while(True):
    p= input("Please enter your application of choice that you'd like to like to run.\n1. Google Chrome\n2. Notepad\n3. Microsoft Word\n4. Microsoft powerpoint\n5. Microsoft Excel\n")
    if (('run' in p.casefold()) or ('execute' in p.casefold()) or ('open' in p.casefold())) and (('chrome' in p.casefold()) or ('google' in p.casefold())):
        tts.speak('Alright, opening Google Chrome on your request')
        print('Alright, opening Google Chrome on your request')
        os.system('chrome')
    elif (('run' in p.casefold()) or ('execute' in p.casefold()) or ('open' in p.casefold())) and (('notepad' in p.casefold())):
        tts.speak('Alright, opening Notepad on your request')
        print('Alright, opening Notepad on your request')
        os.system('notepad')
    elif(('run' in p.casefold()) or ('execute' in p.casefold()) or ('open' in p.casefold())) and (('ms' in p.casefold()) or ('word' in p.casefold())):
        tts.speak('Alright, opening Microsoft Word on your request')
        print('Alright, opening Microsoft Word on your request')
        os.system('winword')
    elif(('run' in p.casefold()) or ('execute' in p.casefold()) or ('open' in p.casefold())) and (('powerpoint' in p.casefold()) or ('ms' in p.casefold()) or ('ppt' in p.casefold())):
        tts.speak('Alright, opening Microsoft Powerpoint on your request')
        print('Alright, opening Microsoft Powerpoint on your request')
        os.system('powerpnt')
    elif(('run' in p.casefold()) or ('execute' in p.casefold()) or ('open' in p.casefold())) and (('ms' in p.casefold()) or ('excel' in p.casefold())):
        tts.speak('Alright, opening Microsoft Excel on your request')
        print('Alright, opening Microsoft Excel on your request')
        os.system('excel')
    elif(('quit' in p.casefold()) or ('exit' in p.casefold())):
        tts.speak('Alright, closing the program on your request')
        print('Alright, closing the program on your request')
        break
    else:
        tts.speak('Please, select the programs from the above mentioned options only!')
        print('Please select the programs from the above mentioned options only')


# In[ ]:




