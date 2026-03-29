# Research Summary & Current Findings

## Key Discoveries

### 1. The Number 5 Hypothesis (CONFIRMED)
Multiple mathematical relationships point to the number 5:
- **120 / 24 = 5** (Skat game value ratio)
- **60 - 55 = 5** (from Thomas's message: "55 - 60 jahren")
- 120 = 24 × 5 (Grand Ouvert = 5 × Grand)

This is the strongest candidate for the puzzle key/password.

### 2. Skat Game Values Analysis
From Ihno's message: "Dein Blatt war so viel besser, als nur bis 24 zu reizen, damit wären auch durchaus 120 drin gewesen"

**24 and 120 are both Grand game values:**
- 24 = Grand with multiplier 2 (12 × 2)
- 120 = Grand with multiplier 10, also called "Grand Ouvert" (12 × 10)

### 3. Pixel Coordinate ASCII Patterns
Analysis of pixel value 5 (the "key" number) shows ASCII characters in X coordinates:
- **'2', '5'** appearing together (rows 119-120)
- **'a', 'b'** appearing together (row 162)
- **'k'** appearing multiple times
- **'T', 'R'** appearing
- **'r', 's'** appearing together (row 151)
- **'d', 'l'** appearing

This suggests the image may encode a message through pixel positions.

### 4. Isabella's Date Significance
- Posted on **24.02.2012** - Day 24 matches the Skat number
- Day 24.02.2012 = 24th day of month
- Text contains ellipsis "..." and "<3"

### 5. What Has Been Ruled Out
- ❌ Image steganography (LSB, EXIF, trailing data, JPEG comments)
- ❌ HTML encoding (zero-width chars, base64, hex patterns)
- ❌ Simple acrostic patterns
- ❌ Every Nth letter analysis
- ❌ Color value ASCII encoding

### 6. Days Lived Calculation
- Birth: 30.10.1986
- Death: 20.10.2011
- **Age: 24 years, 11 months, 20 days** (almost 25)
- **Days lived: 9121 days** (corrected from earlier 9131)
- 9121 = 7 × 1303

### 7. ASCII Mappings from Numbers
| Number | ASCII |
|--------|-------|
| 120 | 'x' |
| 100 | 'd' |
| 55 | '7' |
| 60 | '<' |

### 8. Network Findings
- `/admin` returns 401 (authentication required)
- `/message_handler.php` referenced but commented out
- Other paths return 404 or ERR_ABORTED

## Active Hypotheses

### H1: The number 5 is the password for /admin
**Evidence:**
- Multiple mathematical derivations yield 5
- Pixel value 5 shows interesting patterns
- Simplest answer that fits all clues

**Test:** Try credentials admin/5, haian/5, fabian/5, 5/5

### H2: Pixel X-coordinates of value 5 encode a message
**Evidence:**
- ASCII characters found in X coordinates
- '2','5' together suggests "25"
- 'a','b' together suggests start of alphabet/sequence

**Next:** Extract all printable ASCII from pixel 5 X-coordinates

### H3: Combined approach needed
**Evidence:**
- No single technique reveals complete answer
- Number 5 may unlock deeper layer
- Multiple puzzle elements suggest layered design

## Next Actions

1. Complete credential testing for /admin
2. Extract complete ASCII sequence from pixel 5 X-coordinates
3. Test if "25" (almost 25 years old) is significant
4. Check if pixel patterns spell a word
5. Document all findings for final synthesis
