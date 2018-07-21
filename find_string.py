# def find_string(text, match):
#     sub_str = ""
#     for i in range(len(text)):
#         if i > len(match) - 1:
#             return sub_str
#         if text[i] == match[i]:
#             i+=1
#             sub_str += text[i]
#         elif match[i] == '.' or match[i] == '?':
#             sub_str += text[i]
#             i+=1
#         elif match[i] == '*' and i == len(match) - 1 :
#             sub_str += text[i:]
#         else:
#             text = text[i+1:]
#             sub_str = ""
#     return sub_str  
# result = find_string('world','wor')
# print(result)
def find_string(str,pat):
 import re
 return re.findall(pat,str,re.I) 

result = find_string('world','wor')
print(result)