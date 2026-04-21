"""
@author: Viet Nguyen <nhviet1009@gmail.com>
Optimized version with finer detail and better contrast
"""
import argparse

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps
from utils import get_data


def get_args():
    parser = argparse.ArgumentParser("Image to ASCII")
    parser.add_argument("--input", type=str, default="data/input.jpg", help="Path to input image")
    parser.add_argument("--output", type=str, default="data/output.jpg", help="Path to output text file")
    parser.add_argument("--language", type=str, default="english")
    parser.add_argument("--mode", type=str, default="standard")
    parser.add_argument("--background", type=str, default="black", choices=["black", "white"],
                        help="background's color")
    parser.add_argument("--num_cols", type=int, default=400, help="number of character for output's width")
    parser.add_argument("--contrast", type=float, default=2.0,
                        help="Contrast enhancement factor (1.0-3.0)")
    parser.add_argument("--scale", type=int, default=1,
                        help="Character scale (1=smaller chars, 2=larger)")
    args = parser.parse_args()
    return args


def main(opt):
    if opt.background == "white":
        bg_code = 255
    else:
        bg_code = 0

    char_list, font, sample_character, _ = get_data(opt.language, opt.mode)
    num_chars = len(char_list)

    # Use higher num_cols for finer detail (character width ~6-8 pixels at scale=1)
    num_cols = opt.num_cols
    scale = opt.scale

    image = cv2.imread(opt.input)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply contrast enhancement
    if opt.contrast != 1.0:
        f = image.astype(np.float32) * opt.contrast
        f = np.clip(f, 0, 255)
        image = f.astype(np.uint8)

    # Apply CLAHE for better local contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3, 3))
    image = clahe.apply(image)

    height, width = image.shape
    cell_width = width / num_cols
    cell_height = scale * cell_width
    num_rows = int(height / cell_height)

    if num_cols > width or num_rows > height:
        print("Too many columns or rows. Use default setting")
        cell_width = 6
        cell_height = 12
        num_cols = int(width / cell_width)
        num_rows = int(height / cell_height)

    bbox = font.getbbox(sample_character)
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]

    # Scale char size for output
    out_char_width = max(1, char_width)
    out_char_height = max(1, char_height * scale)

    out_width = out_char_width * num_cols
    out_height = out_char_height * num_rows

    out_image = Image.new("L", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)

    # Get font for scaled text
    try:
        scaled_font_size = max(8, int(12 * scale))
        scaled_font = font.font.font_variant(size=scaled_font_size)
    except:
        scaled_font = font

    for i in range(num_rows):
        line_chars = []
        for j in range(num_cols):
            y1 = int(i * cell_height)
            y2 = min(int((i + 1) * cell_height), height)
            x1 = int(j * cell_width)
            x2 = min(int((j + 1) * cell_width), width)

            region = image[y1:y2, x1:x2]
            if region.size > 0:
                brightness = np.mean(region)
            else:
                brightness = 128

            char_index = min(int(brightness / 255 * num_chars), num_chars - 1)
            line_chars.append(char_list[char_index])

        line = ''.join(line_chars)
        draw.text((0, i * out_char_height), line, fill=255 - bg_code, font=scaled_font)

    if opt.background == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    else:
        cropped_image = out_image.getbbox()

    if cropped_image:
        out_image = out_image.crop(cropped_image)

    out_image.save(opt.output)
    print(f"Output saved: {opt.output}")


if __name__ == '__main__':
    opt = get_args()
    main(opt)
