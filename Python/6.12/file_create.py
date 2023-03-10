print("******** into file_create.py ********")

'''
Python File - working with files 
Create, Read, Update, Delete 

open() / .close() 

x  - create file  
a  - append to file (add to end of file) 
r  - read file (if file is not exist error - No such file or directory)
w  - write (if not exist will create new file )



wb - write binary file
rb - read binary file 
 
'''


# X = craete - create new file..
# open the file for read >> if exist get ERROR (FileExistsError)
# close - on the end to work with file..

file = open('demo_files/deom_file_create.txt', 'x')
file.close()