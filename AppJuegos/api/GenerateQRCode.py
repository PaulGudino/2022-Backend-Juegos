import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)

qr.clear()
qr.add_data('{"client_id" : "1", "ticket_id" : "1", "invoice_number": "1"}')

qr.make(fit=True)

img = qr.make_image(fill_color = "#eb65ef", back_color = "#f7f7fa")
img.save('qrcode.png')