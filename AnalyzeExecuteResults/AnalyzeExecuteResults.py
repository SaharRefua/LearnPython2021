import xlsxwriter
import datetime
import os
import xlrd 
data=[]
testPlansOnly=[]
allDeletedRows=[]
RunID_Only=[]

#Get the Current time 
now = datetime.datetime.now()
current_time = now.strftime("%d-%b-%Y_%H_%M_%S")
#_%H_%M_%S

#Get the Excel file from the user 
print('Please Enter excel file name: ')
file="Example _Backup.xlsx" # input()
#file="Example _Backup copy.xlsx"
print('In process ...................')
userFilesPath=os.getcwd()   # Get the corrent dirctory
#arr= os.listdir(userFilesPath)
os.chdir(userFilesPath)         # Navigate to dirctory X and work there !!!
Hader = "Test Plan ID , TestCaseId,TestCaseName ,TestRunId ,Tester,  ResultOutcome , ResultDate,ResultDate_Original, Duplicate, Build, Automated"

def readDataFromOriginalExcelFile(file):    
    # To open Workbook 
    wb = xlrd.open_workbook(file) 
    sheet = wb.sheet_by_index(0) 

    sheet.cell_value(0, 0)
    for i in range(sheet.nrows): 
        def convertDateTime(dateTimeToConvert):
            try:
                year, month, day, hour, minute, second = xlrd.xldate_as_tuple(dateTimeToConvert, wb.datemode)
                #py_date = datetime.datetime(year, month, day, hour, minute, 0)
                py_date = datetime.date(year, month, day)
                t = py_date.strftime("%d-%b-%Y")
                x = str(t)
                return x
            except:
                # No dateTime Data  
                return dateTimeToConvert

        def getBuildNumber(buildNumber):
            try :
                t=buildNumber.split("_")
                x=t[3]
                x=x[1:-1]
                return x 
            except:
                # return 'No Build'
                return buildNumber
        if(0<i):
            #row = [Test Plan ID,	Test Suite Link , 	Test Suite Name , 	Test Case Id	, Duplicate , Test Case Name	Test Run Id	Result Outcome	Tester	Result Date	Comment	Build	Configuration	Automated)
            TestPlanID = str(sheet.cell_value(i, 0))
            TestSuiteName=str(sheet.cell_value(i, 2))
            #print(sheet.cell_value(i, 3))
            TestCaseId=int(sheet.cell_value(i, 3))
            Duplicate=str(sheet.cell_value(i, 4))
            TestCaseName=str(sheet.cell_value(i, 5))
            #Get TestRunId
            if  (sheet.cell_value(i, 6)==''):
                TestRunId=int(0)
            else:
                TestRunId=int(sheet.cell_value(i, 6))
            ResultOutcome=str(sheet.cell_value(i, 7))
            Tester=str(sheet.cell_value(i, 8))
             # Get ResultDate_temp 
            try:
                ResultDate_temp = float ((sheet.cell(i, 9).value ))
            except:
                ResultDate_temp=0
            # Call function to convert the date
            ResultDate=convertDateTime(ResultDate_temp) 
            Build_temp=str(sheet.cell_value(i, 11))
            Build=getBuildNumber(Build_temp)
            Automated_temp=str(sheet.cell_value(i, 13))
            if Automated_temp=='0':
                Automated='False'
            else:
                Automated='True'
            data.append([TestPlanID, TestCaseId,TestCaseName ,TestRunId ,Tester,  ResultOutcome , ResultDate,ResultDate_temp, Duplicate, Build, Automated])
            testPlansOnly.append(TestPlanID)
            RunID_Only.append(TestCaseId)

 
