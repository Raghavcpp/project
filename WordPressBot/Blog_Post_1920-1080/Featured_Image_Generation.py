from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def deleteimage():
  if os.path.exists("ajathINDIAtext.png"):
    os.remove("ajathINDIAtext.png")
  else:
    print("The file does not exist")

def transform_list(input_list):
    length = len(input_list)
    if length % 2 == 0:
        result = [(x - length/2 + 0.5) for x in range(length)]
    else:
        result = [(x - length//2) for x in range(length)]
    return result[::-1]

def add_text_to_image(input_image_path,
                      text_to_add,
                      output_image_path,
                      font_names,
                      font_size,
                      text_color,
                      boldness,
                      wordwrap):
    try:
        font_name = os.path.join("C:\\Windows\\Fonts", font_names)
        img = Image.open(input_image_path)
        w, h = img.size
        draw = ImageDraw.Draw(img)

        para = [li for part in text_to_add.split(':') for li in textwrap.wrap(part.strip(), width=wordwrap)]
        linepos= transform_list(para)
        # print(para)
        # print(len(para))
        # print(len(max(para, key=len)))
        font = ImageFont.truetype(font_name, font_size)

        for i in range(len(para)):
          left, top, right, bottom = font.getbbox(para[i])
          text_width = right - left
          text_height = bottom - top
          # print(text_width," --- ", text_height)
          # print(w," --- ",h)

          x = (w - text_width)/2
          y = ((h-100)/2 - ((text_height + 10) * linepos[i]))

          draw.text((x, y), para[i], font=font, stroke_width=boldness,fill=text_color)

        output_folder = "output"
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, output_image_path)

        img.save(output_path)

        print(f"Text added to image and saved as: {output_image_path}")

    except FileNotFoundError as e:
        print(f"Error: Input image file not found: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")