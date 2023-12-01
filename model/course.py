from datetime import datetime
from copy import deepcopy 

class Course:
    # We want to keep the: startn and end times, the days, the class title,
    # professor, CRN, room, and Credits
    def __init__(
        self,
        startTime: str, # military time string such as "1530"
        endTime: str, # military time string such as "1530"
        days: list[bool],
        title: str,
        subject_course: str,
        professor: str,
        course_registration_number: int,
        room: int,
        building: str,
        credit_hours: int,
    ):
        self.startTime = datetime.strptime(startTime, "%H%M")
        self.endTime = datetime.strptime(endTime, "%H%M")
        self.days = days
        self.title = title
        self.subject_course = subject_course
        self.professor = professor
        self.course_registration_number = course_registration_number
        self.room = room
        self.building = building
        self.credit_hours = credit_hours

    def meets_on_day(self, day: int):
        assert day < 5, "Day should be in the range of 0-4"
        return self.days[day]


    # used to make a dict from the course
    def __dict__(self):
        return {
            "startTime": self.startTime,
            "endTime": self.endTime,
            "days": self.days,
            "title": self.title,
            "subject_course": self.subject_course,
            "professor": self.professor,
            "course_registration_number": self.course_registration_number,
            "room": self.room,
            "building": self.building,
            "credit_hours": self.credit_hours,
        }

    def __str__(self) -> str:
        # XX1234 title
        # CRN: course_registration_number
        # credit_cours credits
        # ------------------------------
        # startTime - endtime
        # buildling room

        all_info = "\n".join([
            f"{self.subject_course} | {self.title}",
            f"CRN: {self.course_registration_number}",
            f"{self.credit_hours} credits"
            f'{self.startTime.strftime("%I:%M %p")} - {self.endTime.strftime("%I:%M %p")}',
            f"{self.building} {self.room}"
        ])
        return all_info

    def __deepcopy__(self, memo):
        dictionary = deepcopy(self.__dict__(), memo)
        dictionary["startTime"] = dictionary["startTime"].strftime("%H%M")
        dictionary["endTime"] = dictionary["endTime"].strftime("%H%M")

        return self.__class__(**dictionary)
