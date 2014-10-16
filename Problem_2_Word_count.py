# Word counter
# 	This program opens a text document and counts the number of instances
#	that "science" and "systems" occurs. It also returns a count of all words.
#
#
lab_3_text = open('E:\\A_Masters_Program\\501\\Lab_3\\GIS_is_the_best.txt')
file_list = lab_3_text.read()

system_count, science_count, total_words = 0, 0, 0

for word in file_list.split(' '):
    #This is where the words are checked for and counted
    if word.lower() == 'systems':
            system_count = system_count + 1
    elif word.lower() == 'science':
            science_count = science_count + 1
    else:
            total_words = total_words + 1

total_words = total_words + science_count + system_count



print "Number of instances of 'system' = " + str(system_count)

print "Number of instences of 'science' = " + str(science_count)

print "Total words = " + str(total_words)

raw_input('press return to finish: ')