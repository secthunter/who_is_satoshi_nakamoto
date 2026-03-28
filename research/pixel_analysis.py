#!/usr/bin/env python3
"""
Image pixel pattern analysis - light/dark pixel counts and color distributions
"""

from PIL import Image

IMAGE_PATH = "research/01_assets/images/haian_mit_text_skaliert_rand.jpeg"

def analyze_pixel_patterns():
    """Analyze pixel brightness patterns"""
    img = Image.open(IMAGE_PATH)
    
    print("="*60)
    print("PIXEL PATTERN ANALYSIS")
    print("="*60)
    print(f"Image size: {img.size}")
    print(f"Image mode: {img.mode}")
    
    # Convert to grayscale for brightness analysis
    if img.mode != 'L':
        gray = img.convert('L')
    else:
        gray = img
    
    pixels = list(gray.getdata())
    total_pixels = len(pixels)
    
    print(f"\nTotal pixels: {total_pixels}")
    
    # Count light vs dark pixels
    # Dark: 0-127, Light: 128-255
    dark = sum(1 for p in pixels if p < 128)
    light = sum(1 for p in pixels if p >= 128)
    
    print(f"\nDark pixels (0-127): {dark}")
    print(f"Light pixels (128-255): {light}")
    print(f"Dark/Light ratio: {dark/light:.4f}")
    
    # Check for specific patterns in counts
    print(f"\nDark count: {dark}")
    print(f"Light count: {light}")
    
    # ASCII from counts
    if 32 <= dark <= 126:
        print(f"Dark count as ASCII: '{chr(dark)}'")
    if 32 <= light <= 126:
        print(f"Light count as ASCII: '{chr(light)}'")
    
    # Analyze by brightness ranges
    ranges = [(0, 50), (51, 100), (101, 150), (151, 200), (201, 255)]
    print("\nBrightness distribution:")
    for min_b, max_b in ranges:
        count = sum(1 for p in pixels if min_b <= p <= max_b)
        print(f"  {min_b}-{max_b}: {count}")
    
    # Check for exact numbers mentioned in puzzle
    print("\nChecking for specific numbers:")
    print(f"  24: {pixels.count(24)}")
    print(f"  120: {pixels.count(120)}")
    print(f"  55: {pixels.count(55)}")
    print(f"  60: {pixels.count(60)}")
    print(f"  5: {pixels.count(5)}")
    
    # RGB analysis if color image
    if img.mode == 'RGB':
        print("\nRGB Channel Analysis:")
        r_vals = [p[0] for p in img.getdata()]
        g_vals = [p[1] for p in img.getdata()]
        b_vals = [p[2] for p in img.getdata()]
        
        for name, vals in [('R', r_vals), ('G', g_vals), ('B', b_vals)]:
            dark_c = sum(1 for v in vals if v < 128)
            light_c = sum(1 for v in vals if v >= 128)
            print(f"  {name}: Dark={dark_c}, Light={light_c}")

def analyze_grid_patterns():
    """Analyze image in a grid to find patterns"""
    img = Image.open(IMAGE_PATH)
    gray = img.convert('L')
    
    print("\n" + "="*60)
    print("GRID PATTERN ANALYSIS")
    print("="*60)
    
    width, height = img.size
    print(f"Dimensions: {width}x{height}")
    
    # Check if dimensions encode anything
    print(f"\nDimensions analysis:")
    print(f"  Width: {width}")
    print(f"  Height: {height}")
    print(f"  Width as ASCII: '{chr(width)}'" if 32 <= width <= 126 else "  Width: non-printable")
    print(f"  Height as ASCII: '{chr(height)}'" if 32 <= height <= 126 else "  Height: non-printable")
    
    # Check aspect ratio
    ratio = width / height
    print(f"  Aspect ratio: {ratio:.4f}")
    
    # Analyze quadrants
    print("\nQuadrant analysis:")
    mid_w = width // 2
    mid_h = height // 2
    
    # Get average brightness per quadrant
    quadrants = [
        (0, 0, mid_w, mid_h, "Top-Left"),
        (mid_w, 0, width, mid_h, "Top-Right"),
        (0, mid_h, mid_w, height, "Bottom-Left"),
        (mid_w, mid_h, width, height, "Bottom-Right"),
    ]
    
    for x1, y1, x2, y2, name in quadrants:
        quadrant = gray.crop((x1, y1, x2, y2))
        avg = sum(quadrant.getdata()) / len(list(quadrant.getdata()))
        print(f"  {name}: avg brightness = {avg:.2f}")

def find_repeating_patterns():
    """Look for repeating byte patterns"""
    with open(IMAGE_PATH, 'rb') as f:
        data = f.read()
    
    print("\n" + "="*60)
    print("REPEATING PATTERN ANALYSIS")
    print("="*60)
    
    # Look for runs of same byte
    print("\nLong runs of identical bytes:")
    current_byte = data[0]
    run_length = 1
    runs = []
    
    for byte in data[1:]:
        if byte == current_byte:
            run_length += 1
        else:
            if run_length > 10:
                runs.append((current_byte, run_length))
            current_byte = byte
            run_length = 1
    
    # Show longest runs
    runs.sort(key=lambda x: x[1], reverse=True)
    for byte, length in runs[:10]:
        print(f"  Byte 0x{byte:02X} ({byte}): {length} repetitions")

if __name__ == "__main__":
    analyze_pixel_patterns()
    analyze_grid_patterns()
    find_repeating_patterns()
