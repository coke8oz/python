# This will read  the dtr log file
# This will compute the number of hours rendered by an employee per day
from employeeLog import EmployeeLog


def processDtr(file_name):
    dtrs = open(file_name, "r")
    for dtr in dtrs:
        log = dtr.split(" ")
        employeeLog = EmployeeLog(log[0], log[1], log[2], log[3])
        print(employeeLog.employeeId + " -- " + employeeLog.employeeName + " -- " + employeeLog.logIn + " -- " + employeeLog.logOut)

    dtrs.close()


file_name = input("Enter file name: ")
processDtr(file_name)
