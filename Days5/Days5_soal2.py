def find(nums, target):
    x = { }
    for i, j in enumerate(nums):
        hasil = target - j
        if hasil in x:
            return[x[hasil], i]
        x[j] = i
    return None

if __name__ == "__main__":
    nums = [ 2, 7, 11, 15]
    target = 9
    
print(find(nums, target))