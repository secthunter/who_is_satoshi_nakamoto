#!/usr/bin/env python3
"""
Deep coordinate analysis - check if pixel positions encode ASCII data
"""

from PIL import Image

IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"

def analyze_coordinate_ascii():
    """Analyze if X,Y coordinates of specific pixel values map to ASCII"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("="*70)
    print("COORDINATE TO ASCII MAPPING ANALYSIS")
    print("="*70)
    
    # Target values that might encode data
    target_values = [5, 24, 55, 60, 120]
    
    for target in target_values:
        positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == target]
        print(f"\nPixel value {target} ({len(positions)} occurrences):")
        
        # Collect X and Y coordinates that fall in ASCII range
        x_ascii = []
        y_ascii = []
        
        for x, y in positions:
            if 32 <= x <= 126:
                x_ascii.append(chr(x))
            if 32 <= y <= 126:
                y_ascii.append(chr(y))
        
        if x_ascii:
            print(f"  X coords as ASCII: {''.join(x_ascii[:50])}")
        if y_ascii:
            print(f"  Y coords as ASCII: {''.join(y_ascii[:50])}")

def analyze_pixel_5_in_detail():
    """Deep dive on pixel value 5 (the key number)"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("PIXEL VALUE 5 ANALYSIS (The 'Key' Number)")
    print("="*70)
    
    positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == 5]
    print(f"Found {len(positions)} pixels with value 5")
    
    print("\nAll positions (x, y) with ASCII mappings:")
    for i, (x, y) in enumerate(positions):
        x_char = chr(x) if 32 <= x <= 126 else f"({x})"
        y_char = chr(y) if 32 <= y <= 126 else f"({y})"
        print(f"  {i:3d}: ({x:3d}, {y:3d}) -> X={x_char}, Y={y_char}")

def check_row_column_sums():
    """Check if row/column sums encode data"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("ROW/COLUMN SUM ANALYSIS")
    print("="*70)
    
    # Row sums
    row_sums = []
    for row in range(height):
        row_start = row * width
        row_pixels = pixels[row_start:row_start + width]
        row_sums.append(sum(row_pixels))
    
    # Check if row sums mod 256 give ASCII
    print("\nRow sums mod 256 as ASCII (first 50):")
    ascii_chars = []
    for i, s in enumerate(row_sums[:50]):
        val = s % 256
        if 32 <= val <= 126:
            ascii_chars.append(chr(val))
        else:
            ascii_chars.append('.')
    print(''.join(ascii_chars))

def analyze_specific_regions():
    """Analyze specific regions of the image"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    
    print("\n" + "="*70)
    print("REGION ANALYSIS")
    print("="*70)
    
    # The image is 700x1000
    # Check corners and edges
    regions = [
        ("Top-left 50x50", 0, 0, 50, 50),
        ("Top-right 50x50", 650, 0, 700, 50),
        ("Bottom-left 50x50", 0, 950, 50, 1000),
        ("Bottom-right 50x50", 650, 950, 700, 1000),
        ("Center 100x100", 300, 450, 400, 550),
    ]
    
    for name, x1, y1, x2, y2 in regions:
        region = img.crop((x1, y1, x2, y2))
        pixels = list(region.getdata())
        unique = set(pixels)
        print(f"\n{name}:")
        print(f"  Unique pixel values: {len(unique)}")
        print(f"  Range: {min(pixels)} - {max(pixels)}")

if __name__ == "__main__":
    analyze_coordinate_ascii()
    analyze_pixel_5_in_detail()
    check_row_column_sums()
    analyze_specific_regions()
