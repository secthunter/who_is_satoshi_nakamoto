#!/usr/bin/env python3
"""
Extract ASCII message from pixel value 5 X-coordinates
Based on finding that pixel value 5 (the 'key' number) has ASCII patterns in X coords
"""

from PIL import Image

IMAGE_PATH = "images/haian_mit_text_skaliert_rand.jpeg"

def extract_pixel5_ascii():
    """Extract all printable ASCII from pixel value 5 X-coordinates"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("="*70)
    print("EXTRACTING ASCII FROM PIXEL VALUE 5 X-COORDINATES")
    print("="*70)
    
    # Get all positions where pixel value = 5
    positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == 5]
    
    print(f"\nTotal pixels with value 5: {len(positions)}")
    
    # Extract X coordinates that are printable ASCII (32-126)
    x_ascii_chars = []
    x_coords = []
    
    for x, y in positions:
        if 32 <= x <= 126:
            x_ascii_chars.append(chr(x))
            x_coords.append(x)
    
    print(f"\nPrintable ASCII X-coordinates: {len(x_ascii_chars)}")
    print(f"\nAll X-ASCII characters in order:")
    print(''.join(x_ascii_chars))
    
    print(f"\n\nX coordinates (numeric): {x_coords}")
    
    # Try to find patterns
    print("\n" + "="*70)
    print("PATTERN ANALYSIS")
    print("="*70)
    
    # Group consecutive characters
    message = ''.join(x_ascii_chars)
    print(f"\nFull message: {message}")
    
    # Look for common words
    words_to_check = ['the', 'and', 'flag', 'key', 'pass', 'word', 'admin', 'haian', 'secret']
    print("\nChecking for common words:")
    for word in words_to_check:
        if word.lower() in message.lower():
            print(f"  Found: '{word}'")
    
    # Check for repeating patterns
    print("\nChecking for repeating sequences:")
    for length in [2, 3, 4, 5]:
        sequences = {}
        for i in range(len(message) - length + 1):
            seq = message[i:i+length]
            sequences[seq] = sequences.get(seq, 0) + 1
        
        repeats = {k: v for k, v in sequences.items() if v > 1}
        if repeats:
            print(f"\n  Repeating {length}-char sequences:")
            for seq, count in sorted(repeats.items(), key=lambda x: -x[1])[:10]:
                print(f"    '{seq}': {count} times")

def extract_all_pixel_ascii():
    """Extract ASCII from all target pixel values"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("ASCII FROM ALL SIGNIFICANT PIXEL VALUES")
    print("="*70)
    
    target_values = [5, 24, 55, 60, 120]
    
    for target in target_values:
        positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == target]
        
        # X coordinates
        x_chars = [chr(x) for x, y in positions if 32 <= x <= 126]
        # Y coordinates  
        y_chars = [chr(y) for x, y in positions if 32 <= y <= 126]
        
        print(f"\nPixel value {target}:")
        print(f"  X-ASCII ({len(x_chars)} chars): {''.join(x_chars)[:80]}")
        print(f"  Y-ASCII ({len(y_chars)} chars): {''.join(y_chars)[:80]}")

def analyze_sequences():
    """Look for specific sequences in the ASCII"""
    img = Image.open(IMAGE_PATH).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    
    print("\n" + "="*70)
    print("SPECIFIC SEQUENCE ANALYSIS")
    print("="*70)
    
    positions = [(i % width, i // width) for i, p in enumerate(pixels) if p == 5]
    x_coords = [x for x, y in positions if 32 <= x <= 126]
    
    # Check for common flag formats
    print("\nChecking X-coordinates for flag patterns:")
    
    # Convert to string and search
    coord_str = ''.join(map(str, x_coords))
    print(f"Coordinates as string: {coord_str[:100]}")
    
    # Check if coordinates form readable message
    message = ''.join([chr(x) for x in x_coords])
    print(f"\nAs message: {message}")
    
    # Check for "key" related patterns
    if 'key' in message.lower():
        print("\n*** Found 'key' in message! ***")
    if 'flag' in message.lower():
        print("\n*** Found 'flag' in message! ***")
    if 'pass' in message.lower():
        print("\n*** Found 'pass' in message! ***")

if __name__ == "__main__":
    extract_pixel5_ascii()
    extract_all_pixel_ascii()
    analyze_sequences()
