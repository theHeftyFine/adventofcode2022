signal = open("input.txt").readline()

def first_seq_of_len(ln):

    chars = 0
    
    # slide reading window 1 index at a time
    for i in range(0, len(signal)-ln):
        accum = set()
        # add characters of block to set accumulator, for easy counting
        for ch in signal[i:i+ln]:
            accum.add(ch)
        # if the length of the accumulator is equal to the desired length
        # the block contains no duplicates. We found our block, and break the loop
        if len(accum) == ln:
            chars += ln
            break
        # if not, block not found, add one character to the counter, and slide to next index
        else:
            chars += 1
            
    return chars
        
print('solution 1:', first_seq_of_len(4))
print('solution 2:', first_seq_of_len(14))