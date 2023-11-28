from api_controller import search_classes

print("Welcome to the NEU automatic course scheduler program.")
classes = input("Please input the class codes for the classes you wish to take next semester in the following format: CS2500, ECON3100, ART1200 \n").upper()

courses = []
course_titles = []
for course in classes.split(", "):
    course_titles.append(course)
    course = [course[:-4], course[-4:]]
    courses.append(search_classes(course[0], course[1]))
    
valid_courses = []
valid_course_titles = []
for course, title in zip(courses, course_titles):
    # check if course is empty
    if not course:
        print(f"The course {title} does not exist. Continuing without that course.")
    else:
        valid_courses.append(course) 
        valid_course_titles.append(title) 
courses = valid_courses
course_titles = valid_course_titles

time_pref = input("Please enter m, a, or e to signift whether you'd prefer morning, afternoon, or evening classes.\n").lower()
while (time_pref != 'm' and time_pref != 'a' and time_pref != 'e'):
    time_pref = input("Sorry, your previous response was not accepted, please try again between m for morning, a for afternoon, or e for evening classes.")


day_off = input("If you could have one day a week off, which would it be? Please enter mon, tue, wed, thur, or fri. \n").lower()
while (day_off != "mon" and day_off != "tue" and day_off != "wed" and day_off != "thur" and day_off != "fri"):
    day_off = input("Your last reponse was not accepted, please try again to choose between whether you'd like mon, tue, wed, thur, or fri with no classes.")

time_between = input("Lastly, please enter the number of minutes that would be ideal to have as a gap between classes. \n")


print("Is this correct?")
print("classes - ", courses)
print("time prefferred - ",  time_pref)
print("ideal day off - ", day_off)
print("ideal time between classes - ", time_between)