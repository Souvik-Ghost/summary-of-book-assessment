content = input('enter the file name or text')
if content[len(content) - 4:] == '.txt':
  val = content.rindex(' ')
  print(f'.Summary of {content[val + 1:]}')
else:
  print('.Summary of text pasted')