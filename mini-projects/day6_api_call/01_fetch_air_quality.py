"""
미세먼지 API 호출 스크립트
Date: 2026-04-24
"""
import os
from dotenv import load_dotenv
import requests
import csv
from datetime import date
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='air_quality.log',
    filemode='a',
    encoding='utf-8'
)

logging.info("=" * 50)
logging.info("미세먼지 데이터 수집 시작")

# 환경변수 로드
load_dotenv()
API_KEY = os.getenv("AIR_API_KEY")

if not API_KEY:
    logging.error("API 키를 찾을 수 없습니다. .env 파일 확인")
    exit(1)

# API 설정 
BASE_URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

params = {
    "serviceKey": API_KEY,
    "returnType": "json",
    "numOfRows": 100,
    "pageNo": 1,
    "sidoName": "서울",
    "ver": "1.3"
}

# 1. API 호출
try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    logging.info(f"HTTP 상태 코드: {response.status_code}")
except requests.exceptions.RequestException as e:
    logging.error(f"API 호출 실패: {e}")
    exit(1)

# 2. JSON 파싱
try:
    data = response.json()
    items = data['response']['body']['items']
    logging.info(f"API 응답 수신: 측정소 {len(items)}개")
except (KeyError, ValueError) as e:
    logging.error(f"응답 파싱 실패: {e}")
    logging.error(f"응답 원본: {response.text[:200]}")
    exit(1)

# 3. CSV 저장
today = date.today().isoformat()
filename = f"air_quality_{today}.csv"
fieldnames = ["sidoName", "staionName", "dataTime", "pm10Value", "pm25Value"]

try:
    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            row = {field: item.get(field) for field in fieldnames}
            writer.writerow(row)
    logging.info(f"CSV 저장 완료: {filename} ({len(items)}개 측정소)")
except PermissionError:
    logging.error(f"파일 저장 실패: {filename} 이 다른 프로그램에서 사용 중일 수 있습니다.")
    exit(1)
except Exception as e: 
    logging.error(f"파일 저장 중 예기치 않은 에러: {e}")
    exit(1)

logging.info("작업 종료")