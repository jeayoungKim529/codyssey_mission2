#main.py

from utils import *
from classes.class_quiz import Quiz
from classes.class_quizgame import QuizGame


def start_quiz(quizGame):
    quizGame.load_data()
    while True:
        quizGame.print_menu()
        menu_num = check_num("선택: ", 5)

        if menu_num == 1:
            quizGame.quiz_play()
        elif menu_num == 2:
            quizGame.quiz_add()
        elif menu_num == 3:
            quizGame.quiz_list()
        elif menu_num == 4:
            quizGame.check_score()
        elif menu_num == 5:
            print("exit")
            break
        else: #허용 범위 밖 숫자
            pass

def main():
    quizGame = QuizGame()
    start_quiz(quizGame)
    quizGame.save_data()

if __name__ == "__main__":
    main()