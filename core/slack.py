from utils.validator import validate_arguments


def request_auth_slack(services: list, username: str, email: str) -> None:
    validate_arguments(services=services, username=username, email=email)

    print('!@#$%')
