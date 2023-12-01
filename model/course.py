from useful_functions import military_to_standard

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
        crn: int,
        room: int,
        building: str,
        credit_hours: int,
    ):
        self.startTime = startTime
        self.endTime = endTime
        self.days = days
        self.title = title
        self.subject_course = subject_course
        self.professor = professor
        self.course_registration_number = crn
        self.room = room
        self.building = building
        self.credit_hours = credit_hours


    # used by calling str(a) when a is a Course
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
            f"{military_to_standard(self.startTime)} - {military_to_standard(self.endTime)}",
            f"{self.building} {self.room}"
        ])
        return all_info
