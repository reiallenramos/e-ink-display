#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Flash bitmap to Waveshare 2.13" e-ink display
Simple script to display output.bmp on the e-ink screen

Requirements:
- epd2in13.py (Waveshare driver)
- epdconfig.py (Waveshare config)
Both files should be in the same folder as this script.
"""

import os
import logging
import time
from PIL import Image
import epd2in13_V4

logging.basicConfig(level=logging.INFO)

def flash_image():
    """
    Flash output.bmp to the e-ink display
    """
    try:
        image_path = "output.bmp"
        
        # Check if image exists
        if not os.path.exists(image_path):
            logging.error(f"Image file not found: {image_path}")
            logging.error("Please run text_to_bitmap.py first to create output.bmp")
            return False
        
        logging.info(f"Flashing {image_path} to e-ink display...")
        
        # Initialize display
        epd = epd2in13_V4.EPD()
        logging.info("Initializing display...")
        epd.init()
        epd.Clear(0xFF)
        
        # Load and display image
        logging.info("Loading image...")
        epd.init()
        image = Image.new('1', (epd.height, epd.width), 255) # 255: clear the frame
        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_dir, image_path)
        logging.info(image_path)
        image = Image.open(image_path)

        # Convert to 1-bit if needed
        # if image.mode != '1':
        #     logging.info("Converting image to 1-bit mode...")
        #     image = image.convert('1')
        
        # Display the image
        logging.info("Displaying image on e-ink screen...")
        epd.display(epd.getbuffer(image))
        
        logging.info("Image displayed successfully!")
        
        # Put display to sleep to save power
        logging.info("Putting display to sleep...")
        time.sleep(1)
        
        return True
        
    except IOError as e:
        logging.error(f"IO Error: {e}")
        return False
        
    except KeyboardInterrupt:
        logging.info("Interrupted by user")
        epd2in13.epdconfig.module_exit(cleanup=True)
        return False
        
    except Exception as e:
        logging.error(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # Flash the image
    success = flash_image()
    
    if success:
        print("\n✓ Image successfully displayed on e-ink screen!")
    else:
        print("\n✗ Failed to display image")
        exit(1)