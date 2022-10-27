# assignment

# getting start
메인 디렉토리에서 실행
```bash
$ python -m venv .< your venv name >
$ . .< your venv name >/bin/activate
```

## 크롤링
해당 과제에서 1년간의 데이터를 수집하고 모델링을 진행해야 하므로, 임의로 2019년도를 지정하여 크롤링을 진행하였습니다.

수집하고 싶은 연도를 입력하면 해당 연도의 파일이 data 폴더에 저장됩니다.
```bash
$ python crawling.py
Please enter the year : 
```

## model
정확한 input이 주어져있지 않고, 대부분의 데이터들이 상관관계가 높으므로 단순하게 모든 결과를 활용하여 머신러닝으로 접근하기보다는, 시계열 모델로 접근하여 오로지 pm10으로만 모델링을 진행하였습니다.

학습데이터가 너무 적은편이라서, window_size를 15로 설정하였고, 최종적으로 모델 결과는 원하는 날짜의 이전 pm10 데이터 15개를 보내면 해당 날짜의 pm10을 뽑아내는 것으로 진행하였습니다.

현재 모델은 2019년도 해당 1년간의 데이터를 토대로 pm10에 대해서 lstm으로 학습을 진행하였으므로, 2020년에 해당하는 특정 날짜릅 입력하면 이전 날짜 15일을 api로 정보를 수집하여 특정 날짜의 pm10을 예측하여 결과를 보여줍니다.

api 상으로 15개의 입력값을 입력받는 것이 불편하다고 생각하였기 때문에, 현재는 이러한 형태로 제작하였습니다. 



# API test
아래 명령어를 통해 api 서버를 실행시킨 후에, 'http://localhost:8000/docs' 해당 링크로 들어가서 API 테스트를 보낼 수 있습니다.

## local start

### install dependencies
```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### start web-serverr
```bash
$ cd ./src
$ uvicorn main:app --reload --port <your port>
```

## docker start

```bash
$ docker-compose up
```

## API 형식
- 연도는 API 사이트에서 제공하는 1987년 부터 2020년까지만 제공하므로, 해당 연도 안에서 입력을 하면 됩니다.
- 한글자치구명은 강남구, 중구와 같이 서울 지역의 해당 자치구명을 입력하면 됩니다.

```python
POST /assignment/predict_dust
{
  "date": "20200320",
  "region": "강남구"
}
```
```python
결과
{
  "pm10": 39.17774963378906
}
```


