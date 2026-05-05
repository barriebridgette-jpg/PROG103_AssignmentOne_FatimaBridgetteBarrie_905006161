#Student grade calculator
try:
    print("Insert score1: ")
    score1 = float(input())
    print("Insert score2: ")
    score2 = float(input())
    print("Insert score3: ")
    score3 = float(input())
    if score1 >= 0 and score1 <= 100 and score2 >= 0 and score2 <= 100 and score3 >= 0 and score3 <= 100:
        average = (score1 + score2 + score3) / 3
        print("The average score is: " + str(average))
except ValueError:
    print("Error: Invalid input. Numbers accepted only")

