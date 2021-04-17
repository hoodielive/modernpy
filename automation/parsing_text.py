with open('text.txt', r) as f:
    for text in f:
        INPUT_TEXT = text
        words = INPUT_TEXT.split()
        print(words)
        break
        redacted = [''.join('X' if w.isdigit() else w for w in word) for word in words]
        ascii_text = [word.encode('ascii', errors='replace').decode('ascii') for word]

        newlines = [word + '\n' if word.endswith('.') else word for word in ascii_text]
        LINE_SIZE = 80
        lines = []
        line = ''
        for word in newlines:
            if line.endswith('\n') or len(line) + len(word) + len(word) + 1 > LINE_SIZE:
                lines.append(line)
                line = ''
            line = line + ' ' + word
lines = [line,title() for line in lines]
result = '\n'.join(lines)
