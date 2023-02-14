
# import required module
import os
# assign directory
directory = r'C:\sec_gov\Archives\edgar\data\1326801'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)