from collections import deque

def matching_paren(string):
  s = deque()
  
  for c in string:
    if c == '(':
      s.append(c)
    elif c == ')':
      try:
        char = s.pop()
      except:
        return False
  
  return len(s) == 0

print(matching_paren("sdfsd"))

print(matching_paren("JSDKLF)"))

print(matching_paren("GSFG(SDGGSG_SsDF(SDFSD)"))

print(matching_paren("GSD(@)G(@)G(G(GGG(G(G)__D)))"))
