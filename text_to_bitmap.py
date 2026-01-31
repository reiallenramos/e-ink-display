#!/usr/bin/env python3
"""
Simple text to bitmap converter for e-ink displays (250x122)
Generates a 1-bit BMP image suitable for Waveshare e-ink screens
"""

from PIL import Image, ImageDraw, ImageFont

def text_to_bitmap(text):
    """
    Convert text to a 250x122 1-bit bitmap image
    
    Args:
        text: String to render
    """
    # E-ink display dimensions
    WIDTH = 250
    HEIGHT = 122
    FONT_SIZE = 16
    
    # Create white background image (1-bit mode)
    image = Image.new('1', (WIDTH, HEIGHT), 1)
    draw = ImageDraw.Draw(image)
    
    # Try to use a basic font (falls back to default if not available)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position (centered)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (WIDTH - text_width) // 2
    y = (HEIGHT - text_height) // 2
    
    # Draw black text on white background
    draw.text((x, y), text, fill=0, font=font)
    
    # Save as BMP
    image.save("output.bmp", "BMP")
    print(f"Bitmap saved to: output.bmp")
    print(f"Size: {WIDTH}x{HEIGHT}, Mode: 1-bit")


if __name__ == "__main__":
    import sys
    
    # Get text from command line or use default
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = "Hello E-ink!"
    
    # Generate bitmap
    text_to_bitmap(text)