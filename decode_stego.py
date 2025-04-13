from PIL import Image
import numpy as np

def binary_to_text(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join([chr(int(char, 2)) for char in chars])

def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = np.array(img)

    binary_message = ""
    end_marker = "1111111111111110"

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # R, G, B
                lsb = str(pixels[i, j, k] & 1)
                binary_message += lsb

                if binary_message.endswith(end_marker):
                    # Remove the end marker before decoding
                    binary_message = binary_message[:-len(end_marker)]
                    text = binary_to_text(binary_message)
                    print("Decoded Message:")
                    print(text)
                    return text

    print("End marker not found!")
    return ""

# Example usage
decode_image("encoded.png")
