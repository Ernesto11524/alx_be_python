task = input('Enter a task: ')
priority = input('What is the priority of the task (high, medium, low): ').lower()
time_bound = input('Is the task time-bounded? (yes or no): ').lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            result = f"{task} is a high priority task that requires immediate attention today!"
        else:
            result = f"{task} is a high priority task. Consider completing it when you are less busy!"
    case 'medium':
        if time_bound == 'yes':
            result = f"{task} is a medium priority task that requires immediate attention today!"
        else:
            result = f"{task} is a medium priority task. Consider completing it when you are less busy!"
    case 'low':
        if time_bound == 'yes':
            result = f"{task} is a low priority task that requires immediate attention today!"
        else:
            result = f"{task} is a low priority task. Consider completing it when you are free!"

print(result)