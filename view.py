def print_all_events(events):
    """
    Print all events from events list

    Args:
        events (list of :obj: Event): list of events
    """

    for event in events:
        print(event)


def print_main_menu():
    """
    Print menu of program
    """

    print("""
            Chose option:
            1. Book private mentoring
            2. Book checkpoint
            3. Show all my events
            4. Cancel event
            0. Exit program
          """)


def print_goodbye():
    """
    Print goodbye massage
    """

    print("Bye bye")


def get_choice():
    """
    Take option choosen by user

    Returns:
        string: menu option choosen by user
    """

    return input("Chose option: ")


def get_event_date():
    """
    Take date of event from user

    Returns
        string: date of event
    """

    return input("Enter date in format dd-mm-yyyy: ")


def preferred_mentor():
    """
    Take name of preffered mento from user

    Returns:
        string: mentor's name
    """

    return input("Enter preferred mentor: ")


def get_goal():
    """
    Take goal of private mentoring from user

    Return:
        string: goal of private mentoring session
    """

    return input("Enter your goal: ")


def print_msg(msg):
    """
    Print massage
    """

    print(msg)


def get_event_name():
    """
    Take event name from user

    Return:
        string: goal of private mentoring session
    """

    return input("Enter event name: ")
