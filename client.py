import argparse
import requests

# Update this URL to your server's URL if hosted remotely
API_URL = "http://127.0.0.1:8000/predict"


def send_image_for_processing(input_image_path: str, output_image_path: str):
    """Send an image to the server for background removal and save the processed image."""

    # Open and read the input image file
    with open(input_image_path, "rb") as input_file:
        image_data = input_file.read()

    # Send the image to the server
    response = requests.post(API_URL, files={"content": image_data})

    # Check if the request was successful
    if response.status_code == 200:
        # Save the processed image
        with open(output_image_path, "wb") as output_file:
            output_file.write(response.content)

        print(f"Processed image saved to {output_image_path}")
    else:
        print(f"Error: Received status code {response.status_code} - {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send an image to the server for background removal and receive the processed image."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to the input image")
    parser.add_argument(
        "-o",
        "--output",
        help="Path to save the output image",
        default="output.jpg",
    )
    args = parser.parse_args()

    send_image_for_processing(args.input, args.output)
