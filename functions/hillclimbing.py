from course_model import Course
from random_functions.py import days_of_week, avg_time_between, tod_match

# takes in a list of courses and the user's prefferences and calculates the schedules' energy
def energy_function(schedule, tod_pref, day_off_pref, time_betweem_pref):
    energy = 0
    day_off = True
    for course in schedule:
        if (tod_match(course.startTime, tod_pref)):
            energy += 15
        if (day_off_pref in days_of_week(course.days))
            day_off = False
    if day_off:
        energy += 50
    avg_time_between_classes = avg_time_between(schedule)
    energy -= abs(time_betweem_pref - avg_time_between_classes)
    return energy

        
