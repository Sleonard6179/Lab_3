# Word Switch
#	By Samuel Leonard
#
# This script will open a file search the text for a specific word and switch it with a diferent word specified by the user.
#
# However it doesn't seem to run well on my system, it cuts out huge chunks of text while writing to new file. 
# this doesn't happen on other systems. I suspect it may be caused by writing file to an external (inexpensive) micro SD card.
#
# Opens the file to be read
lab_3_text = open('E:\\A_Masters_Program\\501\\Lab_3\\GIS_is_the_best.txt')
science_list = lab_3_text.read()
# Defines rules for replace_all in this case it replaces text according the the rules defined in the dic
# If I understand it this says that for ever case of i replace it with j.
def replace_all(text, dic):
        for i, j in dic.iteritems():
                text = text.replace(i, j)
        return text
# This defines my_text
my_text = science_list
# Here reps = where ever there is "Science" change it to "Systems", also where ever there is "science" change it to "system"
reps = {'Science':'System','science':'system'}
#Defines txt 
txt = replace_all(my_text, reps)
# I had trouble with this bit. but this opens a blank file at this path address and names it
out_file = open('E:\\A_Masters_Program\\501\\Lab_3\\GIS_is_the_best_Problem_3_solved1.txt', 'w+')
# performs a write function defined as txt
out_file.write (txt)
# CLoses the file.
out_file.close()
print out_file 
