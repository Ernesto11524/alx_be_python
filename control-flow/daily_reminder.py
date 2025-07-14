task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            result = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            result = f"'{task}' is a high priority task. Consider completing it when you are less busy!"
    case 'medium':
        if time_bound == 'yes':
            result = f"'{task}' is a medium priority task that requires immediate attention today!"
        else:
            result = f"'{task}' is a medium priority task. Consider completing it when you are less busy!"
    case 'low':
        if time_bound == 'yes':
            result = f"'{task}' is a low priority task that requires immediate attention today!"
        else:
            result = f"'{task}' is a low priority task. Consider completing it when you are free!"

print(f"Reminder: {result}")