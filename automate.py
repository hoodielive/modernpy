#result = template.format(*parameters)

INPUT_TEXT = '''
    AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTNACORP
    HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS INLINE
'''

words = INPUT_TEXT.split()

redacted = [''.join('X' if w.isdigit() else w for w in word) for word in words]

ascii_text = [words.encode('ascii', errors='replace').decode('ascii') for word in redacted]

newlines = [words + '\n' if word.endswith('.') else word in ascii_text]
LINE_SIZE = 80
lines = []
line = ''
for word in newlines:
    if line.endswith('\n') or len(line) + len(word) + 1 > LINE_SIZE:
        lines.append(line)
        line = ''
    line = line + ' ' + word

lines = [ line.title() for line in lines ]
result = '\n'.join(lines)

print(result)
