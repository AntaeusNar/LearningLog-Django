"""A good place to hold some funtions, like a libary?"""

from django.http import Http404
# functions


def check_owner(owner, user):
    if owner != user:
        raise Http404
