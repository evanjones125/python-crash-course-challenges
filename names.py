names = ['evan', 'cameron', 'ethan', 'max']

names[-1] = 'braden'

names.append('max')

for_print = f"{names[0].title()}\n{names[1].title()}\n{names[2].title()}\n{names[3].title()}\n{names[-1].title()}"

print(for_print)