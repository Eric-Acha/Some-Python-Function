import re

pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
string = 'eric2233+-@123gstwffff.com'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,\d}")

password = 'jaw43%$8'


a = pattern.search(string)
check = pattern2.fullmatch(password)


print(check)
