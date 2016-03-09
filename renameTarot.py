#rename card files in waiteSmith tarot deck directory 
#heavily inspired by 'Project: Renaming Files...' in Automate the Boring Stuff (pp. 206 - 209) 

import shutil, os, re

os.chdir('/Users/caitlin/Documents/school/itc_110/web/web/waiteSmith')

#TODO: Loop over the files in the working directory.
for folder, subFolder, fileName in os.walk('.'):
	for files in fileName:
		# Create a regex that matches part of filename to be substituted
		nameRegex = re.compile(r'^(\d)(\d)?(.-.)(T|W\w*)?(\W)?(\w*.)?(\w*.)?(\w*)(.jpg)')
		mo = nameRegex.search(files)
		if mo != None:
		#TODO: Get the different parts of the filename.	
			no1 = mo.group(1)
			no2 = mo.group(2)
			name = mo.group(9)
			if no2 != None:
				newFile = nameRegex.sub(no1 + no2 + name, files)
			else:
				newFile = nameRegex.sub(no1 + name, files)
						
			#TODO: Get the full, absolute file paths.
			oldPath = os.path.join(os.path.abspath(folder), files)
			newPath = os.path.join(os.path.abspath(folder), newFile)
			#TODO: Rename the files.
			print('Renaming "%s" to "%s"...' % (files, newFile))
			#print('Renaming "%s" to "%s"...' % (oldPath, newPath))
			shutil.move(oldPath, newPath) #uncomment after testing
