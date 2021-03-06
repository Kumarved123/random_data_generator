from django.shortcuts import render
from django.template import Context, loader
from pandas import ExcelWriter
from io import BytesIO
import pandas as pd
from utils.utils import *
import xlsxwriter
import os
import sys
import time
import csv
import sqlite3
from django.http import JsonResponse
from django.contrib import messages
from django.core.files import File
from django.http import HttpResponse
from sqlalchemy import create_engine


# Create your views here.
def main(request):
    if request.method != 'POST':
        return render(request, "main.html")
    if request.method == 'POST':
        d = dict(request.POST)
        # getting all the data
        field_name = d['fieldName']
        field_type = d['fieldType']
        percentage = ['percentage']
        nrows = d['fname']
        fileExport = d['fileExport']
        ending = d['l_ending_style']
        chkempty = d['Empty']
        button_value = d["button"]
        valempty = d['valEmpty']
        
        
        rows = []
        chk_index = 0
        chk_arr = []
        formula = (d['formulas'])
        while chk_index < len(chkempty):
            if chkempty[chk_index] == 'Yes':
                chk_arr.append('on')
                chk_index+=2
            else:
                chk_arr.append('off')
                chk_index+=1
        chkempty = chk_arr
        valindex = 0
        chk_index = 0
        val_arr = []
        while valindex < len(valempty)and chk_index < len(chkempty):
            if chkempty[chk_index] == "on":
                val_arr.append(valempty[valindex])
                valindex+=2
            else:
                val_arr.append("0")
                valindex+=1
            chk_index+=1
        
        valempty = val_arr



        # generating the data using functions above
        field_type.pop()
        field_name.pop()
        for i in field_type:
            # GUID Generation
            if i == 'GUID':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(id())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # Row Number Generation
            elif i == 'Row Number':
                tempdata = []
                for j in range(1,int(nrows[0])+1):
                    data = str(j)
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string:
                            print('yes it is there')
                            newValue = enforce_function(string, data, 3)
                        else:
                            newValue = enforce_function(string, data, 2)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # First Name Generation
            elif i == 'First Name':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = fname()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # last Name Generation
            elif i == 'Last Name':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = lname()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # full Name Generation
            elif i == 'Full Name':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = fullname()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # First Name male Generation
            elif i == 'First Name(male)':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = f_fname()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # First Name female Generation
            elif i == 'First Name(female)':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = m_fname()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # Email Generation
            elif i == 'Email':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = Email()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # username Generation
            elif i == 'Username':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = username()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # Comapany Name Generation
            elif i == 'Comapny Name':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = comapny()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # IP address v4 Generation
            elif i == 'Ip address v4':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(ipv4())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


             # IP address v6 Generation
            elif i == 'Ip address v6':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(ipv6())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # job title Generation
            elif i == 'Job Title':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = job()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # Language Generation
            elif i == 'Language':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = lang()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # programming Language Generation
            elif i == 'Programming Language':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = planguage()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


             # Currency
            elif i == 'Currency':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = Currency()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()

            
             # Currency symbol
            elif i == 'Currency Symbol':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(symbol())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


             # Currency symbol
            elif i == 'Gender':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = gender()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()
            
             # random number generation
            elif i == 'Number':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = number()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string:
                            print('yes it is there')
                            newValue = enforce_function(string, data, 3)
                        else:
                            newValue = enforce_function(string, data, 2)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()

                
            # phone number generation
            elif i == 'Phone Number':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(phnumber())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()

            
            # domain name generation
            elif i == 'Domain Name':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(domain())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # date
            elif i == 'Date':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(date_())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # date with time
            elif i == 'Date with time':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(datetime())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()

            
            # time zone generation
            elif i == 'Time Zone':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = timezone()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()
                    
            # boolean generation
            elif i == 'Boolean':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = boolean()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()

            
            # money generation
            elif i == 'Money':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(money())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # mac address generation
            elif i == 'MAC Address':
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append(mac())
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()

            
            # name title generation
            elif i == 'Title':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = nametitle()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


                    
            # gender
            elif i == 'Gender':
                tempdata = []
                for j in range(int(nrows[0])):
                    data = gender()
                    string = formula[field_type.index(i)]
                    if 'this' in string:
                        if "if" in string and "else" in string:
                            newValue = enforce_function(string, data, 3)
                        else:
                            datas = data
                            newValue = ''
                            for data in datas.split():
                                newValue = newValue + ' ' +  enforce_function(string, data, 1)
                        tempdata.append(newValue)
                    else:
                        tempdata.append(data)
                if chkempty[field_type.index(i)] == 'on':
                    df = pd.DataFrame(tempdata)
                    df = empty(df, valempty[field_type.index(i)])
                    tempdata = df['result'].values.tolist()


            # if no match to input
            else:
                tempdata = []
                for j in range(int(nrows[0])):
                    tempdata.append('Not valid Field Type')
                
            rows.append(tempdata)
        
        df = pd.DataFrame((list(zip(*rows))), columns=field_name, dtype=str)
        r, c = df.shape
        table_content = df.to_html(index=False, justify='center',  classes="table")
        if button_value[0] == 'Preview':
            if c == 0:
                return render(request, "main.html")
            else:
                context = {'table_content': table_content}
                return JsonResponse(context)
        elif button_value[0] == '':
            if c == 0:
                return render(request, "main.html")
            else:
                # csv file exporter
                
                if fileExport[0] == 'CSV':
                    
                    filename = "download/random_data.csv"
                    if ending[0] == 'Unix':
                        print("uix")
                        df.to_csv(filename, index=False,encoding="ascii", line_terminator = "\n")
                    else:
                        df.to_csv(filename, index=False,encoding="ascii", line_terminator = "\r\n")
                    path_to_file = os.path.realpath("download/random_data.csv")
                    f = open(path_to_file, 'rb')
                    myfile = File(f)
                    response = HttpResponse(myfile, content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename=' + 'random_data.csv'
                    return response


                # JSON file exporter
                elif fileExport[0] == 'JSON':
                    filename = "download/random_data.json"
                    df.to_json(filename, orient='records', lines=True)
                    path_to_file = os.path.realpath("download/random_data.json")
                    f = open(path_to_file, 'r')
                    myfile = File(f)
                    response = HttpResponse(myfile, content_type='application/json')
                    response['Content-Disposition'] = 'attachment; filename="result.json"'
                    return response


                # TSV file exporter
                elif fileExport[0] == 'TSV':
                    filename = "download/random_data.tsv"
                    if ending[0] == 'Unix':
                        df.to_csv(filename, sep='\t', index=False, line_terminator="\n") 
                    else:
                        df.to_csv(filename, sep='\t', index=False, line_terminator="\r\n")
                    path_to_file = os.path.realpath(filename)
                    f = open(path_to_file, 'r')
                    myfile = File(f)
                    response = HttpResponse(myfile, content_type='text/tsv')
                    response['Content-Disposition'] = 'attachment; filename=' + 'random_data.tsv'
                    return response 



                # TSV file exporter
                elif fileExport[0] == 'Excel':
                    from io import BytesIO as IO
                    excel_file = IO()
                    xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
                    df.to_excel(xlwriter, 'sheetname')
                    xlwriter.save()
                    xlwriter.close()
                    excel_file.seek(0)
                    response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    response['Content-Disposition'] = 'attachment; filename=download/random_data.xlsx'
                    return response

                                
                # XML file exporter
                elif fileExport[0] == 'XML':
                    filename = "download/random_data.xml"
                    pd.DataFrame.to_xml = to_xml
                    to_xml(df, filename)
                    path_to_file = os.path.realpath(filename)
                    f = open(path_to_file, 'r')
                    myfile = File(f)
                    response = HttpResponse(myfile, content_type="text/xml")
                    response['Content-Disposition'] = 'attachment; filename=' + 'random_data.xml'
                    return response 

                if fileExport[0] == 'SQL':
                    r, c = df.shape
                    open("download/randomdata.txt", "w")
                    with open("download/randomdata.txt", "a") as file_prime:
                        for num in range(r):
                            file_prime.write("insert into MOCK_DATA ("+ ", ".join(df.columns.values.tolist())+ ") values ('"+str("', '".join(str(x) for x in df.iloc[[num]].values.tolist()[0]))+ "');"+ '\n')

                    path_to_file = os.path.realpath("download/randomdata.txt")
                    f = open(path_to_file, 'r')
                    with open("download/random_data.sql", 'w') as file:
                        file.write("".join(f))
                    path_to_file = os.path.realpath("download/random_data.sql")
                    f = open(path_to_file, 'r')
                    myfile = File(f)
                    response = HttpResponse(myfile, content_type="text/sql")
                    response['Content-Disposition'] = 'attachment; filename=' + 'random_data.sql'
                    return response 
                
