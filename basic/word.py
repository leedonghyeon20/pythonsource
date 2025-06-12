# word.txt 파일을 읽어서 단어문제 출제
# word.txt 읽어와서 리스트에 담아서 출력

# word.py가 실행되고 있는 경로 가져오기
import os
import random
import time
import sqlite3
from datetime import datetime

print("현재폴더 ", os.getcwd())

conn = sqlite3.connect("./basic/test.db", isolation_level=None)

words = []
with open("./basic/data/word.txt", "r") as f:
    for w in f:
        words.append(w.strip())

# print(words)

# 5 문제 출제 :
# 리스트 섞어주기
# 임의로 하나 추출
n = 1
correct_answer = 0

input("게임을 시작할까요? 엔터입력")
start = time.time()  # 시작시간

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print()

    print(f"* Question {n}")
    print(q)
    # user 는 문제를 타이핑
    answer = input("단어 입력 : ")
    # 문제와 user 가 작성한 값이 일치하는 지 확인
    if answer.strip() == q.strip():
        print("정답!!!")
        # 정답 개수 count 처리
        correct_answer += 1
    else:
        print("오답...")

    n += 1

end = time.time()  # 종료시간
et = format(end - start, ".3f")
print(f"게임시간 : {et}, 정답개수 : {correct_answer}")

# 정답 개수 3개 이상이면 합격
if correct_answer >= 3:
    print("합격")
else:
    print("불합격")


# DB 저장
# records 테이블 생성 - 정답개수(integer) , 기록(et), regdate
cursor = conn.cursor()
sql = "create table if not exists records(correct_answer integer, record text, regdate text)"
cursor.execute(sql)

sql = "insert into records(correct_answer, record, regdate) values(?,?,?)"
now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
cursor.execute(sql, (correct_answer, et, nowDateTime))

conn.close()
