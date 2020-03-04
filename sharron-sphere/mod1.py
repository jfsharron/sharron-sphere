print(str(4))
convert_to_string = str
print(convert_to_string(4))


def runit(f, value):
    return f(value)

def odd(n): 
    return n % 2 == 1 

nums = []
nums = list(filter(odd, range(8001)))

print(nums)