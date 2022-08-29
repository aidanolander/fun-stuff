import csv
import os
import shutil

#ok so this is a mess of a program, but it works
#you have to put this script and the reg csv file inside the resumes folder 
#but the output folder must be on the desktop


#the open file needs to change each time
with open('jan_tech_reginfo.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    yes_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        if row["Are you interested in sharing your information with other employers for future events?"] == 'Yes':
            #print (f'\t{row["Are you interested in sharing your information with other employers for future events?"]}')
            yes_count += 1
            resume_file = (row["Resume"])
            if resume_file :
                if os.path.isfile(resume_file) == True:
                                                #the end of this path will need to change too
                    shutil.copy(resume_file, '/Users/aidanolander/Desktop/opt_in_resumes')
                else:
                    print(resume_file)
            else:
                pass
            #print(resume_file)
            #with open("resume_list.txt", "a") as f1:
            #    f1.write(resume_file)
                
            
        else:
            #print (f'\t{row["Are you interested in sharing your information with other employers for future events?"]}')
            pass
        line_count += 1
    print(f'Processed {line_count} lines. There were {yes_count} affirmatives.')
