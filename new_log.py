# new_log.py
import os
from datetime import datetime

# 오늘 날짜 구하기
today = datetime.now()
year = today.strftime("%Y")
date_str = today.strftime("%Y-%m-%d")

# 경로 설정 (docs/log/2026/2026-01-27.md 형태)
folder_path = os.path.join("docs", "log", year)
file_path = os.path.join(folder_path, f"{date_str}.md")

# 폴더 없으면 생성
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 파일 내용 템플릿 (형이 원하는 대로 수정 가능)
content = f"""# {date_str} 연구 노트

## 📝 오늘 할 일
- [ ] 

## 🧠 아이디어 & 메모
- 

## 🔬 실험/시뮬레이션 로그
- 
"""

# 파일 생성 (이미 있으면 건너뜀)
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"생성 완료: {file_path}")
else:
    print("이미 파일이 존재해")