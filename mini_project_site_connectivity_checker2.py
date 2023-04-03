import requests


status_code_dict = {

    200: """Everything went okay, and the server returned a result (if any).""",

    301: """The server is redirecting you to a different endpoint. \
    This can happen when a company switches domain names, or when an endpoint's name has changed.""",

    401: """The server thinks you're not authenticated. \
    This happens when you don't send the right credentials to access an API.""",

    400: """The server thinks you made a bad request. \
    This can happen when you don't send the information that the API requires to process \
    your request (among other things).""",

    403: """The resource you're trying to access is forbidden, and you don't have the right permissions to see it.""",

    404: """The server didn't find the resource you tried to access."""

}


def main():
    response = requests.get(input("Enter an url: "))
    status_code = response.status_code
    print(f"\nThe status code is {status_code}")
    print(status_code_dict[status_code])


while True:
    command = input("\nCheck a site connectivity(yes/no): ")

    if command.lower() == "yes":
        main()

    elif command.lower() == "no":
        print("\nThe program is terminated.")
        quit()

    else:
        print("\nWe couldn't recognise your command. Please key in again.")
