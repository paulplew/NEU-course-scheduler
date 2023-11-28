from typing import List
class Course:
    # We want to keep the: startn and end times, the days, the class title,
    # professor, CRN, room, and Credits
    def __init__(
        self,
        startTime: int,
        endTime: int,
        days: List[bool],
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
        
    def __str__(self) -> str:
        return self.title