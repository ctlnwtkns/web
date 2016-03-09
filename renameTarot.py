#rename card files in waiteSmith tarot deck directory 
#heavily inspired by 'Project: Renaming Files...' in Automate the Boring Stuff (pp. 206 - 209) 

import shutil, os, re

os.chdir('/Users/caitlin/Documents/school/itc_110/abs_hw/ch9/waiteSmith')

#TODO: Loop over the files in the working directory.
for folder, subFolder, fileName in os.walk('.'):
	for files in fileName:
		# Create a regex that matches part of filename to be substituted
		nameRegex = re.compile(r'^(\d)(\d)?(.-.)(T|W\w*)?(\W)?(\w*.)?(\w*.)?(\w*)(.jpg)')
		mo = nameRegex.search(files)
		if mo != None:
		#TODO: Get the different parts of the filename.	
			int1 = mo.group(1) 
			int2 = mo.group(2)
			ext = mo.group(3)
			if int2 != None:
				newFile = nameRegex.sub(int1 + int2 + ext, files)
			else:
				newFile = nameRegex.sub(int1 + ext, files)
			#TODO: Get the full, absolute file paths.
			oldPath = os.path.join(os.path.abspath(folder), files)
			newPath = os.path.join(os.path.abspath(folder), newFile)
			#TODO: Rename the files.
			print('Renaming "%s" to "%s"...' % (files, newFile))
			shutil.move(oldPath, newPath) #uncomment after testing
