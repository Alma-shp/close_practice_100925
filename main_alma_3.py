# consts
STARTING_HOUR = 8
DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
DAYS_DICT = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5}


def get_amount_of_days():
    days_amount = int(input("Enter the amount of days:"))
    while 7 <= days_amount:
        days_amount = int(input("Invalid days amount."
                                "Enter the amount of days:"))
    return days_amount


def get_hours_per_day():
    hours_amount = int(input("Enter the hours per day:"))
    while 9 <= hours_amount:
        hours_amount = int(input("Invalid hours amount. "
                                 "Enter the hours per day:"))
    return hours_amount


def is_lesson_valid(lesson: str, hours_per_day: int):
    """
    this function receives the 'lesson_input' from 'main()' and checks if is valid.
    :param lesson: str "name of class _ how many hours the class _ day _ starting hour"
    :param hours_per_day: number of hours per day
    :return: bool,problem indicator
    """
    # organizing the input:
    list_of_lesson = lesson.split("_")
    lesson_duration = int(list_of_lesson[1])
    lesson_starting_hour = int(list_of_lesson[3])
    lesson_day = list_of_lesson[2].lower()

    if lesson_duration > hours_per_day:
        problem = "lesson duration is too long."
        return False, problem
    elif lesson_starting_hour < 8:
        problem = "lesson is too early, the day starts at 8."
        return False
    elif lesson_starting_hour > (7 + hours_per_day):
        problem = f"lessons cant start after {7 + hours_per_day}."
        return False, problem
    elif lesson_day not in DAY_LIST:
        problem = "lesson day is not recognized."
        return False, problem
    else:
        problem = ""
        return True, problem


def canBeInserted(schedule: list, list_of_lesson: list):
    """
    this function checks the schedule for the specific lesson and returns if it can be inserted for part 3 or not.
    :param schedule: list of lists
    :param list_of_lesson:  of [name of class,how many hours the class,day,starting hour]
    :return: bool True if the lesson can be inserted, False if not.
    """
    # organizing the input:
    lesson_day = list_of_lesson[2].lower()
    lesson_duration = int(list_of_lesson[1])
    lesson_starting_hour = int(list_of_lesson[3])

    # indicator to what lesson are we currently running on:
    current_starting_hour = 8

    # iteration count when we run inside the range of the lesson:
    iterations = 0

    for hour in schedule[DAYS_DICT[lesson_day]]:
        if current_starting_hour >= lesson_starting_hour:
            if iterations <= lesson_duration:
                if hour != 'Free':
                    return False

        iterations += 1
        current_starting_hour += 1

    return True


def main():
    """
    the main function
    :return:
    """
    # inputs from the user:
    amount_of_days = get_amount_of_days()
    hours_per_day = get_hours_per_day()
    schedule = []
    #

    # part 1 - Initializing the schedule:
    for i in range(amount_of_days):
        schedule.append([])

    for day in schedule:
        for hour in range(hours_per_day):
            day.append("Free")
    #

    # part 2 - The data is inserted: [name of class]_[how many hours the class]_[day]_[starting hour]
    lessons_list = []
    lesson_input = input("Enter the data for the lesson: ")
    while lesson_input != "done":
        valid, problem = is_lesson_valid(lesson_input, hours_per_day)
        if valid:
            lessons_list.append(lesson_input)
        else:
            print(problem)
            print("please enter again: ")

        lesson_input = input("Enter the data for the lesson: ")
    #

    # part 3- Initial insertion of lessons

    # the lessons we will try to place in part 4:
    problematic_lessons = []

    for lesson in lessons_list:
        # getting the info organized:
        list_of_lesson = lesson.split("_")
        lesson_name = list_of_lesson[0]
        lesson_duration = int(list_of_lesson[1])
        lesson_starting_hour = int(list_of_lesson[3])
        lesson_day = list_of_lesson[2].lower()

        # checking if the lesson can be inserted:
        if canBeInserted(schedule, list_of_lesson):
            # placing the lesson :
            current_starting_hour = 8
            iterations = 0
            for hour_index in range(len(schedule[DAYS_DICT[lesson_day]])):
                if current_starting_hour >= lesson_starting_hour:
                    if iterations < lesson_duration:
                        schedule[DAYS_DICT[lesson_day]][hour_index] = lesson_name
                    iterations += 1
                current_starting_hour += 1

        # if the lesson cannot be inserted:
        else:
            problematic_lessons.append(lesson)

    # schedule print:
    print()
    print("schedule after first insertion: ")
    for i in range(amount_of_days):
        print(DAY_LIST[i] + ": ")
        for day in schedule[i]:
            print(day, end=" ")
        print()

    #


main()
