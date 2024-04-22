
from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, text_to_add, output_image_path, font_name="./arial.ttf", font_size=32, text_color=(255, 255, 255), text_position="center"):
    """Adds text to the center of the given image.

    Args:
        input_image_path (str): Path to the input image.
        text_to_add (str): The text to add to the image.
        output_image_path (str): Path to the output image.
        font_name (str): Name of the font to use (default: "arial.ttf").
        font_size (int): Size of the font (default: 30).
        text_color (tuple): RGB color of the text (default: white, (255, 255, 255)).
        text_position (str): Position of the text. Allowed values: "center", "top", "bottom", "left", "right", "topleft", "topright", "bottomleft", "bottomright". Default: "center".
    """

    try:
        # Open the input image
        img = Image.open(input_image_path)

        # Get image dimensions
        width, height = img.size

        # Load the font
        font = ImageFont.truetype('arial.ttf', font_size)
        # Get text dimensions
        left, top, right, bottom = font.getbbox(text_to_add)
        text_width = right - left
        text_height = bottom - top
        # Calculate text position coordinates based on position parameter
        if text_position == "center":
            x = (width - text_width) / 2
            y = (height - text_height) / 2
        elif text_position == "top":
            x = (width - text_width) / 2
            y = 0
        elif text_position == "bottom":
            x = (width - text_width) / 2
            y = height - text_height
        elif text_position == "left":
            x = 0
            y = (height - text_height) // 2
        elif text_position == "right":
            x = width - text_width
            y = (height - text_height) // 2
        elif text_position == "topleft":
            x = 0
            y = 0
        elif text_position == "topright":
            x = width - text_width
            y = 0
        elif text_position == "bottomleft":
            x = 0
            y = height - text_height
        elif text_position == "bottomright":
            x = width - text_width
            y = height - text_height
        else:
            raise ValueError(f"Invalid text_position: {text_position}")

        # Create a Draw object
        draw = ImageDraw.Draw(img)

        # Draw the text with specified color and position
        draw.text((x, y), text_to_add, font=font, fill=text_color)

        # Save the output image
        img.save(output_image_path)

        print(f"Text added to image and saved as: {output_image_path}")

    except FileNotFoundError as e:
        print(f"Error: Input image file not found: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

# Example usage
add_text_to_image(input_image_path="ajathINDIA.png",
                  text_to_add="Hyperledger and Smart Contracts",
                  output_image_path="ajathINDIAtext.png",
                  font_name="./arial.ttf",
                  font_size=100,
                  text_color=(0, 255, 0),
                  text_position="topleft")
