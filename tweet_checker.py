max_chars = 140
print("*" * 100)
tweet_len = len(input("enter your tweet: "))
if tweet_len <= max_chars:
    print(f"That {tweet_len} char tweet will work!")
else:
    print(f"Your {tweet_len} char tweet is {tweet_len - max_chars} char too long")