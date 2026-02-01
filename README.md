# Text to Bitmap Converter for E-ink Displays

A simple Python toolkit to convert text into 250×122 1-bit bitmap images and flash them to Waveshare 2.13" e-ink displays.

## Features

- **text_to_bitmap.py**: Generate 1-bit (black and white) BMP images
- **flash_to_display.py**: Flash bitmap to Waveshare e-ink display
- Fixed 250×122 pixel dimensions (Waveshare 2.13" standard)
- Centered text layout
- Simple command-line interface

## Requirements

```bash
pip install Pillow
```

## Installation

### On Raspberry Pi

**What you need:**
The Waveshare library provides the Python driver code that communicates with the e-ink display hardware.

**Simple 3-step install:**

1. **Download these 2 files from Waveshare GitHub and put them in your project folder:**
   - `epd2in13_V4.py` - [Download here](https://raw.githubusercontent.com/waveshare/e-Paper/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in13_V4.py)
   - `epdconfig.py` - [Download here](https://raw.githubusercontent.com/waveshare/e-Paper/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epdconfig.py)

   Note: After downloading, edit `epd2in13_V4.py` and change the import statement from `from . import epdconfig` to `import epdconfig`.

2. **Install Python dependencies:**
   ```bash
   sudo pip3 install RPi.GPIO spidev Pillow
   ```

3. **Enable SPI interface:**
   ```bash
   sudo raspi-config
   # Navigate to: Interfacing Options -> SPI -> Yes
   sudo reboot
   ```

**Your folder should look like:**
```
your-project/
├── epd2in13_V4.py       (from Waveshare)
├── epdconfig.py         (from Waveshare)
├── text_to_bitmap.py    (our script)
├── flash_to_display.py  (our script)
└── output.bmp           (generated)
```

## Usage

### Step 1: Create Bitmap

```bash
python3 text_to_bitmap.py "Your text here"
```

This creates `output.bmp` in the current directory.

### Step 2: Flash to Display (on Raspberry Pi only)

```bash
# Flash the bitmap to the display
python3 flash_to_display.py
```

**Complete workflow:**
```bash
# Create the bitmap
python3 text_to_bitmap.py "Temperature: 23°C"

# Flash to display
python3 flash_to_display.py
```

## Examples

```bash
# Simple message
python3 text_to_bitmap.py "Hello E-ink!"

# Status message
python3 text_to_bitmap.py "Temperature: 23°C"

# Multi-word text
python3 text_to_bitmap.py "Battery Low - Charge Now"
```

## Output

- **Format**: 1-bit BMP (black and white)
- **Dimensions**: 250 × 122 pixels
- **Colors**: White background, black text
- **Compatibility**: Ready for Waveshare e-ink displays

## Notes

- **text_to_bitmap.py** creates the bitmap images (always saves as `output.bmp`)
- **flash_to_display.py** displays them on the Waveshare e-ink screen
- The font is DejaVu Sans at size 16 (falls back to system default if unavailable)
- Text is automatically centered in the image
- Very long text may be cut off at the edges

## Troubleshooting

**Permission errors**: Run with sudo if needed:
```bash
sudo python3 flash_to_display.py
```

**Import errors**: Make sure `epd2in13_V4.py` and `epdconfig.py` are in the same folder as `flash_to_display.py`

**SPI not enabled**: Run `sudo raspi-config` and enable SPI under Interfacing Options

## Acknowledgements

This project was built with assistance from [Claude](https://claude.ai) (Sonnet 4.5) by Anthropic.

## License

Free to use and modify.