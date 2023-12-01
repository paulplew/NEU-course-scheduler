from typing import Final

from .api_utils import get
from .post import clearAuthentication, authenticate
from course_model import Course

# Check docs here for more information about these endpoints https://apidocs.searchneu.com/banner/apiSpec.html
# the url used to find term information
TERM_URL: Final = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?offset={}&max={}&searchTerm={}"
# The url used to search for subjects (we don't really use this)
SUBJECTS_URL: Final = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/classSearch/get_subject?searchTerm={}&term={}&offset={}&max={}"
# The url used to search for courses and information cookies must be used when
# pushing here
SEARCH: Final = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_subject={}&txt_courseNumber={}&txt_term={}&pageOffset={}&pageMaxSize={}"
SPRING_2024: Final = 202430


def get_terms(page=1, num_results=10, search_term="") -> list[dict[str,str]]:
    QUERY_URL = TERM_URL.format(page, num_results, search_term)
    return get(QUERY_URL).json()

def search_classes(subject: str, course_number: int, page=0, num_results=50) -> list[Course]:
    QUERY_URL = SEARCH.format(subject, course_number, SPRING_2024, page, num_results)

    cookies = authenticate(SPRING_2024)
    # have to get with the headers that we got before
    response = get(QUERY_URL, cookies=cookies)
    search_results = response.json()
    
    courses = []
    for item in search_results["data"]:
        try:
            professor = item["faculty"][0]["displayName"]
            subject_course = item["subjectCourse"]
            title = item["courseTitle"]
            startTime = item["meetingsFaculty"][0]["meetingTime"]["beginTime"]
            endTime = item["meetingsFaculty"][0]["meetingTime"]["endTime"]
            building = item["meetingsFaculty"][0]["meetingTime"]["buildingDescription"]
            room = item["meetingsFaculty"][0]["meetingTime"]["room"]
            days = [
                item["meetingsFaculty"][0]["meetingTime"]["monday"],
                item["meetingsFaculty"][0]["meetingTime"]["tuesday"],
                item["meetingsFaculty"][0]["meetingTime"]["wednesday"],
                item["meetingsFaculty"][0]["meetingTime"]["thursday"],
                item["meetingsFaculty"][0]["meetingTime"]["friday"],
            ]
            course_reference_number = item["meetingsFaculty"][0]["courseReferenceNumber"]
            credit_hours = item["meetingsFaculty"][0]["meetingTime"]["creditHourSession"]
            
            courses.append(Course(
                startTime, 
                endTime, 
                days, 
                title, 
                subject_course,
                professor, 
                course_reference_number, 
                room, 
                building, 
                credit_hours,
                ))
        except IndexError:
            continue
        except TypeError:
            continue

        
    return courses
    
