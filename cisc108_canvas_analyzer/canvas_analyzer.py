"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 7


# 1) print_user_info

def print_user_info(person:str):
    '''
    prints persons name and title

    Args:
        person(str): thing information
    Returns: None
    '''
    print("Name:", person["name"])
    print("Title:", person["title"])
    print("Primary Email:", person["primary email"])
    print("Bio:", person["bio"])


# 2) filter_available_courses

def filter_available_courses(courses:[dict])->[dict]:
    '''

    Takes out courses not available to person

    Args:
        courses([dict]): list of course dictionaries
    Returns:
        [dict]: list of dictionary of available courses
    '''
    available = []
    for course in courses:
        if course["workflow_state"] == "available":
            available.append(course)
    return available


# 3) print_courses

def print_courses(courses:[dict]):
    '''
    Print the ID and name of courses

    Args:
        courses([dict]): list of course dictionaries
    Returns: None
    '''

    for course in courses:
        print("\t", course["id"], ":", course["name"])

# 4) get_course_ids

def get_course_ids(courses:[dict])->[int]:
    '''
    Takes ID from list of courses

    Args:
        courses([dict]): list of course dictionaries
    Returns:
        [int]: list of ID numbers of courses
    '''

    IDS = []
    for course in courses:
        IDS.append(course["id"])
    return IDS

# 5) choose_course

def choose_course(cids:[int])->int:
    '''
    Takes a course ID and returns if it is an available course ID

    Args:
        cids([int]): list of courses IDs
    Returns:
        int: number of courses available IDs
    '''
    message = "Choose course from list"
    pick = None
    while pick not in cids:
        pick = int(input(message))
    return pick

# 6) summarize_points

def summarize_points(summary:[dict]):
    '''
    Prints out stats for person

    Args:
        summary([dict]): list of summary dictionaries
    Returns: None
    '''
    possible = 0
    score = 0
    for sum in summary:
        if sum["score"] is not None:
            point_possible = sum["assignment"]["points_possible"]
            group_weight = sum["assignment"]["group"]["group_weight"]
            possible += points_possible * group_weight
            score += sum["score"] * group_weight
    print("Points possible:", possible)
    print("Points given:", score)
    print("Current grade:", round(100 * score / possible))

# 7) summarize_groups

def summarize_groups(summary:[dict]):
    '''
    Prints out persons grade per category

    Args:
        summary([dict]): list of summary dictionaries
    Returns None
    '''
    group_score = {}
    group_points = {}
    for sum in summary:
        if sum["score"] is not None
            group_name = sum["assignment"]["group"]["name"]
            if group_name not in group_score:
                group_score[group_name] = 0
                group_points[group_name] = 0
            group_score[group_name] += sum["score"]
            group_points[group_name] += sum["assignment"]["points_possible"]
    for name in group_score:
        score, points = group_score[name], group_points[name]
        print("*", name, ":", round(100 * score / points))


# 8) plot_scores

def plot_scores(summary:[dict]):


# 9) plot_grade_trends

def plot_grade_trends(summary:[dict]):


# Keep any function tests inside this IF statement to ensure
# that your `test_my_solution.py` does not execute it.

# 10) main

def main(personid:str):
    '''
    Gives info about persons canvas course

    Args:
        personid(str): person's ID
    Returns None
    '''
    user = canvas_requests.get_user(personid)
    print_user_info(person)
    courses = canvas_requests.get_courses(personid)
    available_courses = filter_available_courses(courses)
    print_courses(available_courses)
    cids = get_course_ids(available_courses)
    cid = choose_course(cids)
    summary = canvas_request.get_summary(personid, cid)
    summarize_points(summary)
    summarize_groups(summary)
    plot_scores(summary)
    plot_grade_trends(summary)


if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')
    
    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')