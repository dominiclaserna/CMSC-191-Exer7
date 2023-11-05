def reverse_complement(sequence):
    revSeq = sequence[::-1]
    revSeq = revSeq.replace("A", "x")
    revSeq = revSeq.replace("T", "y")
    revSeq = revSeq.replace("G", "z")
    revSeq = revSeq.replace("C", "w")
    
    revSeq = revSeq.replace("x", "T")
    revSeq = revSeq.replace("y", "A")
    revSeq = revSeq.replace("z", "C")
    revSeq = revSeq.replace("w", "G")

    print(revSeq)
    return revSeq


reverse_complement('GCAGTTGCA')