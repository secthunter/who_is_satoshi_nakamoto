#!/usr/bin/env python3
"""
Advanced message pattern analysis - nth word, telestic, and hidden patterns
"""

import re

MESSAGES = [
    {"author": "Alex (whiteheatsyd) Craft", "date": "02.11.2011 12:46", "text": "I am sorry to hear such tragic news, my thoughts are with you at this difficult time. He was always a pleasure to talk to and a man of great respect. You should be very proud of the young man he became. RIP"},
    {"author": "Jojo", "date": "31.10.2011 04:27", "text": "Ich werde dich nie vergessen, mein Freund! In den Jahren, die wir zusammen verbracht haben, die viel zu schnell vergangen sind, hast du mein Leben fuer immer bereichert. Dein Humor, dein Lachen und deine positive Ausstrahlung wo immer du warst, wird deiner Familie und deinen Freunden fuer immer in Erinnerung bleiben. Die Welt ist jetzt ein Stueck weniger freundlich. Fuer immer dein Freund Jojo"},
    {"author": "Isabella", "date": "24.02.2012 23:34", "text": "Haian...du fehlst mir unheimlich! :( Ich denke an unsere wunderbare Zeit. Ruhe in Frieden <3 Deine Isa"},
]

def analyze_isabella_date():
    """Isabella's message is dated 24.02.2012 - contains the number 24"""
    print("="*60)
    print("ISABELLA'S DATE ANALYSIS (24.02.2012)")
    print("="*60)
    
    msg = MESSAGES[2]
    print(f"Author: {msg['author']}")
    print(f"Date: {msg['date']}")
    print(f"Text: {msg['text']}")
    
    # 24.02.2012 contains:
    # - 24 (day) - matches the Skat number
    # - 02 (month)
    # - 2012 (year)
    
    print("\nDate significance:")
    print("  Day 24 = matches 'bis 24 zu reizen'")
    print("  Month 02 = February")
    print("  Year 2012 = 1 year after death")
    
    # Check text
    print(f"\nText analysis:")
    print(f"  Length: {len(msg['text'])} chars")
    print(f"  Contains '24' reference: {'24' in msg['date']}")

def analyze_skat_deep():
    """Deep dive into Skat game mechanics"""
    print("\n" + "="*60)
    print("SKAT GAME VALUE ANALYSIS")
    print("="*60)
    
    # Ihno's message mentions:
    # "Dein Blatt war so viel besser, als nur bis 24 zu reizen, damit wären auch durchaus 120 drin gewesen"
    
    print("Skat bidding terms:")
    print("  'Reizen' = bidding")
    print("  'bis 24 zu reizen' = bid up to 24")
    print("  '120 drin gewesen' = 120 would have been possible")
    
    # Game values in Skat:
    # Null = 23, 35, 46, 59
    # Grand = 24, 36, 48, 60, 72, 96, 120
    # Suit = 12, 18, 24, 30, 36, 48, 60
    
    print("\nGrand game values (multiplied by 12, 16, 20, 24):")
    base = 12
    for mult in [2, 3, 4, 5, 6, 8, 10]:
        val = base * mult
        marker = " <-- 24" if val == 24 else " <-- 120" if val == 120 else ""
        print(f"  12 × {mult} = {val}{marker}")
    
    print("\nKey finding: 24 and 120 are both Grand game values")
    print("24 = Grand with multiplier 2")
    print("120 = Grand with multiplier 10 (Grand Ouvert)")
    
    # Mathematical relationship
    print(f"\n120 / 24 = {120 // 24}")
    print(f"120 = 24 × 5")
    print(f"\n*** THE NUMBER 5 IS SIGNIFICANT ***")

def check_hidden_in_text():
    """Check for hidden patterns in message text"""
    print("\n" + "="*60)
    print("CHECKING FOR HIDDEN TEXT PATTERNS")
    print("="*60)
    
    # Look for patterns that might indicate hidden data
    for msg in MESSAGES:
        text = msg['text']
        
        # Check for unusual character sequences
        if '...' in text:
            print(f"{msg['author']}: Contains ellipsis '...'")
        
        # Check for HTML entities or encoded content
        if '&' in text and ';' in text:
            print(f"{msg['author']}: Contains potential HTML entities")
        
        # Check for repeated characters (possible stego)
        repeats = re.findall(r'(.)\1{2,}', text)
        if repeats:
            print(f"{msg['author']}: Repeated characters: {repeats}")

def analyze_every_nth_letter():
    """Extract every Nth letter to look for hidden messages"""
    print("\n" + "="*60)
    print("EVERY NTH LETTER ANALYSIS")
    print("="*60)
    
    for n in [5, 10, 12, 24]:
        all_text = ''.join([m['text'] for m in MESSAGES])
        # Remove spaces and punctuation
        clean = re.sub(r'[^a-zA-Z]', '', all_text)
        nth_letters = clean[n-1::n]
        print(f"\nEvery {n}th letter: {nth_letters[:50]}...")

if __name__ == "__main__":
    analyze_isabella_date()
    analyze_skat_deep()
    check_hidden_in_text()
    analyze_every_nth_letter()
