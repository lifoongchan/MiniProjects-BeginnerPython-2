"""This program generates qr code"""

import qrcode


def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fil_color="blue", back_color="white")
    img.save("new_qr.png")


generate_qrcode(input("Enter link of your choice for the barcode: "))
