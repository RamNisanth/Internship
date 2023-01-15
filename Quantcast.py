#!/usr/bin/env python
# coding: utf-8

# In[2]:


import argparse 
import re
import csv

parser = argparse.ArgumentParser(description= "hola")
parser.add_argument("command", type = str, help='Enter a command')
args = parser.parse_args()
command = args.command.lower()

#$ ./most_active_cookie cookie_log.csv -d 2018-12-09
#command = '$ ./most_active_cookie cookie_log.csv -d 2018-12-09'  ############ We need to get this command from CMD
def analyse_command(command):
    if re.search(' -d ', command) and re.search(r'^\$',command):
        file_name = re.search('\w{0,100}.csv',command).group()
        date = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}$', command).group()
        folder = re.search(r'\w+',command).group()
        return (folder,file_name, date)
    else:
        print("Command not detected!!")
analyse_command(command)
(folder, file_name, date)=analyse_command(command)   



INDEX = dict()
MAX = 0
result=[]
with open('./'+folder+'/'+file_name, 'r') as file:
    csvreader = csv.reader(file)
    flag = False
    for row in csvreader:
        i = row[1]
        if flag:
            if i[:i.index(',')] not in INDEX and i[i.index(',')+1:i.index(',')+11]==date:
                INDEX[i[:i.index(',')]]=1
            elif i[:i.index(',')] in INDEX and i[i.index(',')+1:i.index(',')+11]==date:
                INDEX[i[:i.index(',')]]+=1
        flag = True
    for KEY in INDEX:
        if INDEX[KEY]>MAX:
            MAX = INDEX[KEY]
    for k in INDEX:
        if INDEX[k]==MAX:
            result.append(k)            
print(result)

