#!/usr/bin/env python3
"""
Test various paths and credentials on haian.de
"""

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://haian.de"

def test_paths():
    """Test various potential hidden paths"""
    paths = [
        "/admin",
        "/login",
        "/flag",
        "/key",
        "/secret",
        "/5",
        "/24",
        "/120",
        "/x",
        "/9131",
        "/9121",
        "/haian",
        "/fabian",
        "/skat",
        "/poker",
        "/2011",
        "/1986",
        "/30101986",
        "/20102011",
        "/password",
        "/.env",
        "/config",
        "/api",
        "/debug",
    ]
    
    print("="*60)
    print("PATH DISCOVERY")
    print("="*60)
    
    for path in paths:
        try:
            url = f"{BASE_URL}{path}"
            response = requests.get(url, timeout=10, allow_redirects=False)
            status = response.status_code
            
            if status == 200:
                print(f"[200] {path} - FOUND")
            elif status == 401:
                print(f"[401] {path} - AUTH REQUIRED (potential entry!)")
            elif status == 403:
                print(f"[403] {path} - FORBIDDEN")
            elif status == 301 or status == 302:
                print(f"[{status}] {path} - REDIRECT to {response.headers.get('Location', 'unknown')}")
            elif status != 404:
                print(f"[{status}] {path} - UNUSUAL")
        except Exception as e:
            print(f"[ERR] {path} - {str(e)[:50]}")

def test_admin_credentials():
    """Test various credentials for /admin"""
    print("\n" + "="*60)
    print("ADMIN CREDENTIAL TESTING")
    print("="*60)
    
    # Potential usernames
    usernames = ["admin", "haian", "fabian", "user", "root"]
    
    # Potential passwords (based on our analysis)
    passwords = [
        "5",          # The key number
        "24",         # Skat bid
        "120",        # Skat value
        "55",         # Thomas's number
        "60",         # Thomas's number
        "9131",       # Previous days lived calculation
        "9121",       # Correct days lived
        "x",          # ASCII from 120
        "7",          # ASCII from 55
        "password",
        "haian",
        "fabian",
        "123456",
        "admin",
    ]
    
    url = f"{BASE_URL}/admin"
    
    for username in usernames:
        for password in passwords:
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                if response.status_code == 200:
                    print(f"[SUCCESS] {username}/{password} - ACCESS GRANTED!")
                    print(f"Response length: {len(response.text)}")
                    return (username, password)
                elif response.status_code != 401:
                    print(f"[{response.status_code}] {username}/{password}")
            except Exception as e:
                print(f"[ERR] {username}/{password} - {str(e)[:30]}")
    
    print("\nNo valid credentials found in test set.")
    return None

def test_query_params():
    """Test query parameters on main page"""
    print("\n" + "="*60)
    print("QUERY PARAMETER TESTING")
    print("="*60)
    
    params_to_try = [
        {"key": "5"},
        {"password": "5"},
        {"flag": "true"},
        {"debug": "1"},
        {"admin": "true"},
        {"24": "120"},
    ]
    
    for params in params_to_try:
        try:
            response = requests.get(BASE_URL, params=params, timeout=5)
            print(f"Params {params}: Status {response.status_code}, Length {len(response.text)}")
        except Exception as e:
            print(f"[ERR] {params} - {str(e)[:30]}")

if __name__ == "__main__":
    test_paths()
    test_admin_credentials()
    test_query_params()
