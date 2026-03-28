#!/usr/bin/env python3
"""
Advanced pixel pattern analysis - row/column patterns and bit encoding
"""

from PIL import Image

IMAGE_PATH = "research/01_assets/images/haian_mit_text_skaliert_rand.jpeg"

def analyze_row_patterns():
    """Analyze each row for patterns"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    
    print("="*60)
    print("ROW-BY-ROW ANALYSIS")
    print("="*60)
    
    # Get pixel data
    pixels = list(img.getdata())
    
    # Analyze each row
    dark_counts = []
    for row in range(height):
        row_start = row * width
        row_pixels = pixels[row_start:row_start + width]
        dark = sum(1 for p in row_pixels if p < 128)
        dark_counts.append(dark)
    
    # Find rows with unusual dark counts
    avg_dark = sum(dark_counts) / len(dark_counts)
    print(f"Average dark pixels per row: {avg_dark:.2f}")
    
    # Look for rows that deviate significantly
    unusual_rows = []
    for i, count in enumerate(dark_counts):
        deviation = abs(count - avg_dark)
        if deviation > 100:  # Threshold for unusual
            unusual_rows.append((i, count, deviation))
    
    print(f"\nUnusual rows (>{avg_dark+100:.0f} or <{avg_dark-100:.0f} dark pixels):")
    for row, count, dev in unusual_rows[:20]:
        print(f"  Row {row}: {count} dark pixels (deviation: {dev:.0f})")
        # Check if row number or count is meaningful
        if 32 <= row <= 126:
            print(f"    Row {row} as ASCII: '{chr(row)}'")
        if 32 <= count <= 126:
            print(f"    Count {count} as ASCII: '{chr(count)}'")

def analyze_column_patterns():
    """Analyze each column for patterns"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*60)
    print("COLUMN-BY-COLUMN ANALYSIS")
    print("="*60)
    
    # Analyze each column
    dark_counts = []
    for col in range(width):
        col_pixels = [pixels[row * width + col] for row in range(height)]
        dark = sum(1 for p in col_pixels if p < 128)
        dark_counts.append(dark)
    
    avg_dark = sum(dark_counts) / len(dark_counts)
    print(f"Average dark pixels per column: {avg_dark:.2f}")
    
    # Look for columns that deviate significantly
    unusual_cols = []
    for i, count in enumerate(dark_counts):
        deviation = abs(count - avg_dark)
        if deviation > 50:  # Threshold for unusual
            unusual_cols.append((i, count, deviation))
    
    print(f"\nUnusual columns (>{avg_dark+50:.0f} or <{avg_dark-50:.0f} dark pixels):")
    for col, count, dev in unusual_cols[:20]:
        print(f"  Column {col}: {count} dark pixels (deviation: {dev:.0f})")
        if 32 <= col <= 126:
            print(f"    Column {col} as ASCII: '{chr(col)}'")
        if 32 <= count <= 126:
            print(f"    Count {count} as ASCII: '{chr(count)}'")

def encode_counts_as_bytes():
    """Try to interpret dark/light counts as encoded data"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*60)
    print("ENCODING ANALYSIS")
    print("="*60)
    
    # Get dark counts per row
    dark_counts = []
    for row in range(height):
        row_start = row * width
        row_pixels = pixels[row_start:row_start + width]
        dark = sum(1 for p in row_pixels if p < 128)
        dark_counts.append(dark)
    
    # Try to map to ASCII
    print("\nDark counts mod 256 as bytes:")
    byte_string = bytes([d % 256 for d in dark_counts[:100]])
    print(f"First 100 rows as bytes: {byte_string[:50]}")
    
    # Check for printable characters
    printable = [chr(d % 256) for d in dark_counts if 32 <= (d % 256) <= 126]
    print(f"\nPrintable characters from dark counts: {''.join(printable[:100])}")
    
    # Try differences between consecutive rows
    print("\nDifferences between consecutive rows:")
    diffs = [dark_counts[i+1] - dark_counts[i] for i in range(len(dark_counts)-1)]
    printable_diffs = [chr(d + 128) for d in diffs if -128 <= d <= 127 and 32 <= (d + 128) <= 126]
    print(f"Printable from differences: {''.join(printable_diffs[:50])}")

def check_specific_pixel_values():
    """Check coordinates of specific pixel values"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*60)
    print("COORDINATES OF SPECIFIC PIXEL VALUES")
    print("="*60)
    
    target_values = [24, 120, 55, 60, 5]
    
    for target in target_values:
        print(f"\nPixel value {target}:")
        positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == target]
        print(f"  Found {len(positions)} pixels with value {target}")
        
        if len(positions) > 0:
            # Check first few positions
            for i, (x, y) in enumerate(positions[:10]):
                print(f"  Position {i}: ({x}, {y})")
                # Check if coordinates encode data
                if 32 <= x <= 126:
                    print(f"    X={x} -> '{chr(x)}'")
                if 32 <= y <= 126:
                    print(f"    Y={y} -> '{chr(y)}'")

if __name__ == "__main__":
    analyze_row_patterns()
    analyze_column_patterns()
    encode_counts_as_bytes()
    check_specific_pixel_values()
