def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high)
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
                high = mid - 1
        else:
            return True
    return False

