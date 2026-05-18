# Read the image data from a local file
import base64
from openai import OpenAI

# Add your real API key
client = OpenAI(api_key="YOUR_REAL_API_KEY")

# Generate image
img_results = client.images.generate(
    model="gpt-image-1",
    prompt="A robot eating a cheeseburger.",
    size="1024x1024"
)

# Save image
image_data = base64.b64decode(img_results.data[0].b64_json)

with open("image.png", "wb") as image_file:
    image_file.write(image_data)

print("Image saved successfully!")
