from PIL import Image


def image_sized():

    image = Image.open(input("\nEnter the name of image file: "))

    # print the current size of image
    print(f"\nCurrent size : {image.size}\n")

    # specify the size we're changing to
    request_height = int(input("Resized height: "))
    request_weight = int(input("Resized weight: "))
    file_name = input("\nKey in new image name: ")
    resized_image = image.resize((request_weight, request_height))
    resized_image.save(file_name)


while True:
    command = input("\nStart resizing image (Y/N): ")

    if command.upper() == "Y":
        image_sized()

    elif command.upper() == "N":
        print("Thank you for using this program. See you!")
        break

    else:
        print("Please check and re-enter your command again.")
