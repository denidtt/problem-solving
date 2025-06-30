def is_palindrome(s):
    cleaned = [_.lower() for _ in s if _.isalnum()]
    return cleaned==cleaned[::-1]


print(is_palindrome('deni'))