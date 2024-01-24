import os
import sys
import argparse
import datetime
import exifread
import shutil
import re
import time

# helper functions==============================================================
def get_exif(filename):
    f = open(filename, "rb")
    tags = exifread.process_file(f)
    f.close()
    return tags

def get_date(tags):
    date = str(tags["EXIF DateTimeOriginal"])
    date = date.replace(":", "")
    date = date.replace(" ", "")
    return date[0:8] + "_" + date[8:12]

def get_alternate_date(filename):
    date = str(time.ctime(os.path.getmtime(filename)))
    date = date.replace(":", "")
    date = date.replace(" ", "")

    final_date = date[-4:];

    #convert month to number
    if(date[3:6] == "Jan"):
        final_date += "01"
    elif(date[3:6] == "Feb"):
        final_date += "02"
    elif(date[3:6] == "Mar"):
        final_date += "03"
    elif(date[3:6] == "Apr"):
        final_date += "04"
    elif(date[3:6] == "May"):
        final_date += "05"
    elif(date[3:6] == "Jun"):
        final_date += "06"
    elif(date[3:6] == "Jul"):
        final_date += "07"
    elif(date[3:6] == "Aug"):
        final_date += "08"
    elif(date[3:6] == "Sep"):
        final_date += "09"
    elif(date[3:6] == "Oct"):
        final_date += "10"
    elif(date[3:6] == "Nov"):
        final_date += "11"
    elif(date[3:6] == "Dec"):
        final_date += "12"
    
    #add date_time
    final_date += date[6:8] + "_" + date[8:12]
    return final_date

#change file names based on extention===========================================
def work(filename, extension):
    tags = get_exif(filename)
    date = get_date(tags)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+extension):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+extension):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+extension)
                print(date+"_"+str(i)+extension)
                break
    else:
        os.rename(filename, date+extension)
        print(date+extension)

def work_alternate(filename, extension):
    date = get_alternate_date(filename)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+extension):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+extension):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+extension)
                print(date+"_"+str(i)+extension)
                break
    else:
        os.rename(filename, date+extension)
        print(date+extension)

#===============================================================================
def work_all(directory):
    valid_extensions = [".HEIC", ".heic", ".JPG", ".jpg", ".JPEG", ".jpeg", ".PNG", ".png", ".MOV", ".mov", ".MP4", ".mp4"]

    for filename in os.listdir(directory):
        extension = os.path.splitext(filename)[1]

        # If the file does not have a valid extension, skip it
        if(extension not in valid_extensions):
            continue

        try:
            work(filename, extension)
        except:
            # print("Error: " + filename)
            work_alternate(filename, extension)
            continue

#main===========================================================================
# . indicates all files in current directory
work_all(".")