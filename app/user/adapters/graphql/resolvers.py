from django.contrib.auth import get_user_model

def resolve_whoami(info):
    """
    This function returns the currently authenticated user.

    Args:
        info (str): The GraphQL query

    Returns:
        User: The currently authenticated user

    Raises:
        Exception: If the user is not authenticated
    """
    user = info.context.user

    # Check if user is authenticated
    if user.is_anonymous:
        raise Exception("Authentication Failure: Your must be signed in")
    return user

def resolve_users(info):
    """
    This function returns all the users in the system.

    Args:
        info (str): The GraphQL query

    Returns:
        [User]: A list of all the users in the system

    Raises:
        Exception: If the user is not authenticated
    """
    user = info.context.user

    # Check if user is authenticated
    if user.is_anonymous:
        raise Exception("Authentication Failure: Your must be signed in")
    return get_user_model().objects.all()