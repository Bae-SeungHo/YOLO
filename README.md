YOLOv5 전처리 코드 With Python
==============================

'''python
1. 
for label in labels: 
	img = glob('.//'+label+'/*.jpg')
	img = [ PIL.open(img[i]).convert('RGB').resize((416,416)) for i in range(len(img))]
	if not os.path.exists(os.getcwd()+'//'+'export/images'):
   		os.makedirs(os.getcwd()+'//'+'export/images')
	[img[i].save('./export/images/'+label+'_'+str(i)+'.jpg','JPEG') for i in range(len(img))]
'''