def removeDuplicate():
    Duplicated="Duplicated"
    for row in data:
        if row[8]== Duplicated:
            for i in data:
                # if TestCaseId is equal 
                if i[1]==row[1]:
                        i_runId=int(i[3])
                        row_runId=int(row[3])
                        
                        try:
                            if i_runId==0:
                                data.remove(i)
                                allDeletedRows.append(i)
                            elif row_runId==0:
                                data.remove(row)
                                allDeletedRows.append(row)
                            elif i_runId>row_runId:
                                data.remove(row)
                                allDeletedRows.append(row)
                            elif i_runId<row_runId:
                                data.remove(i)
                                allDeletedRows.append(i)
                            # if run id and Test case id are equal remove th duplicate test (Automation test have the same run id but not the same test id )    
                            elif i_runId==row_runId and row[1]==i[1]:
                                if row[8]!=i[8]: #and i[10] == "False" and row [10 ]=="False": 
                                    data.remove(row)
                                    allDeletedRows.append(row)

                        except:
                            print("Error " , i , "\n" ,row)

def CreateNewExcelFile():
    #Navigate /Create Folder Reports
    path_reports =userFilesPath+ "\\Reports"
    try:
        os.mkdir(path_reports)
    except OSError:
        #print ("Creation of the directory %s failed" % path_reports)
        print ("Creation of the directory %s failed" % path_reports)
    else:
        print ("Successfully created the directory %s " % path_reports)
    os.chdir(path_reports) # Navigate to Reports dirctory and work there !!!
    reportName='Report' + '_' + str(current_time)+'.xlsx'
    Workbook = xlsxwriter.Workbook(reportName)
    plans=set(testPlansOnly)
    for plan in plans:
        temp=str(plan)
        temp=temp[-26:]
        Workbook_data=Workbook.add_worksheet(temp)
        title=Hader.split(',')
        row=0
        column=0
        for item in title:
            Workbook_data.write(row, column , item )
            column= column+1
        row=1 
        column=0
        for row_data in data:
            column=0
            if row_data[0]==plan:
                for  item in row_data :
                    Workbook_data.write(row, column , item )
                    # incase  ResultOutcome is not applicable Or failed i will colcor the call in Red and enter ResultOutcome Value  
                    if (column==5 and item== 'NotApplicable') or (column==5 and item== 'Failed'):           #'NotApplicable'
                        filure = Workbook.add_format(
                           { "bg_color": "#B22222",
                             "bold" : True,
                            }
                         )
                        Workbook_data.write(row , column  ,item , filure)
                    # incase no ResultOutcome was found for this test i will colcor the call in Yellow and enter No ResultOutcome string 
                    elif column==5 and item== '':
                        NoData = Workbook.add_format(
                           { "bg_color": "#FFFF33",
                             "bold" : True,
                            }
                         )
                        Workbook_data.write(row , column  ,'No ResultOutcome' , NoData)
                    column= column+1
                row=row+1
        x=len(data)
        x=x+1
        t=str(x)
        range='A1:K{}'.format(t)
        Workbook_data.autofilter(range)
    Workbook.close()

def CheckIfthereAreStilDuplicatedIntheList():
    maxNumberOFDupliacates=0
    for TC_ID in RunID_Only:
        test_id=TC_ID
        if RunID_Only.count(TC_ID) > 1:
            if maxNumberOFDupliacates<RunID_Only.count(TC_ID):
                maxNumberOFDupliacates=RunID_Only.count(TC_ID)
    print('Max dupliated tests in the excel are : ' , maxNumberOFDupliacates)
            
    i=0
    while maxNumberOFDupliacates > i:
        removeDuplicate()
        i=i+1

readDataFromOriginalExcelFile(file)
CheckIfthereAreStilDuplicatedIntheList()
CreateNewExcelFile()
# define the name of the directory to be createdExample _Backup copy.xlsx
path =userFilesPath+ "\\Logs"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
os.chdir(path) # Navigate to Logs dirctory and work there !!!

LogsfileName='DeletedTests' + '_' + str(current_time)+'.txt'
with open(LogsfileName, 'a') as dt:
    dt.write(Hader)
    for deleteRow in allDeletedRows:
        i = str(deleteRow)
        dt.write("\n")
        dt.write(i)
print("----------------------------------------------------------------------")
print('My work is complete  =)')
print('All the deleted test are saved in DeletedTests.txt')
print('Please see the last report file from Reports folder')
print("----------------------------------------------------------------------")

