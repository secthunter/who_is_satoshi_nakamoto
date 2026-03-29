#!/usr/bin/env python3
"""
Decode the pixel 5 X-coordinate ASCII string
Looks like it could be base64 or other encoding
"""

import base64
import binascii

# The extracted string from pixel value 5 X-coordinates
PIXEL5_STRING = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

def try_base64_decode(s):
    """Try to decode as base64"""
    print("="*60)
    print("BASE64 DECODE ATTEMPTS")
    print("="*60)
    
    # Try standard base64
    try:
        # Add padding if needed
        padded = s + '=' * (4 - len(s) % 4) if len(s) % 4 else s
        decoded = base64.b64decode(padded)
        print(f"Standard base64: {decoded}")
        try:
            print(f"As UTF-8: {decoded.decode('utf-8')}")
        except:
            pass
    except Exception as e:
        print(f"Standard base64 failed: {e}")
    
    # Try URL-safe base64
    try:
        # Replace characters for URL-safe
        url_safe = s.replace('-', '+').replace('_', '/')
        padded = url_safe + '=' * (4 - len(url_safe) % 4) if len(url_safe) % 4 else url_safe
        decoded = base64.b64decode(padded)
        print(f"URL-safe base64: {decoded}")
        try:
            print(f"As UTF-8: {decoded.decode('utf-8')}")
        except:
            pass
    except Exception as e:
        print(f"URL-safe base64 failed: {e}")

def analyze_string_properties(s):
    """Analyze the string properties"""
    print("\n" + "="*60)
    print("STRING ANALYSIS")
    print("="*60)
    
    print(f"\nLength: {len(s)}")
    print(f"Length mod 4: {len(s) % 4}")
    
    # Character frequency
    from collections import Counter
    freq = Counter(s)
    print(f"\nCharacter frequency:")
    for char, count in freq.most_common(20):
        print(f"  '{char}': {count}")
    
    # Check for specific patterns
    print(f"\nSpecific patterns:")
    print(f"  Contains '25': {'25' in s}")
    print(f"  Contains '52': {'52' in s}")
    print(f"  Contains '5': {s.count('5')} times")
    print(f"  Contains 'k': {s.count('k')} times")
    
    # Positions of '25'
    pos25 = [i for i in range(len(s)-1) if s[i:i+2] == '25']
    print(f"  Positions of '25': {pos25}")

def try_rot_cipher(s):
    """Try ROT ciphers"""
    print("\n" + "="*60)
    print("ROT CIPHER ATTEMPTS")
    print("="*60)
    
    for shift in range(1, 26):
        result = ""
        for c in s:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result += chr((ord(c) - base + shift) % 26 + base)
            else:
                result += c
        
        # Check if result looks like readable text
        readable = sum(1 for c in result if c.isalpha() or c.isspace() or c in '.,!?')
        if readable > len(result) * 0.8:
            print(f"\nROT{shift}: {result[:80]}")

def try_reversal(s):
    """Try reversing the string"""
    print("\n" + "="*60)
    print("REVERSAL ATTEMPTS")
    print("="*60)
    
    reversed_s = s[::-1]
    print(f"\nReversed: {reversed_s}")
    
    # Try base64 on reversed
    try:
        decoded = base64.b64decode(reversed_s)
        print(f"Reversed base64 decoded: {decoded}")
    except:
        pass

def try_chunks(s):
    """Try processing in chunks"""
    print("\n" + "="*60)
    print("CHUNK ANALYSIS")
    print("="*60)
    
    # Try 2-char chunks
    chunks2 = [s[i:i+2] for i in range(0, len(s), 2)]
    print(f"\n2-char chunks (first 20): {chunks2[:20]}")
    
    # Try 4-char chunks
    chunks4 = [s[i:i+4] for i in range(0, len(s), 4)]
    print(f"\n4-char chunks (first 10): {chunks4[:10]}")
    
    # Try 5-char chunks (the magic number!)
    chunks5 = [s[i:i+5] for i in range(0, len(s), 5)]
    print(f"\n5-char chunks (first 10): {chunks5[:10]}")
    
    # Check if any chunks are meaningful
    print(f"\nAll 5-char chunks:")
    for i, chunk in enumerate(chunks5):
        print(f"  {i:2d}: '{chunk}'")

def check_key_patterns():
    """Check for patterns related to 'key'"""
    s = PIXEL5_STRING
    
    print("\n" + "="*60)
    print("KEY PATTERN CHECK")
    print("="*60)
    
    # The string starts with 'k'
    print(f"\nStarts with 'k': {s.startswith('k')}")
    print(f"Ends with '>': {s.endswith('>')}")
    
    # Check if it could be a key/password itself
    print(f"\nCould this BE the password/key?")
    print(f"First 10 chars: {s[:10]}")
    print(f"Last 10 chars: {s[-10:]}")
    
    # Substrings that look like words
    possible_words = ['key', 'flag', 'pass', 'word', 'admin', 'haian', 'five', '25']
    for word in possible_words:
        if word in s.lower():
            print(f"  Found '{word}' at position {s.lower().index(word)}")

def extract_clean_password():
    """Extract what could be a clean password"""
    s = PIXEL5_STRING
    
    print("\n" + "="*60)
    print("POTENTIAL PASSWORD CANDIDATES")
    print("="*60)
    
    # The number 5 is key, maybe first/last 5 chars?
    print(f"\nFirst 5 chars: '{s[:5]}'")
    print(f"Last 5 chars: '{s[-5:]}'")
    print(f"Chars at position 5: '{s[5:10]}'")
    
    # Extract alphanumeric only
    alphanumeric = ''.join(c for c in s if c.isalnum())
    print(f"\nAlphanumeric only ({len(alphanumeric)} chars): {alphanumeric[:50]}")
    print(f"First 5 alphanumeric: '{alphanumeric[:5]}'")
    
    # Maybe the password is just "5" or "25" or "52"
    print(f"\nSimple candidates:")
    print(f"  '5' (the key number)")
    print(f"  '25' (almost 25 years old)")
    print(f"  '24' (Skat number, age)")
    print(f"  'kO~4O' (first 5 of pixel string)")

if __name__ == "__main__":
    print(f"Analyzing: {PIXEL5_STRING}")
    
    analyze_string_properties(PIXEL5_STRING)
    try_base64_decode(PIXEL5_STRING)
    try_rot_cipher(PIXEL5_STRING)
    try_reversal(PIXEL5_STRING)
    try_chunks(PIXEL5_STRING)
    check_key_patterns()
    extract_clean_password()
