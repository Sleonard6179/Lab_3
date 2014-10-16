# File fixer
#   By Samuel Leonard
#    
#
#   This script will search through a folder and retrieve files.
#   it then serches the files to check for a specific file extension,
#   if it is not there or is incorrect, this program will change the file
#   extension and add specified text to the beggining of the file name.
#   It then exports the corrected files to a new folder.
#
#
import os
# Names the location of desired folder.
in_path = 'E:\\A_Masters_Program\\501\Lab_3\\text_files\\'
# Names new folder to recieve corrected files.
mypath = 'E:\\A_Masters_Program\\501\Lab_3\\text_files_fixed\\'
if not os.path.isdir(mypath):
    os.makedirs(mypath)   

# Walks through the directory and pulls files.
for root, dirs, files in os.walk(in_path):
    for file_lower in files:

        file_lower = file_lower.lower()
        file_split = file_lower.split('.')
    	# Splits the files and replaces them with desired aspects.
        if file_split[1] == 'txt':
            os.rename(in_path + file_lower, mypath + "file_" + file_lower +'.txt')
        else:
            os.rename(in_path + file_lower, mypath + "file_" + file_split[0] + '.txt')