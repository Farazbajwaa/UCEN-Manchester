def extract_and_rearrange(string):
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    str_2 = "".join(string[6:13].split('ro'))
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))
    str_4 = "".join(string[21:29].split(string[23:28]))

    return str_1 + " " + str_2 + " " + str_3 + " " + str_4

def ultra_extract_and_rearrange(string):
    first_transform = extract_and_rearrange(string)
    return first_transform

print(ultra_extract_and_rearrange("egthb quirock nwoGrb forijmpxv"))

Code is :The quick brown fox
