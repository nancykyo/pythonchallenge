import re

ff= open("equality.delete")
try:
    all_the_text = ff.read( )
finally:
    ff.close( )

print re.findall(r"([a-z][A-Z]{3}[a-z][A-Z]{3}[a-z])",all_the_text)

