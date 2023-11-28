In short, we plan to create a program that takes in the classes the user (a Northeastern undergraduate student) wants to take in the upcoming semester and outputs an optimized schedule of these classes that maximizes the user's preferred qualities.

From the user\'s perspective, they'll run the program which will request the class codes of the classes they want to take in the upcoming semester. The program will accept a comma-delimited list as its initial input. Then the program will ask a few multiple choice, or yes/no questions about the user\'s preferences. Some examples of these questions are, "Do you prefer morning or evening classes?", "Are there any days you would prefer to not have classes?", or "How long of a break do you prefer between classes? In hours."  This information is used to determine a quality rating for a specific schedule. The course information will be used in conjunction with the user's preferences to develop an optimal schedule.

We will obtain the course information from the ~~[Northeastern Developer API](https://www.google.com/url?q=https://developerportal.northeastern.edu/course-catalog/apis/get/courses&sa=D&source=editors&ust=1697997740025939&usg=AOvVaw1ojD0Mozu1SUgt13Bkgh-M)~~ [Search NEU Reverse Engineered API](https://apidocs.searchneu.com/banner/apiSpec.html#studentregistrationssb-terms-get) or a similar API if we are unable to get an API key. Our program will make a request and parse the resulting information into an object we can operate on.

From what we know so far we can either use a simulated annealing, or a hill climbing approach. In both approaches we will take the user's preferences and create a value function that evaluates the quality of a given schedule against the user\'s preferences. The algorithm will swap courses from the catalog if they produce a schedule with better quality, making sure the required courses remain in the schedule. In the simulated annealing approach the algorithm will work until the temperature reaches 0, and in hill climbing it will take a specified number of steps, keeping track of the optimal solution over all schedules. These approaches may not find the true optimal result but will produce a "good enough" solution for our user's purposes.

We expect to encounter limitations since the search space is quite large which may cause long runtimes. In addition to that, creating a value function may be difficult since the user is specifying the parameters. Finally we may run into issues with the quality of the solutions since simulated annealing and hill climbing produces approximate solutions that may not be the optimal solution. From a user interaction standpoint it may be difficult to verify the user's inputted classes exist and are offered in a given term, and it may not be possible to provide a functional GUI in the allotted time frame, so we are considering this as a stretch goal.

We are eager to create this tool because we believe it has the potential to help many northeastern students. We foresee using it in future semesters ourselves, and plan to share it with any friends who may find it useful. We also look forward to using some classical AI concepts in a tool with real world use cases.

An interaction with the program might look like the following `>>` is program output and `<<` is user input:
```
>> Please input your desired courses:
<< CS1800, CS1802, CS2500, CS2501, ENGW1111
>> Do you prefer morning, afternoon, or evening classes or have no preference? (\[m\]orning/\[a\]fternoon/\[e\]vening/\[no\] preference)
<< Morning
>> Are there any days of the week you would like to have off? (\[mon\]day/\[tues\]day/\[wed\]nesday/\[thurs\]day/\[fri\]day)
<< Wednesday
>> Is there a minimum or maximum amount of time you would like between classes? (min \_ max \_)
<< min 0.5 max 3
>> Crunching...This may take a moment, please wait
>> Here is your schedule <SCHEDULE\> would you like to compute again? (\[Y\]es/\[N\]o)
<< N
>> Thanks, printing the CRN numbers for your courses ...
```

# Developer install

1. Ensure python 3.11 and direnv are installed on your system
2. Execute `python --version` and ensure the version is correct
3. Build a venv by running `python -m venv .venv` 
4. Install requirements by running `pip install -r requirements.txt` 
5. Run `type python` and ensure output is 
   `<cwd>/.venv/bin/python`
