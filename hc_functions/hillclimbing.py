from course_model import Course
from useful_functions import days_of_week, avg_time_between, tod_match, valid_schedule
import random


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


def hillclimb(schedule, tod_pref, day_off_pref, time_betweem_pref, iterations, all_courses):
      	# variables to hold the best results 
    best_solution = schedule
    best_energy = energy_function(schedule, tod_pref, day_off_pref, time_betweem_pref)
    num_classes = len(schedule)
    
    for i in range(iterations):
		#a random class index in the schedule and num of possible courses for that class
        class_idx = random.randint(0, num_classes-1)
        num_courses = len(all_courses[class_idx])
		
		# copy of the current best maze
        new_schedule = best_solution

		# upating the random class to be a random course form the 2d list of all courses
        new_schedule[class_idx] = all_courses[class_idx][random.randint(0,num_courses-1)]

		# prevents the tile change from creating an unsolvable maze
        while not valid_schedule(new_schedule):
            new_schedule[class_idx] = all_courses[class_idx][random.randint(0,num_courses-1)]

		# finds the energy value of the new maze
        new_energy = energy_function(new_schedule, tod_pref, day_off_pref, time_betweem_pref)

		# compares the new energy value to the previous best
        if  new_energy < best_energy:
            best_solution = new_schedule
            best_energy = new_energy


    return best_solution, best_energy

        
def hillclimb_random_restarts(schedule, tod_pref, day_off_pref, time_betweem_pref, iterations, num_restarts, all_courses):
	# variables to hold the best results 
	best_solution = schedule
	best_energy = energy_function(schedule, tod_pref, day_off_pref, time_betweem_pref)

	for i in range(num_restarts):
		new_solution, new_energy = hillclimb(schedule, tod_pref, day_off_pref, time_betweem_pref, iterations, all_courses)
		if new_energy < best_energy:
			best_solution = new_solution
			best_energy = new_energy

	return best_solution, best_energy