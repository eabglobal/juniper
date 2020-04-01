import pyodbc
driver = '{ODBC Driver 17 for SQL Server}'
sqlServer = 'your-sqlserver'
sqlDatabase = 'your-sqldatabase'
sqlPort = 1433
sqlUsername = 'your-sqlusername'
sqlPassword = 'your-sqlpassword'


def lambda_handler(event, context):
    print(pyodbc.drivers())
    print('Attempting Connection...')
    conn = pyodbc.connect("DRIVER=driver;SERVER=sqlServer;PORT=sqlPort;DATABASE=sqlDatabase;UID=sqlUsername;PWD=sqlPassword")
    print('Connected!!!')
