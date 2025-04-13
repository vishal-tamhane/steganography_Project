from PIL import Image
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image_path, secret_message, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode
    pixels = np.array(img)
    
    binary_message = text_to_binary(secret_message) + '1111111111111110'  # End marker
    binary_index = 0
    total_pixels = pixels.shape[0] * pixels.shape[1] * 3  # RGB channels
    
    if len(binary_message) > total_pixels:
        raise ValueError("Message too large to hide in this image.")

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # Iterate over R, G, B
                if binary_index < len(binary_message):
                    pixels[i, j, k] = (pixels[i, j, k] & 0xFE) | int(binary_message[binary_index])
                    binary_index += 1

    encoded_img = Image.fromarray(pixels)
    encoded_img.save(output_path)
    print(f"Message encoded and saved as {output_path}")

# Example Usage
encode_image("input.jpg", "Hello, this is a secret!", "encoded.png")
