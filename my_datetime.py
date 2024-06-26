import datetime
# Print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

first_name='Susan'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('look completed')