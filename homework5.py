from collections import defaultdict

def prefixspan(did, seq_list, freq_sequences, minsup):
    
    item_list = defaultdict(int)

    for s in seq_list:
        already_process_item = set()

        for i in s:
            if i not in already_process_item:
                item_list[i] = item_list[i] + 1
                already_process_item.add(i)

    f = {}

    for k, v in item_list.items():
        if v >= minsup:
            f[k] = v
    
    for i, s in f.items():
        
        did2 = did + i
        
        freq_sequences[did2] = s

        new_seq_list = []
        for seq in seq_list:
            index = seq.find(i)

            if (index != -1) and (index + 1 < len(seq)):
                new_seq_list.append(seq[index + 1 :])

        if new_seq_list:
            prefixspan(did2, new_seq_list, freq_sequences, minsup)

    return freq_sequences

def ord_prefixspan(filename, minsup):
    freq_sequences = {} # default initialization
    
    # complete your code here

    data = []

    with open(filename, 'r') as f:
        for line in f:
            c = line.strip().split(', ')

            if len(c) == 2:
                seq_c = c[1].strip('<>')
                data.append(seq_c)

    freq_sequences = prefixspan('', data, freq_sequences, minsup)
    
    return freq_sequences