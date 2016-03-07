import os

for foldername, subfolders, filenames in os.walk('waiteSmith'):
	print('The current folder is ' + foldername)
	
for subfolder in subfolders:
	print('SUBFOLDER of ' + foldername + ':' + subfolder)
	
for filename in filenames:
	print('file inside ' + foldername + ':' + filename)

print('')