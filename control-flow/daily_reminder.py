task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task that does not require immediate attention today")

    case "medium":
        if time_bound ==  "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention soon!")
        else:
            print(f"Note: {task} is a medium priority task that does not require immediate attention today")

    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task that does not require immediate attention today.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time")



