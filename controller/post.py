from typing import Final

from .api_utils import post
from requests.cookies import RequestsCookieJar

SET_TERM_URL: Final = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/term/search?mode=search"
CLEAR_TERM_URL: Final = "https://nubanner.neu.edu/StudentRegistrationSsb/ssb/classSearch/resetDataForm"

def authenticate(term_id: int) -> RequestsCookieJar:
    payload: Final = {"term": term_id}
    headers: Final = { "Content-Type": "application/x-www-form-urlencoded; charset=UT;", }

    response = post(SET_TERM_URL, data=payload, headers=headers)
    cookies = response.cookies
    return cookies

def clearAuthentication(cookies) -> bool:
    return post(CLEAR_TERM_URL, cookies=cookies).json()