#Source: https://stackoverflow.com/questions/13833200/attributeerror-based-on-re-compile-pattern
##  This should be line 19
html_doc = """
        <title>Flickr: username</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta property="og:title" content="username" />
        <meta property="og:type" content="flickr_photos:profile" />
        <meta property="og:url" content="http://www.flickr.com/people/Something/" />
        <meta property="og:site_name" content="Flickr" />
        <meta property="og:image" content="http://farm79.staticflickr.com/1111/buddyicons/99999999@N99.jpg?1234567890#99999999@N99" />

                <li>
                <a href="/groups/theportraitgroup/">The Portrait Group</a>
                <span class="text-list-item">
        1,939,830 photos,&nbsp;125,874 members    
                </span>
        </li>
                <li>
                <a href="/groups/412762@N20/">Seagulls Gone Wild</a>
                        <span class="text-list-item">
                2,266 photos,&nbsp;464 members
                </span>
                                                        </li> """

from urllib.request import urlopen
from bs4 import BeautifulSoup
import fileinput
import re
                                ##  This should be line 46
## Strips for basic group data
Tab      = re.compile("(\t){1,}")                                                    # strip tabs
ID       = re.compile("^.*/\">")                                    # Group ID, could be ID or Href
Href     = re.compile("(\s)*<a href=\"/groups/") # Strips to beginning of ID
GName    = re.compile("/\">(<b>)*")                                    # Strips from end of Href to GName

## Persons contact info
conName  = re.compile("(\s)*<meta property=\"og\:title\" content=\"")        # Contact Name 
##conName = re.compile("(\s)*<a href=\"/groups/")
conID    = re.compile("(\s)*<meta property=\"og\:image.*\#")                    # Gets conName's @N ID
conRef   = re.compile("(\s)*<meta property=\"og\:url.*com/people/")

Amp   = re.compile("&amp;")
Qt    = re.compile("&quot;")                                                
Gt    = re.compile("&gt;")
Lt    = re.compile("&lt;")


exfile = 1        ## 0 = use internal data, 1 = use external file

InFile = html_doc

if exfile:
        InFile = open('\Python\test\Group\group 50 min.ttxt', 'r', encoding = "utf-8", errors = "backslashreplace")
        closein = 1        ## Only close input file if it was opened
else:
        closein = 0

OutFile = open('C:\Python\test\Group\Output.ttxt', 'w', encoding = "utf-8", errors = "backslashreplace")
cOutFile = open('C:\Python\test\Group\ContactOutput.ttxt', 'w', encoding = "utf-8", errors = "backslashreplace")

i = 1    ## counter for debugging

                                ##  This should be line 80
for line in InFile:
##    print('{}'.format(i), end = ', ') ## this is just a debugging line, to see where the program errors out
##    i += 1
        if Href.search(line):
                ln = line
                ln = re.sub(Href, "", ln)
                gID, Name = ln.split("/\">")
                Name = Name[:-5]    ## this removes the "\n" at EOL as well
                if "@N" in gID:
                        rH = ""
                else:        
                        rH = gID
                        gID = ""

##        sLn = '{3}\t{0}\t{1}\t{2}\n'.format(Name, gID, rH, conName)
                sLn = '{0}\t{1}\t{2}\n'.format(Name, gID, rH, conName)
                        ##  Replace HTML codes
                sLn = re.sub(Gt, ">", sLn)
                sLn = re.sub(Lt, "<", sLn)
                sLn = re.sub(Qt, "\"", sLn)
                sLn = re.sub(Amp, "&", sLn)

                OutFile.write(sLn)
                        ##  This should be line 104
                #################################################    
        elif conName.search(line):
                ln = line
                ln = re.sub(conName, "", ln)
                conName = ln.split("\" />")
        elif conID.search(line) is not None:
                ln = line
                ln = re.sub(conID, "", ln)
                conID = ln.split("\" />")
        elif conRef.search(line) is not None:
                ln = line
                ln = re.sub(conRef, "", ln)
                conRef = ln.split("\" />")
        else:
                pass

        sLn = '{0}\t{1}\t{2}\n'.format(conID, conRef, conName)
        cOutFile.write(sLn)        ## I know, this will make a massive file with duplicated data, but deal w/ it later
                #################################################

if closein:
        InFile.close()
OutFile.close()
cOutFile.close()