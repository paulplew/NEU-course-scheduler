import shutil
from model import Schedule, Course

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

def print_day(schedule: Schedule, day: int):
    courses_on_day = []
    for course in schedule.get_courses():
        if course.meets_on_day(day):
            courses_on_day.append(course)
        # sort the courses in this day by their start time
    courses_on_day = sorted(courses_on_day, key=lambda x: x.startTime)

    # if there are no courses
    if len(courses_on_day) == 0:
        return
    
    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    data = []
    data.append(days[day])

    # add title info
    for course in courses_on_day:
        data.append(format_course_info(course))
    data.append("-" * terminal_width)
    
    print("\n".join(data))

def print_schedule(schedule: Schedule):
    for day in range(5):
        print_day(schedule, day)



def format_course_info(course: Course):
    course_dict = course.__dict__()

    return "\n".join([
        f'{course_dict["subject_course"]}: {course_dict["title"]}',
        f'CRN: {course_dict["course_registration_number"]}',
        f'{course_dict["building"]}: {course_dict["room"]} {course_dict["professor"]}',
        f'{course_dict["startTime"]} - {course_dict["endTime"]}'
    ])
