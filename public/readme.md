✅ 1. 프로그램 개요 – "할 일 목록(Todo List) CLI 프로그램"
이 프로그램은 명령어 기반으로 작동하며, 사용자가 해야 할 일을 추가, 확인, 삭제할 수 있게 해주는 간단한 CLI 앱입니다.

📁 2. 파일 구성
arduino
복사
편집
/public
├── todo.py
└── README.md
🧾 3. todo.py (업로드할 파이썬 파일)
python
복사
편집
# todo.py

import json
import os

TODO_FILE = "todo_list.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def show_todos():
    todos = load_todos()
    if not todos:
        print("할 일이 없습니다.")
    else:
        print("\n[할 일 목록]")
        for i, item in enumerate(todos, start=1):
            print(f"{i}. {item}")

def add_todo():
    task = input("추가할 할 일을 입력하세요: ")
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print("✅ 할 일이 추가되었습니다.")

def remove_todo():
    show_todos()
    try:
        idx = int(input("삭제할 번호를 입력하세요: ")) - 1
        todos = load_todos()
        if 0 <= idx < len(todos):
            removed = todos.pop(idx)
            save_todos(todos)
            print(f"🗑️ '{removed}' 삭제 완료.")
        else:
            print("❌ 유효하지 않은 번호입니다.")
    except ValueError:
        print("❌ 숫자를 입력해주세요.")

def main():
    while True:
        print("\n--- 할 일 목록 프로그램 ---")
        print("1. 할 일 보기")
        print("2. 할 일 추가")
        print("3. 할 일 삭제")
        print("4. 종료")

        choice = input("선택 (1-4): ")

        if choice == "1":
            show_todos()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            remove_todo()
        elif choice == "4":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 선택입니다.")

if __name__ == "__main__":
    main()
📝 4. README.md
markdown
복사
편집
# ✅ 할 일 목록 CLI 프로그램

누군가의 하루를 더 잘 정리하게 도와주는 간단한 명령어 기반의 Todo 프로그램입니다.

---

## 📦 파일 구성
- `todo.py`: 메인 파이썬 실행 파일
- `todo_list.json`: 할 일 목록이 저장되는 파일 (자동 생성됨)

---

## 🛠️ 사용 방법

1. 터미널에서 실행:
   ```bash
   python todo.py
메뉴에서 원하는 작업을 선택하세요:

1: 현재 할 일 보기

2: 새 할 일 추가

3: 기존 할 일 삭제

4: 종료

💡 예시
text
복사
편집
--- 할 일 목록 프로그램 ---
1. 할 일 보기
2. 할 일 추가
3. 할 일 삭제
4. 종료
선택 (1-4): 2
추가할 할 일을 입력하세요: 수학 숙제

✅ 할 일이 추가되었습니다.



## 설명

✅ 완성된 README.md
markdown
복사
편집
# ✅ 할 일 목록 CLI 프로그램

누군가의 하루를 더 잘 정리하게 도와주는 간단한 명령어 기반의 Todo 프로그램입니다.

---

## 📖 설명

이 프로그램은 파이썬으로 만든 **할 일(To-Do) 목록 관리 도구**입니다.  
명령줄(Command Line)에서 실행되며, 사용자는 다음과 같은 작업을 할 수 있습니다:

- 해야 할 일을 **추가**
- 등록된 할 일 목록을 **확인**
- 완료된 일을 목록에서 **삭제**

모든 할 일은 로컬 파일(`todo_list.json`)에 자동으로 저장되어, 프로그램을 다시 실행해도 데이터가 유지됩니다.

이 프로그램은 파이썬의 기본 기능만을 사용하여 제작되어 별도의 설치가 필요 없습니다.  
**학생, 직장인, 개발자 등** 누구나 사용할 수 있습니다.

---

## 📦 파일 구성

/public
├── todo.py # 메인 프로그램
├── todo_list.json # 할 일 데이터 저장용 (자동 생성됨)
└── README.md # 프로그램 사용법 및 설명

yaml
복사
편집

---

## 🛠️ 사용 방법

### 1. 실행
터미널(명령 프롬프트)에서 아래 명령어 입력:

```bash
python todo.py
2. 메뉴에서 선택
text
복사
편집
--- 할 일 목록 프로그램 ---
1. 할 일 보기
2. 할 일 추가
3. 할 일 삭제
4. 종료
선택 (1-4):
💡 예시
text
복사
편집
선택 (1-4): 2
추가할 할 일을 입력하세요: 수학 숙제

✅ 할 일이 추가되었습니다.

선택 (1-4): 1

[할 일 목록]
1. 수학 숙제
📌 기능 요약
기능	설명
할 일 보기	현재 등록된 할 일 목록을 출력
할 일 추가	새로운 할 일을 입력 받아 추가
할 일 삭제	목록에서 특정 항목을 삭제
데이터 저장	todo_list.json 파일로 자동 저장
