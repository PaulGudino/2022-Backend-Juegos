import qrcode
from pathlib import Path
from PIL import Image

def generateCode(client_id, ticket_id, invoice_number):
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
    )

    qr.clear()
    data = f'"client_id": "{client_id}" , "ticket_id": "{ticket_id}" , "invoice_number": "{invoice_number}"'
    qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill_color = "#eb65ef", back_color = "#f7f7fa")

    cwd = Path.cwd()
    joined_path = cwd / "media"

    if (Path(joined_path).exists()):
        joined_path = cwd / "media" / f'{client_id}-{ticket_id}.png'
        img.save(joined_path)
    
    else:
        Path(joined_path).mkdir(exist_ok=False)
        joined_path = cwd / "media" / f'{client_id}-{ticket_id}.png'
        img.save(joined_path)
        

