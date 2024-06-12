def check_palindrome(num):
    rev_num = 0
    dup_num = num
    while num:
        last_digit = num%10
        rev_num = (rev_num*10)+last_digit
        num = num//10
    if rev_num == dup_num:
        return True
    return False

def check_palindrome_in_range(min_num, max_num):
    arr = []
    for i in range(min_num, max_num+1):
        rev_num = 0
        dup_num = i
        while i:
            last_digit = i%10
            rev_num = (rev_num*10)+last_digit
            i = i//10
        if rev_num == dup_num:
            arr.append(rev_num)
    return arr

print(check_palindrome(123454321))
print(check_palindrome_in_range(10,700))