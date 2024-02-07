#longest substring without repeating characters

s = "abcabcbb"
new_s = ""
for i in s:
    new_s += i
    if i == new_s[-1]:
        continue
    
    

print(f"longest substring without repeating characters is {new_s} and its length is {len(new_s)}")