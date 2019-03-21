def proteins(strand):
    codon_protein = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine',
        'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
        'UGU': 'Cysteine', 'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
    }
    length = int(len(strand)/3)
    sequence = []
    for seq in range(length):
        prot = codon_protein[strand[seq*3:(seq+1)*3]]
        if prot == 'STOP':
            break
        else:
            sequence.append(prot)
    return sequence
