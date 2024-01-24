# rename images & videos with date taken

## Purpose
This code is used to rename image & video files in a directory using the EXIF data of the file. (If no EXIF data exists, the last modified date will be used).

## Usage
Put the code in the directory where the images & videos are located. Run the code.

## Renaming Behaviour
The code will rename the files in the directory with the following format:
```
YYYYMMDD_HHMM.ext
```
Ex:<br />
Given a photo named IMG_0000.jpg taken on 2019/01/01 at 12:00, the code will rename it to:
```
20190101_1200.jpg
```

If there are multiple files taken at the same time, the code will append a number to the end of the file name.

Ex:<br />
Given a photo named IMG_0000.jpg taken on 2019/01/01 at 12:00 and another photo named IMG_0001.jpg taken on 2019/01/01 at 12:00, the code will rename them to:
```
20190101_1200.jpg
20190101_1200_1.jpg
```
If a photo does not have EXIF data, the last modified date of the image/video file will be used. (Since videos most often do not have EXIF data, it will use the last modified date).

## Supported Extensions
The code will rename files with the following extensions:
- heic
- jpg
- jpeg
- png
- mov
- mp4
  
## Dependencies
Install exifread to read exif data from images
``` pip install "exifread<3" ``` (for mac silicon users)
otherwise, install the regular exifread version
