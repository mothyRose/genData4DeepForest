import os

#This program is used to rename all the files from 1 to the last


#classes = ('car','people','pet','sign','traffic')
root_path='.\\'
classes = ('bus','dinasour','elephant','flower','horse')
def rename_all(path):
	for i,file in enumerate(os.listdir(path)):
		if os.path.isfile(os.path.join(path,file))==True:
			if True:
				newname=str(i)+'.JPEG'
				os.rename(os.path.join(path,file),os.path.join(path,newname))
				print (file,'ok')
	#        print file.split('.')[-1]
	
for i in range(len(classes)):
	rename_all(root_path+classes[i]+'\\')
