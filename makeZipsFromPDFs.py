import os
import zipfile

"""
Run this script inside subdirectory (house/county)
in order to use relative paths... ie, if we run at root level,
the zipped file will be Aitkin.zip -> DDP Test/county/Aitkin/all the pdfs..
This way it will be Aitkin.zip -> Aitkin/all the pdfs...
"""




####Step 3: zip up folders
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            print 'zipping ', file
            ziph.write(os.path.join(path, file))
        

## you could add both/all root directories here, but if we place this script in the working directory, it will zip them to that directory with relative paths
## so change the next variable to the appropriate directory
            
folders_to_zip = [r"D:\\DDP Test\\county"]
for folder in folders_to_zip:
    #print("processing: " + folder)
    for root, dirs, files in os.walk(folder):
##        print "root: ",root
##        print "dirs ", dirs
##        print "files ", files
##        print
        for subdirs in dirs:
            #print root, subdirs
            cleanrootlist = root.split('\\')
            #to join the path we have to use every other index... I could have cleaned this prior to next line
            #cleanroot = os.path.join('D:\\', cleanrootlist[2], cleanrootlist[4], subdirs)
            cleanroot = os.path.join(subdirs)
            print cleanroot
            zipf = zipfile.ZipFile(subdirs + '.zip', 'w', zipfile.ZIP_DEFLATED, allowZip64 = True)
            zipdir(cleanroot, zipf)
            zipf.close()












            
            
