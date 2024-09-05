import random

def show_multiplication_question():
    first_num = random.randint(1, 10)
    second_num = random.randint(1, 10)
    correct_answer = first_num * second_num
    
    print(f"What is {first_num} times {second_num}?")
    
    user_answer = int(input("Enter your answer: "))
    
    if user_answer == correct_answer:
        print("Correct! Good job!")
        return True
    else:
        print(f"Wrong answer. The correct answer is {correct_answer}. Keep practicing!")
        return False

def main():
    print("Welcome to the Multiplication Memory Training Program!")
    print("You will be given multiplication questions to practice your memory.")
    
    score = 0
    total_questions = 5
    
    for _ in range(total_questions):
        result = show_multiplication_question()
        if result:
            score += 1
            
    print(f"You completed the Memory Training Program! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    main()