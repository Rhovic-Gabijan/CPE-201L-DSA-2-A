def min_max(seq):
    if len(seq) == 1:
        return seq[0], seq[0]
    else:
        min_rest, max_rest = min_max(seq[1:])
        return min(seq[0], min_rest), max(seq[0], max_rest)
    
nums = [4,6,3,8,-4,7,2,9]
minimum, maximum = min_max(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)