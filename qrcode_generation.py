import qrcode
import base64
import io


class QRCodeClass:
    '''
    QRCodeClass generates a qr code for your link oy any text data.
    '''

    def __init__(self, link) -> None:
        self.link = link

    def create_qr_code(self) -> str:
        try:
            qr = qrcode.QRCode(version=1,
                               error_correction=qrcode.constants.ERROR_CORRECT_H,
                               box_size=10,
                               border=4)
            qr.add_data(self.link)
            qr.make(fit=True)
            img = qr.make_image()

            # converting image in base 64
            buffer = io.BytesIO()
            img.save(buffer)
            image_bytes = buffer.getvalue()

            # Convert the bytes to a base64 string
            img_base64 = base64.b64encode(image_bytes).decode('utf-8')

            return img_base64
        except Exception as e:
            print(f"An error occurred while generating the QR code: {e}")
            return "Unable to Generate QR Code."


