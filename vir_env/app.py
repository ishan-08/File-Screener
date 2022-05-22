import os, csv
from symtable import Symbol 
import pandas as pd 
from flask import Flask, render_template, request
from file1 import file1
from file2 import file2
from file3 import file3
from file4 import file4

app = Flask(__name__)
app.debug = True
 
@app.route("/")
def index():
    
    Num = request.args.get('Number', None) 

    lists = []

    if Num:
        if int(Num.split("-")[0]) == 1:
            for i in range(len(file1)):
                if i == int(Num.split("-")[1]):
                    i=str(i)
                    lists.append(file1[i])
                elif i > int(Num.split("-")[1]) and i < int(Num.split("-")[2]):
                    i=str(i)
                    lists.append(file1[i])
                else:
                    pass
        elif int(Num.split("-")[0]) == 2:
            for i in range(len(file2)):
                if i == int(Num.split("-")[1]):
                    i=str(i)
                    lists.append(file2[i])
                elif i > int(Num.split("-")[1]) and i < int(Num.split("-")[2]):
                    i=str(i)
                    lists.append(file2[i])
                else:
                    pass
        elif int(Num.split("-")[0]) == 3:
            for i in range(len(file3)):
                if i == int(Num.split("-")[1]):
                    i=str(i)
                    lists.append(file3[i])
                elif i > int(Num.split("-")[1]) and i < int(Num.split("-")[2]):
                    i=str(i)
                    lists.append(file3[i])
                else:
                    pass
        elif int(Num.split("-")[0]) == 4:
            for i in range(len(file4)):
                if i == int(Num.split("-")[1]):
                    i=str(i)
                    lists.append(file4[i])
                elif i > int(Num.split("-")[1]) and i < int(Num.split("-")[2]):
                    i=str(i)
                    lists.append(file4[i])
                else:
                    pass        
        else:
            pass            
            
    return render_template('index.html', lists=lists, Num=Num)

    
