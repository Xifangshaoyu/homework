import re

pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|30|31)\d{3}[0-9Xx]$'
id_card = '430602200012222356'

if re.match(pattern,id_card):
    print("身份证合法")
else:
    print("身份证不合法")