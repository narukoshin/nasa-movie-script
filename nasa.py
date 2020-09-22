#!/usr/bin/env python3
from time import sleep
from sys import exit
import os

os.system("clear")

print(r'''
  o          o           o           o__ __o           o         
 <|\        <|>         <|>         /v     v\         <|>        
 / \\o      / \         / \        />       <\        / \        
 \o/ v\     \o/       o/   \o     _\o____           o/   \o      
  |   <\     |       <|__ __|>         \_\__o__    <|__ __|>     
 / \    \o  / \      /       \               \     /       \     
 \o/     v\ \o/    o/         \o   \         /   o/         \o   
  |       <\ |    /v           v\   o       o   /v           v\  
 / \        < \  />             <\  <\__ __/>  />             <\ 
''')


try:
    sure=str(input('Are you sure you want to hack NASA? (yes/no): '))
    if 'yes' in sure:
        pass
    else:
        exit()
except KeyboardInterrupt:
    print('NASA HACK> user exit...')

print('\033[32mUser permission received.. Warming up for hacking NASA, please wait...\033[0m')
sleep(3)
print('\033[95mStarting hacking NASA...')
sleep(.5)
print('\033[31mHacking NASA 0%')
sleep(1)
print('\033[31mHacking NASA 20%')
sleep(2)
print('\033[31mHacking NASA 42%')
print('\033[31mHacking NASA 58%')
sleep(1)
print('\033[31mHacking NASA 95%')
print('\033[31mHacking NASA 100%')
sleep(.5)
print('\033[32mNASA HACKED SUCCESSFULY!\033[0m')
print('Launching remote access control...')
print('To list all commands, please type `help`')
input('NASA> ')