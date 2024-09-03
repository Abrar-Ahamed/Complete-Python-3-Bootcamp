t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ans = input()
    string = s+ans
    left_sum, right_sum = 0,0
    string_dict = {}
    string_fin = set(string)
    answer = set(ans)
    c = 0
    for i in string_fin:
        if i!= " ":
            string_dict[i] = c
            c+=1
    print(string_dict)
    for i in s:
        if i!= " ":
            left_sum += string_dict[i]
    for j in ans:
        if j!= " ":
            right_sum += string_dict[i]

    if left_sum == right_sum:
        print("true")
    else:
        print("false")
