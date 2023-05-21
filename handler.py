import base64
import io

import PIL
import PIL.Image
import PIL.ImageDraw


def hello(event, context):
    print("Hello, Pillow!")
    print(PIL.__version__)
    # これはCloudWatch Logsに書き出される

    image = PIL.Image.new("RGB", (100, 100))
    draw = PIL.ImageDraw.Draw(image)

    draw.rectangle((20, 20, 80, 80))  # 質素な四角形を作成

    # バイナリイメージを作成
    output = io.BytesIO()
    image.save(output, format="JPEG")
    responseBody = output.getvalue()

    # BASE64エンコード
    responseBody = base64.b64encode(responseBody).decode("utf-8")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/jpeg",
        },
        "body": responseBody,
        "isBase64Encoded": True,
    }
