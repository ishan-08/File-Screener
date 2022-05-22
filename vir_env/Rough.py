import os, csv
from symtable import Symbol 
import pandas as pd 
from flask import Flask, render_template, request
from file1 import file1

with open('vir_env/file2.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        x = line.replace("\t", " ")
        print(x)

#st_line = input("Enter start line number:")
#end_line = input("Enter end line number:")
#print(st_line)
#print(end_line)
#for i in range(len(file1)):
#    if i == int(st_line):
#        i=str(i)
#        print(file1[i])
#    elif i > int(st_line) and i < int(end_line):
#        i=str(i)
#        print(file1[i])
#    else:
#        pass
#y = file1['142']
#print(y)

#{% for i in range(len(file1)) %}
    #    {% list = {{Num}}.split('-') %}
    #    {% if i == {{list[0]}} %}
    #    <tr>
    #        <td> {{file1[i]}} </td>
    #    </tr>
    #    {% elif  (i</table{{list[1]}}) and (i > {{list[0]}})  %}
    #    <tr>
    #        <td> {{file1[i]}} </td>
    #    </tr>
    #    {% else %}
    #    <tr>
    #        <td> pass </td>
    #    </tr>
    #    {% endif %}
    #{% endfor %}