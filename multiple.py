# python multiples string writes here
lines = ['Shiba Murmu\n', 'Mohan chandra Gandhi\n', 'Raja Ram mohan chandra nayak\n' ]
with open('writeslines.txt', 'w') as file:
    file.writelines(lines)
    print('Writes lines here.')