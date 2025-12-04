post_at = set(
    index_row + 1j * index_col
    for index_row, line in enumerate(open("day04/input"))
    for index_col, elt in enumerate(line)
    if elt == "@"
)
# part 2
count = 1

papers = 0
while count == 1:
    adjacents = [
        set(pos + real + 1j * imag for real in (-1, 0, 1) for imag in (-1, 0, 1))
        - {pos}
        for pos in post_at
    ]
    neighbors = [post_at.intersection(s) for s in adjacents]
    mask = [len(elt) < 4 for elt in neighbors]
    removed = set(pos for pos, index in zip(post_at, mask) if index)
    post_at = post_at - removed
    added = sum(mask)
    papers += added
    print(papers)
    if added == 0:
        count = 0
print(papers)
