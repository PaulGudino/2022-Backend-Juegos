# sudo dnf install zbar-libs
# sudo apt-get install libzbar0

from pyzbar import pyzbar
from pathlib import Path
from PIL import Image

def readCode(fileName):

    cwd = Path.cwd()
    joined_path = cwd / "media"

    if (Path(joined_path).exists()):
        joined_path = joined_path / fileName
        if (Path(joined_path).exists()):
            image = Image.open(joined_path)
            qr_code = pyzbar.decode(image)[0]
            data = qr_code.data.decode('utf8').encode('shift-jis').decode('utf-8')
            print("The data is: ", data)
        else:
            print("File not found")
    else:
        print("media folder not found")

