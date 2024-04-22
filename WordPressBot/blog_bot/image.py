from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, output_path):
    # Open the image
    image = Image.open(image_path)

    # Get image dimensions
    width, height = image.size

    # Choose a font and size
    font_size = 40
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text size and position to center it
    draw = ImageDraw.Draw(image)
    # Unpack width and height directly from textlength()
    text_width, text_height = draw.textlength(text, font)  # Option 2 using unpacking
    # OR:
    # width, height = draw.textlength(text, font)  # Option 1 using explicit assignment

    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Add text to the image
    draw.text((text_x, text_y), text, font=font, fill="#38e6d6")

    # Save the modified image
    image.save(output_path)

# Example usage
input_image_path = "ajathINDIA.png"
output_image_path = "ajathINDIAtext.png"
text_to_add = "Hyperledger and Smart Contracts"

add_text_to_image(input_image_path, text_to_add.upper(), output_image_path)
