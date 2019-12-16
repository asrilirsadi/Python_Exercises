str_brackets = '(()))((())'
open_brackets = []
close_brackets = []
result = True

# print(len(str_brackets))
for i in range(len(str_brackets)):
    if str_brackets[i] == '(':
        open_brackets.append(i)
    if str_brackets[i] == ')':
        close_brackets.append(i)

if len(open_brackets) == len(close_brackets):
    check = len(open_brackets)
    for j in range(check):
        if open_brackets[j] > close_brackets[j]:
            result = False
else:
    result = False

print(open_brackets)
print(close_brackets)
print(result)