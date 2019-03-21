def to_rna(dna_strand):
    rna_dict = {
    'G':'C', 'C':'G', 'T':'A', 'A':'U'
    }
    rna_strand = str()
    for nucleotide in dna_strand:
        if nucleotide in rna_dict.keys():
            rna_strand += rna_dict[nucleotide]
    return rna_strand
