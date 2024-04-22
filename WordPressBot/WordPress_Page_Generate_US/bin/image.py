from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_image_path, text_to_add, output_image_path, font_name, font_size=100, text_color="#71F242", text_position="center"):
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
        font = ImageFont.truetype(font_name, font_size)
        # Get text dimensions
        left, top, right, bottom = font.getbbox(text_to_add)
        text_width = right - left
        text_height = bottom - top
        # Calculate text position coordinates based on position parameter
        print(text_width," --- ", text_height)
        print(width," --- ",height)

        x = (width - text_width)/2
        y = (height/2 - text_height)
        
        # Create a Draw object
        draw = ImageDraw.Draw(img)

        # Draw the text with specified color and position
        draw.text((x, y), text_to_add, font=font, stroke_width=3,fill=text_color)

        # Save the output image
        img.save(output_image_path)

        print(f"Text added to image and saved as: {output_image_path}")

    except FileNotFoundError as e:
        print(f"Error: Input image file not found: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

# Example usage
add_text_to_image(input_image_path="ajathAr.png",
                  text_to_add="Hyperledger and Smart Contracts",
                  output_image_path="ajathINDIAtext.png",
                  font_name="C:\\arial.ttf",
                  font_size=100,
                  text_color="#71F242",
                  text_position="topleft")

# Error: An unexpected error occurred: cannot open resource
