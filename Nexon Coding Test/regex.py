target=  "kdh"
target= ".*?".join(target)
import re
print(target)
p = re.compile(target)
s = 'kaaadahrad'
ans=0
print(p.findall(s))
