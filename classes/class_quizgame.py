#class_quizgame.py

import json
from classes.class_quiz import Quiz
from utils import *

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0 #최고 점수
    #
    #메뉴표시
    def print_menu(self):
        print("========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")
    #
    #퀴즈 풀기
    def quiz_play(self):
        #퀴즈가 없는 경우
        if len(self.quizzes) == 0:
            print("⚠️ 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
            return
        #퀴즈가 있는 경우
        score = 0
        print()
        for q in self.quizzes:
            print("[문제]")
            print(q.question)
            for i in range(4):
                print(f"[{i + 1}] {q.choices[i]}")
            answer = check_num("정답: ", 4) #정답 입력
            if answer == q.answer: #정답/오답 여부
                print("✅ 정답입니다!\n")
                score += 1
            else:
                print("❌ 오답입니다!\n")
        print("========================================") #결과 표시
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if self.best_score < (score / len(self.quizzes) * 100):
            self.best_score = (score / len(self.quizzes) * 100)
            print("🎉 새로운 최고 점수입니다!")
        print("========================================\n")
    #
    #퀴즈 추가
    def quiz_add(self):
        print("\n📌 새로운 퀴즈를 추가합니다.\n")
        question = input("문제: ")
        choices = []
        for i in range(4):
            choices.append(input(f"선택지[{i + 1}]: "))
        answer = check_num("정답: ", 4)
        while answer == 0:
            answer = check_num("정답: ", 4)
        self.quizzes.append(Quiz(question, choices[0], choices[1], choices[2], choices[3], answer))
        print("\n✅ 퀴즈가 추가되었습니다!\n")
        # self.save_data()
    #
    #목록 보기
    def quiz_list(self):
        #퀴즈가 없는 경우
        if len(self.quizzes) == 0:
            print("⚠️ 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
            return
        #퀴즈가 있는 경우
        print()
        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        for q in self.quizzes:
            q.print_quiz()
    #
    #점수 확인
    def check_score(self):
        print(f"🏆 최고 점수: {self.best_score}점\n")
    #
    #파일 저장
    def save_data(self):
        try:
            state = {
                "quizzes": [quiz.to_dict() for quiz in self.quizzes],
                "best_score": self.best_score
            }
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent =4)
        except Exception as e:
            handle_file_exception(e)
    #
    #파일 불러오기
    def load_data(self):
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                state = json.load(f)
            self.quizzes = [
                Quiz(q["question"], q["choices"][0], q["choices"][1], q["choices"][2], q["choices"][3], q["answer"])
                for q in state["quizzes"]
            ]
            self.best_score = state["best_score"]
            print(f"\n📂 저장된 데이터를 불러왔습니다.\n퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점\n")
        except Exception as e:
            handle_file_exception(e)