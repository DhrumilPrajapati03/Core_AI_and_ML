def va(s: str, t : str) -> bool:
    str1 = s.lower()
    str2 = s.lower()

    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")

    counts = [0]* 26

    for i in str1:
        counts[ord(i) - ord('a')]+=1

    for i in str2:
        counts[ord(i) - ord('a')]-=1

    for count in counts:
        if count!=0:
            return False
    return True

print(va("atal","lata"))