def main():
    score = 0

    print("==============================")
    print("       PYTHON QUIZ GAME")
    print("==============================")

    print("\n1. What is the capital of India?")
    print("A. Mumbai")
    print("B. New Delhi")
    print("C. Kolkata")
    print("D. Chennai")

    answer = input("Enter your answer: ")

    if answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is B.")

    print("\n2. Which language are we using?")
    print("A. Java")
    print("B. C++")
    print("C. Python")
    print("D. HTML")

    answer = input("Enter your answer: ")

    if answer.upper() == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is C.")

    print("\n3. Which keyword is used to define a function?")
    print("A. function")
    print("B. def")
    print("C. fun")
    print("D. define")

    answer = input("Enter your answer: ")

    if answer.upper() == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is B.")

    print("\n==============================")
    print("         QUIZ RESULT")
    print("==============================")
    print("Your score:", score, "/ 3")

    percentage = (score / 3) * 100
    print("Percentage:", percentage, "%")


if __name__ == "__main__":
    main()