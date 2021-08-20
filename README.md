YOLOv5 Easy Tutorial With Python
==============================

들어가기에 앞서
----------
YOLO 는 Object Detection 분야에서 가장 유명히 알려진 모델입니다. 

2015 년 YOlov1 를 처음 시작으로 현재 Yolov4 (Darknet) ,Yolov5 (Pycharm) 등의 모델이 만들어 졌습니다.

하지만 라이브러리를 로드하고 쉽게 학습하던 Tensorflow 와는 달리  YOLO를 통해 학습을 하려 하면 처음엔 낯선 코드가 어렵게 느껴집니다.

그래서 이번에 **아주** ***간단하게*** YOLOv5를 통해 학습하는 방법을 하나하나 짚으며 넘어가 보겠습니다.


### 1. 검출 물체 선택


```python
1. 
for label in labels: 
	img = glob('.//'+label+'/*.jpg')
	img = [ PIL.open(img[i]).convert('RGB').resize((416,416)) for i in range(len(img))]
	if not os.path.exists(os.getcwd()+'//'+'export/images'):
   		os.makedirs(os.getcwd()+'//'+'export/images')
	[img[i].save('./export/images/'+label+'_'+str(i)+'.jpg','JPEG') for i in range(len(img))]
```
