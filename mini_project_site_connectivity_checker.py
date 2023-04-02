import urllib.request as urllib


print("\nThis is a site connectivity checker program")


def main(url):
    print("checking connectivity...")
    response = urllib.urlopen(url)
    response_code = response.getcode()
    print(f"Connected {url} successfully. \nThe response code was {response_code}")


while True:
    command = input("\nCheck a site connectivity(yes/no): ")

    if command.lower() == "yes":
        input_url = input("\nEnter your url: ")
        main(input_url)

    elif command.lower() == "no":
        print("\nThe program is terminated.")
        quit()

    else:
        print("\nWe couldn't recognise your command. Please key in again.")
