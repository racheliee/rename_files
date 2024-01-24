# rename images & videos with date taken

## Purpose
This code is used to rename image & video files in a directory.

## Usage
Put the code in the directory where the images & videos are located. Run the code.

## Renaming Behaviour
The code will rename the files in the directory with the following format:
```
YYYYMMDD_HHMMSS.ext
```
Ex:<br />
Given a photo named IMG_0000.jpg taken on 2019/01/01 at 12:00:00, the code will rename it to:
```
20190101_120000.jpg
```

If there are multiple files taken at the same time, the code will append a number to the end of the fsile name.

Ex:<br />
Given a photo named IMG_0000.jpg taken on 2019/01/01 at 12:00:00 and another photo named IMG_0001.jpg taken on 2019/01/01 at 12:00:00, the code will rename them to:
```
20190101_120000.jpg
20190101_120000_1.jpg
```

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
