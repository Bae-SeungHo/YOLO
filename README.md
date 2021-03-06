YOLOv5 Easy Tutorial With Python + Preprocessing Python code 
==============================

들어가기에 앞서
----------
YOLO 는 Object Detection 분야에서 가장 유명히 알려진 모델입니다. 

2015 년 Yolov1 를 처음 시작으로 현재 Yolov4 (Darknet) ,Yolov5 (Pycharm) 등의 모델이 만들어 졌습니다.

하지만 라이브러리를 로드하고 쉽게 학습하던 Tensorflow 와는 달리  YOLO를 통해 학습을 하려 하면 처음엔 낯선 코드가 어렵게 느껴집니다.

그래서 이번에 **최대한** ***간단하게*** YOLOv5를 통해 학습하는 방법을 하나하나 짚으며 넘어가 보겠습니다.


### 1. 주제 선정
---
물체 검출을 하기 위해선 우선 무엇을 검출할 것인지 그 주제를 생각해야겠죠.

저는 안전모 (HardHat) 와 안전재킷(LifeJacket)을 탐지하고 착용 유무를 학습시켜서 피서객이 안전모, 구명조끼를 

착용하도록 하는 모델을 구현해보도록 하겠습니다.



#### 1-A. Yolov5 설치
실행을 눌러서 cmd 를 연 후 깃헙에서 YOLOv5를 내려받습니다. *관리자권한으로 실행하면 다른 폴더에 저장되니 유의하세요*

> https://github.com/ultralytics/yolov5

저장 폴더는 기본적으로 C://사용자/"유저이름" 에 "yolov5" 라는 폴더입니다.



### 2. 데이터셋 수집
---
검출할 물체를 선정했으면, 그에 맞는 데이터셋을 수집해야 합니다.

Kaggle , roboflow 또는 구글 이미지에서 안전모 착용 , 구명조끼 착용 데이터셋과 안전모,

구명조끼 모두 착용하지 않은 데이터셋을 수집하였습니다.

각각 200장 정도 수집하면 괜찮은 성능이 나오는 것 같습니다.

이미지를 모아서 안전모, 구명조끼 이미지들 각각 폴더에 저장하고, C://사용자/"유저이름" 위치에 "Dataset" 폴더를 만들어서

그곳으로 모두 이동해줍시다.


<img src = "https://user-images.githubusercontent.com/77887166/130191193-37e9e9e3-9ec5-4bd3-85bc-47bc4cfefca9.jpg" width="300"> 안전모 O

<img src = "https://user-images.githubusercontent.com/77887166/130190314-ec34fcda-0f26-4b82-966a-9fcbd4653d5c.jpg" width="300"> 구명조끼 O

<img src = "https://user-images.githubusercontent.com/77887166/130191919-dbf32669-c0e0-4db1-8604-38016e592cf5.png" width="300"> 수집한 데이터셋



### 3. 이미지 Resizing
---
YOLOv5 학습기에 이미지를 입력할 때는 모든 이미지가 같은 사이즈여야 합니다.

하지만 인터넷에서 다운받은 이미지는 다 사이즈가 제각각일 겁니다.

그래서, "[1]IMG_to_416.py" 파이썬 파일을 통해 이미지를 전부 가로,세로를 416 사이즈로 Resizing 하는 작업이 필요합니다.

코드 내부를 보면 다음과 같습니다.

```python
labels = input().split() # Resizing 할 대상 이미지 폴더입니다.

for label in labels: 
	img = glob('.//'+label+'/*.jpg') # 이미지 파일을 추출합니다.
	img = [ PIL.open(img[i]).convert('RGB').resize((416,416)) for i in range(len(img))] # 이미지 파일을 RGB , 416 사이즈로 변환합니다.
	if not os.path.exists(os.getcwd()+'//'+'export/images'):
   		os.makedirs(os.getcwd()+'//'+'export/images')
	[img[i].save('./export/images/'+label+'_'+str(i)+'.jpg','JPEG') for i in range(len(img))] # export 폴더 속의 images 폴더에 이름을 순서대로 저장합니다.
```


