s = input()
while s:
    if s.endswith("@@@"):
        # s = input()
        continue
    if s.startswith("##"):
        print(s[2:])
    else:
        print(s)
    s = input()

print('\n'.join(line.lstrip('#') for line in iter(input, '') if not line.endswith('@@@')))