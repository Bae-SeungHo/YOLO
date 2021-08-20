YOLOv5 Easy Tutorial With Python
==============================

들어가기에 앞서
----------
YOLO 는 Object Detection 분야에서 가장 유명히 알려진 모델입니다. 

2015 년 Yolov1 를 처음 시작으로 현재 Yolov4 (Darknet) ,Yolov5 (Pycharm) 등의 모델이 만들어 졌습니다.

하지만 라이브러리를 로드하고 쉽게 학습하던 Tensorflow 와는 달리  YOLO를 통해 학습을 하려 하면 처음엔 낯선 코드가 어렵게 느껴집니다.

그래서 이번에 **아주** ***간단하게*** YOLOv5를 통해 학습하는 방법을 하나하나 짚으며 넘어가 보겠습니다.


### 1. 주제 선정
----------------------
물체 검출을 하기 위해선 우선 무엇을 검출할 것인지 그 주제를 생각해야겠죠.

저는 안전모 (HardHat) 와 안전재킷(LifeJacket)을 탐지하고 착용 유무를 학습시켜서 피서객이 안전모, 구명조끼를 착용하도록 하는 모델을 구현해보도록 하겠습니다.




### 2. 데이터셋 수집

검출할 물체를 선정했으면, 그에 맞는 데이터셋을 수집해야 합니다.

Kaggle 또는 구글 이미지에서 안전모 착용 , 구명조끼 착용 데이터셋과 안전모 , 구명조끼 모두 착용하지 않은 데이터셋을 수집하였습니다.

각각 200장 정도 수집하면 괜찮은 성능이 나오는 것 같습니다.


<img src = "https://user-images.githubusercontent.com/77887166/130191193-37e9e9e3-9ec5-4bd3-85bc-47bc4cfefca9.jpg" width="300"> 안전모 O

<img src = "https://user-images.githubusercontent.com/77887166/130190314-ec34fcda-0f26-4b82-966a-9fcbd4653d5c.jpg" width="300"> 구명조끼 O

<img src = "https://user-images.githubusercontent.com/77887166/130191919-dbf32669-c0e0-4db1-8604-38016e592cf5.png" width="300"> 수집한 데이터셋



### 3. 

```python
1. 
for label in labels: 
	img = glob('.//'+label+'/*.jpg')
	img = [ PIL.open(img[i]).convert('RGB').resize((416,416)) for i in range(len(img))]
	if not os.path.exists(os.getcwd()+'//'+'export/images'):
   		os.makedirs(os.getcwd()+'//'+'export/images')
	[img[i].save('./export/images/'+label+'_'+str(i)+'.jpg','JPEG') for i in range(len(img))]
```
