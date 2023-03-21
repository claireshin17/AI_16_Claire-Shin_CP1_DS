# Text Summarization Service 
- 본 서비스는 논문 및 레포트의 초록(1024자 이하)을 통해 짧은 주제문을 자동으로 생성하는 서비스입니다. 
- 요약/주제문을 추출할 .txt 파일의 요약문은 test.ipynb 파일을 실행해서 Jupyter Notebook 내에서 확인하거나 result 폴더에 생성되는 Excel 파일을 통해 확인 하실 수 있습니다. 

## Bringing the package to you
`$ git clone https://github.com/claireshin17/AI_16_Claire-Shin_CP1_DS` 

## Setting up the environment 
- `python==3.8` or higher
- Required packages:
```
pandas
openpyxl
torch==1.9.1
torchtext==0.10.1
torchvision==0.10.1
transformers==4.8.2
streamlit==1.1.0
pyyaml==5.4.1
pytorch_lightning==1.5.2
```
- 사용하실 conda 환경에 `$ pip install -r requirements.txt` 명령으로 필수 패키지를 모두 설치하실 수 있습니다. 

## 폴더 구조 
```
AI_16_Claire-Shin_CP1_DS
├── data
│   └── sample0.txt    # 요약할 txt 파일 위치 
├── model              # 서비스가 사용할 모델의 위치 
├── utils              # 전처리, 데이터 가져오기, 요약하기 함수가 있는 폴더
├── result
│   └── summary.xlsx   # 생성된 요약문 excel파일의 위치
│
├── README.md          # 사용설명서
├── test.ipynb         # 서비스 실행 파일
└── requirements.txt   # 서비스 실행을 위한 필수조건 
```
## 서비스 사용 방법
- 요약을 원하는 .txt 파일을  data 폴더 안에 넣습니다. 
- test.ipynb를 열어 각 셀을 실행시켜서 서비스를 실행합니다. 
