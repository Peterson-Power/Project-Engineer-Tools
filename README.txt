Version 2.0

Although this application is written in python, nothing additional is needed to run this application


This script runs off 4 assumptions. Not fulfilling one of these will break the process:
1. The PDF is not open in a reader
2: All bookmarks have a title and are assigned to a page (you will get an error like "int < none" if this is not done) 
3: No child bookmarks will be on a page previous to their parent
4. There is at least 1 more bookmark than the cutoff value (the script will ignore the first x number of bookmarks, so don't have less than that)



The script will use the rest of the bookmarks and use it to generate a TOC on the first page(s) of the new pdf. You might need to reorder the PDF to have the page numbers match the bookmark cutoff.

JST