x = '# asdfj'
lines = ['asdf', '@asjdfkl', '#asdjflk', 'dsf##$', '\n']
lines = [line for line in lines  if line[0] != '#' and line !='\n']

print(lines)
