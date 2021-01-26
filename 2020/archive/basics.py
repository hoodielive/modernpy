employees = {
    'Oya' : 434545,
    'Ogun' : 932304,
    'Sango': 10425,
    'Osanyin' : 32424
}

top_earners = []

for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key, val)) 
print(top_earners)

# all this can be done like: 

top_earners_baptized = [ (k, v) for k, v in employees.items() if v >= 100000 ]
print(top_earners_baptized)

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [[ x for x in line.split() if len(x) > 3 ] for line in text.split('\n')]
print(w)

txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
print(list(mark))
