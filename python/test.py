line = ""
l = []
while True:
      try:
        line = input()
        if line == '':
          break
        else:
          l.append(line)
      except EOFError:
        break

print(l.sort())