[1]IMG_to_416.py 파일과 이미지를 모아놓은 폴더들을 같은 폴더에 두고 실행시킨 뒤,

실행된 도스창에 폴더 이름들을 모두 적어주세요. (스페이스바로 띄워서!)


![image](https://user-images.githubusercontent.com/77887166/130194023-bd22f31e-27c0-4703-8cc2-8a11c1998b9f.png) 

그러면 Resizing 된 이미지들이 export/images 폴더에 저장됩니다.


![image](https://user-images.githubusercontent.com/77887166/130193782-a176a761-755d-42ca-95dc-607ae35529a5.png)  


### 4. 학습 데이터 / 테스트 데이터 분리
---
export 폴더에 전처리된 이미지들이 저장되었다면 , 학습 데이터와 테스트 데이터로 분리합니다.

"[2]Path_Manual.py" 파일 코드 내부에는 test size 를 조절할 수 있습니다.

```python
input_test_size = 0.2
```

대게 test size 를 전체의 20% 로 두어서 0.2로 설정하였는데, 변경하실 수 있습니다!

그 후, "[2]Path_Manual.py" 를 "[1]IMG_to_416.py" 을 두었던 같은 폴더에 두고 실행하면

자동으로 train , test 폴더가 생성되며 폴더 내부의 images 에 사진이 저장됩니다.



### 5. 이미지 라벨링
---
이제는 사용자가 직접 이미지의 어느 부분이 안전모인지, 구명조끼인지 지정해 주어야 합니다.

그렇기 위해서는 LabelImg 라는 툴을 사용합니다.

> https://github.com/tzutalin/labelImg

설치하시면 우선 data 폴더 안의 "predefined_classes.txt" 를 수정하여 Object 카테고리를 설정합니다.

저는 헬멧 착용 유무 , 구명조끼 착용 유무를 확인하므로 네개의 카테고리를 메모장에 추가하였습니다.

![image](https://user-images.githubusercontent.com/77887166/130195167-3f125c5a-c86e-44b4-878a-12cf16dbef34.png)

그 후, labelimg.py 를 실행하고 , 좌측 탭의 "Open dir" 를 선택하여 학습데이터의 폴더를 선택합니다. (train/images 폴더 선택)

그리고 "Change Save Dir" 를 선택하여 이번엔 학습데이터의 라벨링 폴더를 선택합니다. (train/labels 폴더 선택)

왼쪽 탭 밑의 저장 형식을 선택할 수 있는데 , "PascalVOC" 로 선택되어 있다면 "YOLO" 로 바꿔줍니다 __(중요!!)__

![image](https://user-images.githubusercontent.com/77887166/130195687-2152f5d1-1236-46ae-ab2d-c699b4bddc65.png)

하는데 시간이 쫌 걸릴거에요.. 저는 600장 하는데 2시간 정도 들은 것 같습니다!

학습 데이터의 라벨링이 끝났으면 test 폴더의 이미지들도 같은 방법으로 라벨링 해주세요!

조작방법은 w로 영역 선택 , a 와 d 로 사진 이동 입니다. LabelImg 깃헙에서 자세히 설명되어 있으니 참고하시면 됩니다.


### 6. data.yaml 파일 만들기
---
라벨링이 끝났나요? 거의 다 왔습니다!

이제 Dataset 폴더에 data.yaml 파일을 만들어줍니다.

메모장을 여신 후, 아래와 같은 양식으로 적어줍시다.

```
path: 데이터셋 저장 폴더 # dataset root dir
train: train/images  
val: test/images 

# Classes
nc: 물체 카테고리의 갯수  # number of classes
names: [ 카테고리 각각의 이름 ]  # class names
```

저와 같은 경우에는, 네개의 카테고리를 분류하므로 다음과 같이 적어주었습니다.

```
path: ../Dataset/ # dataset root dir
train: train/images  
val: test/images  

# Classes
nc: 4  # number of classes
names: ['lifejacket', 'Hardhat', 'No_Hat', 'No_Jacket']  # class names
```


### 7. 학습하기
---
지금까지 잘 따라오셨다면 이제 학습할 준비가 다 되었습니다!

도스창을 통해 직접 학습시켜봅시다.

cmd 를 연후 다음과 같이 입력해줍시다!

```cmd
cd yolov5
python train.py --img 416 --batch 8 --epochs 30 --data ../Dataset/data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name my_first_training
```
여기에서, --img 는 이미지 크기 , --batch 는 배치 사이즈 , --epochs 는 반복 횟수 , --data 는 data.yaml 의 경로,

--cfg는 학습에 사용될 모델 사이즈 , --weights 는 이미 학습된 가중치 (없으면 --cfg의 모델사이즈와 같은 이름의 .pt),

--name 은 학습 후 가중치가 저장될 폴더입니다.

batch 사이즈는 클수록 그래픽카드 메모리를 많이 소모하기 때문에 오류가 난다면 batch size 를 줄여볼 수 있습니다.

그리고, 더 정교한 모델을 원한다면 --cfg 의 yolo 모델을 다른 걸 사용할 수 있습니다.

지금까지 문제가 없다면 바로 학습이 시작될 것입니다.

![image](https://user-images.githubusercontent.com/77887166/130201451-9ed03a80-674a-4720-bec9-a8e919b0b619.png)


### 8. 학습 결과 확인하기
---
학습이 다 되었다면 yolov5 폴더의 runs/train/my_first_training 폴더가 새로 생길 것입니다.

폴더 안에는 학습 가중치가 저장된 weights 폴더 , 그리고 학습 결과 이미지가 같이 들어가 있습니다.

그리고 이 다음 학습된 결과를 통해 검출할 떄에 weights 폴더 안의 가중치 파일을 사용하게 됩니다.

**best.pt** 는 제일 학습 정확도가 높을 때의 가중치 , **last.pt** 는 가장 마지막의 가중치입니다. 


### 9. 학습한 가중치를 통해 예측하기
---
이제 학습이 잘 되었는지 확인해봅시다.

우선 사진을 예측하기 위해 다음의 코드를 새로운 cmd 창에 입력합니다. (예측할 사진 파일은 Dataset 폴더 안의 sample.jpg 로 저장해줍시다.)

```cmd
cd yolov5
python detect.py --img 416 --conf 0.5 --weights runs/train/my_first_training/weights/best.pt --source ../Dataset/sample.jpg 
```

--img 는 이미지 사이즈 , --conf 는 최소 정확도 , --weights 는 학습한 가중치가 저장된 경로 , --source 는 학습할 사진이 저장된 폴더입니다.

코드를 실행하면 runs/detect/exp 폴더 안의 예측 결과가 저장됩니다.

![image](https://user-images.githubusercontent.com/77887166/130202605-4c8d0d1b-9fcd-49fc-bb5a-8a3f9f3ed9e9.png)  (성능이 꽤나 준수합니다.)


웹캠을 통해 실시간으로 예측하고 싶으면 --source 만 다음과 같이 수정합니다.

```cmd
cd yolov5
python detect.py --img 416 --conf 0.5 --weights runs/train/my_first_training/weights/best.pt --source 0
```

그러면 웹캠을 통해 실시간으로 결과가 출력됩니다.

https://user-images.githubusercontent.com/77887166/130204204-52b60616-db7a-4f48-b11e-dc3d7d6856c7.mp4

꽤나 잘 맞추는 것으로 보입니다! 라벨링이 정교하고 학습을 더 한다면 예측결과는 더 좋을겁니다.

