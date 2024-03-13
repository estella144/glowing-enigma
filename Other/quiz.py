print("Quiz 0.2.1, 6 Mar 2023, by Oliver Nguyen")
print("Test release, Last commit: da2c91c\n")

class Quiz:
    """Quiz"""

    def __init__(self, questions):
        x = 0
        for i in questions:
            questions[questions.index(i)] = Question(i[0], i[1].lower())
        self.questions = questions

    def ask(self):
        number_of_questions = len(self.questions)
        correct_answers = 0
        username = input("What is your name? ")
        for i in self.questions:
            x = i.ask()
            if x:
                correct_answers += 1

        percent_correct_answers = (correct_answers / number_of_questions) * 100
        print("\n" + username + ", you scored", str(correct_answers)) 
        print("You answered", str(round(percent_correct_answers, 1)) + "% of questions correctly.")
        input("Press ENTER to quit the quiz")

class Question:
    """Question in a quiz"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        print("Question:", self.question, "\nAnswer:", self.answer)

    def ask(self):
        answer = input(self.question + " ")
        if answer == self.answer.lower():
            print("Correct")
            return True
        else:
            print("Incorrect. The answer is", self.answer)
            return False

# Type all answers in lowercase
q_list = [["Do integers have quotes around them? [YES/NO]", "no"],
          ["What is the data type which is True or False called?", "boolean"],
          ["What is the assignment symbol in Python?", "="],
          ["What is a piece of data with a name and value which can change called?", "variable"],
          ["Can an integer store a decimal? [YES/NO]", "no"]]
          
q = Quiz(q_list)
q.ask()
