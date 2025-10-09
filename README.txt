Version 1.9

Although this application is written in python, all that is needed to run this script is to download and run the application

I've provided the python source code in case you want to fork it. But the code is completely independent of the application.


Keep in mind the script runs off 3 assumptions. Not fulfilling all of these will break the process
1: All bookmarks have a title and are assigned to a page 
2: No child bookmarks will be on a page previous to their parent
3: There will be 4 bookmarks before the table of contents(title page, Peterson power page, 2x territory maps)


The script will keep the structure of the rest of the bookmarks and use it to generate a TOC on the first page of the new pdf. You will need to reorder the PDF to put the TOC to put it directly behind the BOM. 

Currently the TOC does not contain clickable links but it hopefully will soon, work permitting.

JST