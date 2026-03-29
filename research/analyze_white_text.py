#!/usr/bin/env python3
"""
Analyze lines and columns overflown by white text in the memorial image
The white text (birth/death dates) appears as high-brightness pixels
"""

from PIL import Image
import numpy as np

IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"

def analyze_white_text_regions():
    """Identify and analyze regions with white text"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = np.array(img)
    
    print("="*70)
    print("WHITE TEXT REGION ANALYSIS")
    print("="*70)
    print(f"Image dimensions: {width}x{height}")
    
    # White text appears as high brightness pixels (close to 255)
    # Find rows and columns with high brightness values
    
    # Threshold for "white" - text is typically 200-255 in grayscale
    white_threshold = 200
    
    # Find rows (lines) that contain white pixels
    white_rows = []
    for row in range(height):
        row_pixels = pixels[row, :]
        white_count = np.sum(row_pixels > white_threshold)
        if white_count > 10:  # At least 10 white pixels to be text
            white_rows.append((row, white_count))
    
    print(f"\nRows with white pixels (>200, >10 pixels):")
    print(f"Found {len(white_rows)} rows")
    
    # Group consecutive rows into text regions
    text_regions = []
    current_region = []
    for row, count in white_rows:
        if not current_region or row == current_region[-1][0] + 1:
            current_region.append((row, count))
        else:
            if len(current_region) > 0:
                text_regions.append(current_region)
            current_region = [(row, count)]
    if current_region:
        text_regions.append(current_region)
    
    print(f"\nGrouped into {len(text_regions)} text regions:")
    for i, region in enumerate(text_regions):
        start_row = region[0][0]
        end_row = region[-1][0]
        print(f"  Region {i+1}: Rows {start_row}-{end_row} ({len(region)} lines)")
        
        # Analyze this region's pixels
        region_pixels = pixels[start_row:end_row+1, :]
        print(f"    Brightness range: {region_pixels.min()}-{region_pixels.max()}")
        print(f"    Mean brightness: {region_pixels.mean():.2f}")
        print(f"    White pixels (>200): {np.sum(region_pixels > 200)}")

def extract_text_line_data():
    """Extract pixel data from lines containing white text"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = np.array(img)
    
    print("\n" + "="*70)
    print("TEXT LINE PIXEL DATA EXTRACTION")
    print("="*70)
    
    white_threshold = 200
    
    # Find all rows with significant white pixels
    text_rows = []
    for row in range(height):
        row_data = pixels[row, :]
        white_pixels = row_data[row_data > white_threshold]
        if len(white_pixels) > 20:  # Significant text line
            text_rows.append(row)
    
    print(f"Found {len(text_rows)} text-heavy rows")
    
    # Extract ASCII from these specific rows
    print("\nAnalyzing white text rows for patterns:")
    
    for idx, row in enumerate(text_rows[:20]):  # First 20 text rows
        row_data = pixels[row, :]
        
        # Get positions of white pixels
        white_positions = np.where(row_data > white_threshold)[0]
        
        if len(white_positions) > 0:
            # Check if positions map to ASCII
            ascii_chars = []
            for pos in white_positions:
                if 32 <= pos <= 126:
                    ascii_chars.append(chr(pos))
            
            # Check pixel values as ASCII
            pixel_ascii = []
            for val in row_data[row_data > white_threshold]:
                if 32 <= val <= 126:
                    pixel_ascii.append(chr(int(val)))
            
            if ascii_chars or pixel_ascii:
                print(f"\nRow {row}:")
                print(f"  White pixel positions (ASCII): {''.join(ascii_chars[:30])}")
                print(f"  White pixel values (ASCII): {''.join(pixel_ascii[:30])}")

def analyze_text_columns():
    """Analyze columns that contain white text pixels"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = np.array(img)
    
    print("\n" + "="*70)
    print("TEXT COLUMN ANALYSIS")
    print("="*70)
    
    white_threshold = 200
    
    # Find columns with white pixels
    text_columns = []
    for col in range(width):
        col_data = pixels[:, col]
        white_count = np.sum(col_data > white_threshold)
        if white_count > 5:  # Some white pixels in this column
            text_columns.append((col, white_count))
    
    print(f"Found {len(text_columns)} columns with white pixels")
    
    # Group into regions
    col_regions = []
    current = []
    for col, count in text_columns:
        if not current or col == current[-1][0] + 1:
            current.append((col, count))
        else:
            if len(current) > 0:
                col_regions.append(current)
            current = [(col, count)]
    if current:
        col_regions.append(current)
    
    print(f"Grouped into {len(col_regions)} column regions:")
    for i, region in enumerate(col_regions[:10]):  # Show first 10
        start = region[0][0]
        end = region[-1][0]
        print(f"  Region {i+1}: Columns {start}-{end}")

def extract_text_coordinates():
    """Extract coordinates where white text appears and check for encoding"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = np.array(img)
    
    print("\n" + "="*70)
    print("WHITE TEXT COORDINATE ENCODING")
    print("="*70)
    
    white_threshold = 200
    
    # Get all coordinates of white pixels
    white_coords = []
    for row in range(height):
        for col in range(width):
            if pixels[row, col] > white_threshold:
                white_coords.append((col, row))  # (x, y)
    
    print(f"Total white pixels: {len(white_coords)}")
    
    # Check if X coordinates (columns) encode ASCII
    x_coords = [x for x, y in white_coords]
    x_ascii = [chr(x) for x in x_coords if 32 <= x <= 126]
    
    # Check if Y coordinates (rows) encode ASCII  
    y_coords = [y for x, y in white_coords]
    y_ascii = [chr(y) for y in y_coords if 32 <= y <= 126]
    
    print(f"\nX coordinates as ASCII ({len(x_ascii)} chars):")
    print(''.join(x_ascii[:100]))
    
    print(f"\nY coordinates as ASCII ({len(y_ascii)} chars):")
    print(''.join(y_ascii[:100]))
    
    # Try combinations
    print("\n\nCombined X,Y as message:")
    combined = []
    for x, y in white_coords[:200]:
        if 32 <= x <= 126:
            combined.append(chr(x))
        if 32 <= y <= 126:
            combined.append(chr(y))
    print(''.join(combined[:100]))

def analyze_text_specific_values():
    """Analyze specific pixel values in white text regions"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = np.array(img)
    
    print("\n" + "="*70)
    print("WHITE TEXT PIXEL VALUE ANALYSIS")
    print("="*70)
    
    white_threshold = 200
    
    # Collect all white pixel values
    white_values = []
    for row in range(height):
        row_data = pixels[row, :]
        white_vals = row_data[row_data > white_threshold]
        white_values.extend(white_vals.tolist())
    
    print(f"Total white pixel values collected: {len(white_values)}")
    
    # Check for specific values
    unique_values = sorted(set(white_values))
    print(f"\nUnique white pixel values ({len(unique_values)}):")
    print(unique_values[:50])  # First 50
    
    # Check if any map to our target numbers
    target_nums = [5, 24, 55, 60, 120, 25, 52]
    print(f"\nChecking for target values {target_nums}:")
    for target in target_nums:
        count = white_values.count(target)
        if count > 0:
            print(f"  Value {target}: {count} occurrences")
    
    # Check ASCII mapping of white values
    ascii_from_values = [chr(int(v)) for v in white_values if 32 <= v <= 126]
    print(f"\nWhite values as ASCII ({len(ascii_from_values)} chars):")
    print(''.join(ascii_from_values[:100]))

if __name__ == "__main__":
    analyze_white_text_regions()
    extract_text_line_data()
    analyze_text_columns()
    extract_text_coordinates()
    analyze_text_specific_values()
