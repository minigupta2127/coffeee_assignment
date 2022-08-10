import datetime
import os
#que 11.. checking if file exists in the same path as the program
file=os.path.exists('readme.txt')
print("File exists:",file)

#que13..to find out number of CPUs using 
print("Cpu count:",os.cpu_count())

#que14..to list all files in a directory
path1=r'C:\Users\Lenovo\Desktop\coffeee_assignment\basic_python'
print("All files in the given path:",os.listdir(path1))

#ques15.. to access environment variables
print(os.environ)

#que16..to get current username
print("Current username:",os.getlogin())

#que27..to get syatem's time
system_time=datetime.datetime.now()
print("Systems time:",system_time)