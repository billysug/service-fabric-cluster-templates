import pyodbc
server = 'billyssql.database.windows.net'
database = 'billyssql'
username = 'billys'
password = 'LeilaniSierra0522#'   
driver= '{ODBC Driver 17 for SQL Server}'


count=0
while(True):
    cnxn=pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    count+=1
    print(count)
    print(cnxn.getinfo)


