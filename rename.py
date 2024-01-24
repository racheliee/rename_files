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
    return date[0:8] + "_" + date[8:14]

def get_video_date(filename):
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
#rename heic files
def work_heic(filename):
    tags = get_exif(filename)
    date = get_date(tags)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+".HEIC"):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+".HEIC"):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+".HEIC")
                print(date+"_"+str(i)+".HEIC")
                break
    else:
        os.rename(filename, date+".HEIC")
        print(date+".HEIC")

#rename jpg files
def work_jpg(filename):
    tags = get_exif(filename)
    date = get_date(tags)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+".JPG"):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+".JPG"):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+".JPG")
                print(date+"_"+str(i)+".JPG")
                break
    else:
        os.rename(filename, date+".JPG")
        print(date+".JPG")
        
#rename jpeg files
def work_jpeg(filename):
    tags = get_exif(filename)
    date = get_date(tags)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+".JPEG"):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+".JPEG"):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+".JPEG")
                print(date+"_"+str(i)+".JPEG")
                break
    else:
        os.rename(filename, date+".JPEG")
        print(date+".JPEG")

#rename png files
def work_png(filename):
    tags = get_exif(filename)
    date = get_date(tags)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+".PNG"):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+".PNG"):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+".PNG")
                print(date+"_"+str(i)+".PNG")
                break
    else:
        os.rename(filename, date+".PNG")
        print(date+".PNG")

#rename mov files
def work_mov(filename):
    date = get_video_date(filename)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date + ".MOV"):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+".MOV"):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+".MOV")
                print(date+"_"+str(i)+".MOV")
                break
    else:
        os.rename(filename, date+".MOV")
        print(date+".MOV")

def work_mp4(filename):
    date = get_video_date(filename)

    # rename image file to YYYYMMDD_HHMMSS format.
    # if file already exists, add numbering to the end of the file name
    if os.path.exists(date+".MP4"):
        i = 1
        while True:
            if os.path.exists(date+"_"+str(i)+".MP4"):
                i += 1
            else:
                os.rename(filename, date+"_"+str(i)+".MP4")
                print(date+"_"+str(i)+".MP4")
                break
    else:  
        os.rename(filename, date+".MP4")
        print(date+".MP4")

#===============================================================================
def work_all(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".HEIC") or filename.endswith(".heic"):
            try:
                work_heic(filename)
            except:
                print("Error: " + filename)
                continue
        elif filename.endswith(".JPG") or filename.endswith(".jpg"):
            try:
                work_jpg(filename)
            except:
                print("Error: " + filename)
                continue
        elif filename.endswith(".JPEG") or filename.endswith(".jpeg"):
            try:
                work_jpeg(filename)
            except:
                print("Error: " + filename)
                continue
        elif filename.endswith(".PNG") or filename.endswith(".png"):
            try:
                work_png(filename)
            except:
                print("Error: " + filename)
                continue
        elif filename.endswith(".MOV") or filename.endswith(".mov"):
            try:
                work_mov(filename)
            except:
                print("Error: " + filename)
                continue
        elif filename.endswith(".MP4") or filename.endswith(".mp4"):
            try:
                work_mp4(filename)
            except:
                print("Error: " + filename)
                continue
        else:
            continue

#main===========================================================================
# . indicates all files in current directory
work_all(".")