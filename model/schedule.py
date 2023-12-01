from model import Course

class Schedule:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    def __init__(self, courses: list[Course]):
        self._courses = courses;

    def get_courses(self) -> list[Course]:
        return self._courses;

    def weekday_as_str(self, day: str) -> str:
        assert day in self.days, f"Invalid day provided: {day}"

        index = self.days.index(day)

        weekday_course_info = [day]
        # loop through the courses and get their information as a string
        for course in self._courses:
            if not course.days[index]:
                continue
            course_str = str(course)
            course_str_lines = course_str.split("\n")
            # replace newlines with newline and then tab
            course_str = course_str.replace("\n", "\n\t")
            # add a tab to the first line
            course_str = "\t" + course_str

            weekday_course_info.append(course_str)

        # zip everything up with new lines
        return "\n".join(weekday_course_info)

    def __str__(self):
        course_strings = []
        for course in self._courses:
            course_strings.append(str(course))

        return "\n".join(course_strings)


