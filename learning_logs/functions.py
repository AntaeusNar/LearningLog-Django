"""A good place to hold some funtions, like a libary?"""

# functions


def check_owner(owner, user):
    if owner != user:
        raise Http404
