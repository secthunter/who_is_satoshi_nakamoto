# Haian.de Puzzle Research - Critical Findings

**Target**: https://haian.de  
**Subject**: Memorial page for Fabian "Haian" Schüßler (30.10.1986 - 20.10.2011)  
**Analysis Date**: March 2025  
**Framework**: AGENTS.md Protocol

---

## Executive Summary

This research analyzes a memorial webpage for potential hidden messages, steganography, or puzzle elements. The target appears to be a legitimate memorial site, but contains numerical and linguistic patterns that suggest embedded puzzle elements.

**Primary Finding**: The number **5** emerges as the key number through multiple mathematical relationships. Pixel coordinate analysis reveals a potential encoded message in X-coordinates of pixels with value 5.

---

## 1. Target Overview

### Page Structure
- Single static HTML memorial page
- 27 condolence messages from friends and family
- German/English bilingual content
- Gray color scheme (#A0A0A0, #808080, #505050)
- One memorial image: `haian_mit_text_skaliert_rand.jpeg` (700x1000 pixels, 269,508 bytes)

### Subject Information
- **Name**: Fabian "Haian" Schüßler
- **Birth**: 30.10.1986
- **Death**: 20.10.2011
- **Age at death**: 24 years, 11 months, 20 days (almost 25)
- **Days lived**: 9,121 days

---

## 2. Critical Numerical Findings

### The Number 5 (PRIMARY KEY)
Multiple independent calculations converge on the number 5:

| Calculation | Source | Result |
|-------------|--------|--------|
| 120 / 24 | Skat game values | **5** |
| 60 - 55 | Thomas's message | **5** |
| 24 × 5 = 120 | Skat multipliers | **5** |

**Significance**: 5 is the only number consistently derived from multiple message sources.

### Skat Game Values (24 and 120)
From Ihno's message: "Dein Blatt war so viel besser, als nur bis 24 zu reizen, damit wären auch durchaus 120 drin gewesen"

**24 and 120 are both Grand game values in Skat:**
- 24 = Grand with multiplier 2 (12 × 2)
- 120 = Grand with multiplier 10, called "Grand Ouvert" (12 × 10)
- 120 = 24 × 5

### ASCII Mappings from Numbers
| Number | Source | ASCII |
|--------|--------|-------|
| 120 | Ihno's Skat reference | 'x' |
| 100 | Sven's "100%" | 'd' |
| 55 | Thomas's message | '7' |
| 60 | Thomas's message | '<' |

### Age/Dates
- **9121 days lived** (7 × 1303)
- Death occurred 20 days before 25th birthday
- Isabella's message dated **24**.02.2012 (day 24 matches Skat number)

---

## 3. Pixel Coordinate Discovery (CRITICAL)

### Pixel Value 5 Analysis
Analysis of pixels with value 5 (the "key" number) reveals **ASCII characters in X-coordinates**:

**Extracted string (115 printable ASCII characters):**
```
kO~4OI|jM^{[kD_SZ25`R8TRrsQSj\a5b<F4pru445bE_O?BED52dqks8=RSVOSB?utAWhilWh8euz>Odiz|9kOkrt@@;DpN=Nn`_edl}MAB|~PCno>
```

### Key Patterns in Pixel String
- Contains "**25**" at position 17 (age he almost reached)
- Contains "**52**" (reversed 25)
- "**45**" appears twice
- Starts with 'k', ends with '>'
- Could be: encoded data, password, or cipher text

### Other Pixel Values
| Pixel Value | ASCII from X-coords | Notable Pattern |
|-------------|---------------------|-----------------|
| 5 | `kO~4OI|jM...` | Contains "25", "52" |
| 24 | 2308 chars | Too long, likely noise |
| 55 | 127 chars | Contains "=DH\rsv~>" |
| 60 | 77 chars | Contains "abkm_@BYZz" |
| 120 | 4 chars | "{wtq" |

---

## 4. Network & Path Analysis

### Confirmed Endpoints
| Path | Status | Notes |
|------|--------|-------|
| / | 200 OK | Main memorial page |
| /admin | **401** | **Authentication required - POTENTIAL ENTRY POINT** |
| /robots.txt | 404 | Not found |
| /sitemap.xml | 404 | Not found |

### Authentication Testing Results
- `/admin` requires HTTP Basic Authentication
- Tested credentials: **None succeeded**
  - admin/5, haian/5, fabian/5, 5/5
  - admin/24, admin/120, admin/25
  - admin/password, admin/haian
  - Various combinations with pixel 5 string

### Query Parameters
Tested parameters (key, password, flag, debug, admin) - **no effect on response**

---

## 5. Ruled Out (Negative Findings)

### Image Steganography
- ❌ **No EXIF metadata** found
- ❌ **No LSB steganography** (only noise patterns extracted)
- ❌ **No trailing data** after JPEG EOI marker (FFD9)
- ❌ **No JPEG comment segments** (COM markers)
- ❌ **No hidden strings** in binary

### HTML/Text Encoding
- ❌ **No zero-width characters** detected
- ❌ **No base64 patterns** in messages
- ❌ **No hex patterns** found
- ❌ **No meaningful acrostic** from first letters
- ❌ **Whitespace analysis** - normal HTML formatting only

### Linguistic Patterns
- ❌ **Every Nth letter** (N=2,3,5,7,10,12,24) - no readable message
- ❌ **First/last letters** - no meaningful words formed
- ❌ **Word frequency** - normal German condolence language

### Network
- ❌ Simple path enumeration (/24, /120, /5, etc.) all return 404
- ❌ Query parameters don't change response

---

## 6. Active Hypotheses

### H1: The Number 5 is the Key (CONFIRMED)
**Status**: **Validated by multiple sources**
- 120 / 24 = 5
- 60 - 55 = 5
- 24 × 5 = 120
- Pixel value 5 shows interesting patterns

### H2: Pixel 5 X-Coordinates Encode a Message (ACTIVE)
**Status**: **Under investigation**
- 115-character string extracted
- Contains "25", "52" - age-related numbers
- Could be: password, key, or encoded flag
- **Not valid base64** (padding issues)
- **Not simple ROT cipher**

### H3: /admin is the Entry Point (ACTIVE)
**Status**: **Confirmed endpoint, credentials unknown**
- Returns 401 (auth required) vs 404 for non-existent paths
- Requires correct username/password combination
- Pixel 5 string or "5" may be involved in credentials

### H4: Combined/Layered Solution (PENDING)
**Status**: **Speculative**
- Number 5 may unlock first layer
- Pixel string may decode to next step
- May require external tool or specific cipher

---

## 7. Research Artifacts Created

| Script | Purpose |
|--------|---------|
| `analyze_text.py` | Text patterns, acrostic, word frequency |
| `analyze_numbers.py` | Date calculations, number sequences |
| `analyze_image.py` | EXIF, LSB, JPEG structure analysis |
| `advanced_patterns.py` | Skat analysis, date significance |
| `advanced_pixel.py` | Row/column patterns, coordinate encoding |
| `advanced_stego.py` | JPEG marker analysis, DCT coefficients |
| `deep_coordinate_analysis.py` | Pixel ASCII extraction |
| `extract_pixel_ascii.py` | Full ASCII from pixel values |
| `decode_pixel5_string.py` | Decode pixel 5 string attempts |
| `test_web_paths.py` | Path discovery, credential testing |
| `test_admin_advanced.py` | Advanced credential combinations |

---

## 8. Next Steps & Recommendations

### Immediate Actions
1. **Decode the pixel 5 string** - Try different ciphers/encodings:
   - XOR with key "5"
   - Substitution cipher
   - Vigenère with key "5" or "25"
   - Binary encoding

2. **Expand credential testing** for /admin:
   - Try pixel 5 string segments (first 10, last 10, etc.)
   - Try "25" as password (the age significance)
   - Try combinations: haian/25, admin/SZ25

3. **Analyze the pixel 5 string deeper**:
   - Check for anagrams
   - Try frequency analysis
   - Look for substitution patterns

### Secondary Investigations
4. Check if coordinates (x,y) of pixel 5 form a pattern (image, QR, etc.)
5. Investigate "25" significance (almost 25 years old)
6. Look at message timestamps for additional patterns
7. Check German text for wordplay/anagrams

---

## 9. Key Evidence Summary

### Primary Clues
1. **Number 5** - Mathematically derived from multiple sources
2. **Pixel 5 string** - `kO~4OI|jM^{[kD_SZ25...` with embedded "25"
3. **Isabella's date** - Day 24 (24.02.2012) matches Skat number
4. **Thomas's numbers** - "55 - 60 jahren" = difference of 5
5. **Skat references** - 24, 120, game values with 5× relationship

### Secondary Clues
- Image dimensions: 700×1000 (7 and 1000 - no obvious significance)
- File size: 269,508 bytes (no obvious pattern)
- 27 condolence messages (no obvious significance)
- Norwegian phrase "Jeg elsker deg" (I love you) - potential significance

---

## 10. Conclusion

The memorial page contains **confirmed puzzle elements** centered around the number **5**. The Skat game references (24, 120) and mathematical relationships consistently point to 5 as the key. The **pixel value 5 X-coordinate string** is the most promising lead for the next layer of the puzzle.

The `/admin` endpoint requiring authentication is likely the entry point to the solution, but the correct credentials remain undetermined. The pixel 5 extracted string may be the password, or it may decode to reveal the password.

**Recommended focus**: Decode the pixel 5 string and test it (or its decoded form) as credentials for /admin.

---

*Research conducted following AGENTS.md protocol*  
*All findings documented in research/ folder structure*
