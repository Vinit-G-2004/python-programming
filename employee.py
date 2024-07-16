def evaluate_performance():
    print("Welcome to the Employee Performance Evaluation System\n")
    productivity = int(input("Rate the employee's productivity on a scale of 1 to 10: "))
    communication = int(input("Rate the employee's communication skills on a scale of 1 to 10: "))
    teamwork = int(input("Rate the employee's teamwork abilities on a scale of 1 to 10: "))
    punctuality = int(input("Rate the employee's punctuality on a scale of 1 to 10: "))
    total_score = productivity + communication + teamwork + punctuality
    if total_score >= 35:
        performance = "Excellent"
    elif total_score >= 30:
        performance = "Good"
    elif total_score >= 25:
        performance = "Satisfactory"
    else:
        performance = "Needs Improvement"
    print("\nEvaluation Result:")
    print("Total Score:", total_score)
    print("Performance Level:", performance)
evaluate_performance()
