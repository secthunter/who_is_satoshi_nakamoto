#!/usr/bin/env python3
"""
Test /admin with the pixel 5 string and variations
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"

# The pixel 5 extracted string
PIXEL5_STRING = "kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>"

def test_advanced_credentials():
    """Test with the pixel 5 string and variations"""
    print("="*60)
    print("TESTING PIXEL 5 STRING CREDENTIALS")
    print("="*60)
    
    # Generate password candidates from pixel 5 string
    passwords = [
        PIXEL5_STRING,  # Full string
        PIXEL5_STRING[:10],  # First 10 chars
        PIXEL5_STRING[:5],  # First 5 chars
        PIXEL5_STRING[-10:],  # Last 10 chars
        PIXEL5_STRING[-5:],  # Last 5 chars
        ''.join(c for c in PIXEL5_STRING if c.isalnum()),  # Alphanumeric only
        '25',  # The age
        'SZ25',  # Chunk containing 25
        '52',  # Reversed 25
        '5',  # The key number
        'haian5',
        'fabian5',
        'admin5',
        'key',
        'flag',
        'kO~4O',  # First 5
        'PCno>',  # Last 5
    ]
    
    usernames = ['admin', 'haian', 'fabian', 'user', 'root', '5', '25', '']
    
    url = f"{BASE_URL}/admin"
    
    found = False
    for username in usernames:
        for password in passwords:
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                if response.status_code == 200:
                    print(f"\n[SUCCESS] Username: '{username}', Password: '{password}'")
                    print(f"Response length: {len(response.text)}")
                    print(f"First 200 chars: {response.text[:200]}")
                    found = True
                    return (username, password)
                elif response.status_code == 401:
                    pass  # Expected for wrong credentials
                else:
                    print(f"[{response.status_code}] {username}/{password[:20]}")
            except Exception as e:
                pass  # Silently skip errors
    
    if not found:
        print("\nNo valid credentials found in advanced test set.")
    return None

def test_specific_combinations():
    """Test specific combinations that might work"""
    print("\n" + "="*60)
    print("TESTING SPECIFIC COMBINATIONS")
    print("="*60)
    
    # Based on our analysis, try these specific combos
    combos = [
        ('admin', '5'),
        ('admin', '25'),
        ('admin', '24'),
        ('admin', '120'),
        ('admin', 'haian'),
        ('haian', '5'),
        ('haian', '25'),
        ('haian', 'haian'),
        ('5', '5'),
        ('fabian', '5'),
        ('skat', '5'),
        ('skat', '24'),
        ('skat', '120'),
        ('poker', '5'),
        ('24', '120'),  # Skat values
        ('120', '24'),  # Reversed
        ('admin', 'kO~4O'),
        ('admin', 'SZ25'),
        ('haian', 'SZ25'),
    ]
    
    url = f"{BASE_URL}/admin"
    
    for username, password in combos:
        try:
            response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
            if response.status_code == 200:
                print(f"\n[SUCCESS] '{username}' / '{password}' - ACCESS GRANTED!")
                print(f"Response: {response.text[:500]}")
                return (username, password)
            elif response.status_code == 401:
                print(f"[401] {username}/{password}")
        except Exception as e:
            print(f"[ERR] {username}/{password}: {str(e)[:30]}")
    
    return None

def check_http_headers():
    """Check for hidden headers or clues"""
    print("\n" + "="*60)
    print("CHECKING HTTP HEADERS")
    print("="*60)
    
    try:
        response = requests.get(BASE_URL, timeout=10)
        print(f"\nStatus: {response.status_code}")
        print(f"Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_advanced_credentials()
    test_specific_combinations()
    check_http_headers()
