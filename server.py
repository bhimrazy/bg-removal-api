from io import BytesIO

import litserve as ls
from fastapi import Response, UploadFile
from PIL import Image
from transformers import pipeline


class BackgroundRemovalAPI(ls.LitAPI):
    def setup(self, device):
        self.segmentation_model = pipeline(
            "image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True
        )

    def decode_request(self, request: UploadFile):
        # Extract image file from the request
        return Image.open(request.file)

    def predict(self, image):
        # Perform background removal on the image
        result = self.segmentation_model(image)
        return result

    def encode_response(self, image):
        # Convert the processed image to PNG format and prepare the response
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        return Response(
            content=buffer.getvalue(), headers={"Content-Type": "image/png"}
        )


# Start the server
if __name__ == "__main__":
    api = BackgroundRemovalAPI()
    server = ls.LitServer(api, timeout=False)
    server.run(port=8000)
