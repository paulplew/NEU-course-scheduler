from datetime import datetime
import random
from itertools import product

# turns a list of [False, True, False, False, True] into ["tue", "fri"]
def days_of_week(list):
    days = []
    if list[0]:
        days.append("mon")
    if list[1]:
        days.append("tue")
    if list[2]:
        days.append("wed")
    if list[3]:
        days.append("thur")
    if list[4]:
        days.append("fri")
    return days

# "0915" => "9:15 AM"
# "1600" => "4:00 PM"
def military_to_standard(string_time: str) -> str:
    time = datetime.strptime(string_time, "%H%M")
    return time.strftime("%I:%M %p")

# list of courses => rounded avg time between classes in min
# lsit turns into dictionary like {"mon": [(915, 1020), (1030, 1135)], "tue" : [(800, 945)], etc}
def avg_time_between(listof_courses):
    schedule_dict = {"mon": [],"tue": [],"wed": [],"thur": [],"fri": []}
    total_gap = 0
    n = 0
    for course in listof_courses:
        if course.days[0]:
            schedule_dict["mon"].append((course.startTime, course.endTime))
        if course.days[1]:
            schedule_dict["tue"].append((course.startTime, course.endTime))
        if course.days[2]:
            schedule_dict["wed"].append((course.startTime, course.endTime))
        if course.days[3]:
            schedule_dict["thur"].append((course.startTime, course.endTime))
        if course.days[4]:
            schedule_dict["fri"].append((course.startTime, course.endTime))
    for day in schedule_dict:
        # sorts each day in order of start times
        schedule_dict[day].sort(key=lambda x: x[0])
        if len(schedule_dict[day]) > 1:
            for i in range(len(schedule_dict[day])-1):
                gap = (datetime.strptime(schedule_dict[day][i+1][0],"%H%M") - datetime.strptime(schedule_dict[day][i][1],"%H%M"))
                hours, minutes, seconds = map(int, str(gap).split(':'))
                total_gap += hours * 60 + minutes
                n+=1

    # if there are no gaps 
    if n==0:
        return None
    return round(total_gap / n)

# takes a classes start time and prefferred time of day and returns a boolean whether it matches
def time_of_day_score(startTime, tod_pref):
    # morning more points as it approaches 8:00am
    # afternoon more points at is approaches 1:00pm
    # evening more points as it approaches 4:30pm
    goal_time = -1
    if tod_pref == "m":
        goal_time = 800
    elif tod_pref == "a":
        goal_time = 1300
    elif tod_pref == "e":
        goal_time = 1630

    assert goal_time != -1, f"Incorrect time of day preference provided: {tod_pref}"
    
    if startTime is None:
        # the class is async
        return 0

    # every hour away from the goal is -25 points from the starting 50 points
    return 50 - ((abs(goal_time - int(startTime)) // 60) * 25)
 
# generates a random schedule from the 2d list of courses
def schedule_generator(listoflistsof_courses):
    if len(listoflistsof_courses) > 0:
        # list of all course combinations
        all_schedules = [item for item in product(*listoflistsof_courses)]
        #shuffle the list so we check them randomly (trying to make sure we don't get the same schedule everytime)
        random.shuffle(all_schedules)
        #iterate through combinations and return first valid one
        for s in all_schedules:
            if valid_schedule(s):
                return list(s)
        print('ERROR, NO VALID SCHEDULES POSSIBLE')
    else:
        print("ERROR, COURSES PROVIDED")




# determines whether provided schedule is valid (classes don't overlap)
def valid_schedule(schedule):
    schedule_dict = {"mon": [],"tue": [],"wed": [],"thur": [],"fri": []}
    valid = True
    for course in schedule:
        if course.days[0]:
            schedule_dict["mon"].append((course.startTime, course.endTime))
        if course.days[1]:
            schedule_dict["tue"].append((course.startTime, course.endTime))
        if course.days[2]:
            schedule_dict["wed"].append((course.startTime, course.endTime))
        if course.days[3]:
            schedule_dict["thur"].append((course.startTime, course.endTime))
        if course.days[4]:
            schedule_dict["fri"].append((course.startTime, course.endTime))
    for day in schedule_dict:
        # sorts each day in order of start times
        schedule_dict[day].sort(key=lambda x: x[0])
        if len(schedule_dict[day]) > 1:
            for i in range(len(schedule_dict[day])-1):
                gap = (int(schedule_dict[day][i+1][0]) - int(schedule_dict[day][i][1]))
                if gap <= 0:
                    valid = False
    return valid