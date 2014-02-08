
import re

ff= open("source.delete")
try:
    all_the_text = ff.read( )
finally:
    ff.close( )

print re.findall(r"([a-z])",all_the_text)
