import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a',
    encoding='utf-8'
)

logging.debug("디버그 메시지")
logging.info("정보 메시지")
logging.warning("경고 메시지")
logging.error("에러 메시지")
logging.critical("치명적 메시지")