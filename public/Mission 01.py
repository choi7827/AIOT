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
