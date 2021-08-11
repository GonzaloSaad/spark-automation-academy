"""
G10: Vertical Separation

Variables and function should be defined close to where they are used.
Local variables should be declared just above their first usage and should have a small vertical scope.

We don’t want local variables declared hundreds of lines distant from their usages.

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/general/g10-vertical-separation.html

"""
from unittest.mock import Mock


def example():
    employee = _get_employee()
    cars = _fetch_cars_from_other_service(employee.id)

    if employee.active:
        _do_some_stuff_here(employee)
    else:
        _do_some_stuff_there(employee)

    db_client = _get_db_client()
    insurance_api = _get_insurance_api()
    profile = db_client.get_profile(employee.id)
    for picture in profile.pictures:
        _publish_picture(picture)

    # ------------ The function continues ----------------
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # ------------ The function continues ----------------
    if cars:
        insurance_api.update_cars(cars)


def _publish_picture(_):
    # Placebo function for this example.
    pass


def _do_some_stuff_there(_):
    # Placebo function for this example.
    pass


def _do_some_stuff_here(_):
    # Placebo function for this example.
    pass


def _get_employee():
    # Placebo function for this example.
    return Mock()


def _fetch_cars_from_other_service(_):
    # Placebo function for this example.
    return Mock()


def _get_insurance_api():
    # Placebo function for this example.
    return Mock()


def _get_db_client():
    # Placebo function for this example.
    return Mock()
