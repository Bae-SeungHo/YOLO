## YOLOv5 를 쉽게 사용하는 Guide

for label in labels: 
	img = glob('.//'+label+'/*.jpg')
	img = [ PIL.open(img[i]).convert('RGB').resize((416,416)) for i in range(len(img))]
	if not os.path.exists(os.getcwd()+'//'+'export/images'):
   		os.makedirs(os.getcwd()+'//'+'export/images')
	[img[i].save('./export/images/'+label+'_'+str(i)+'.jpg','JPEG') for i in range(len(img))]

