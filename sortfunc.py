def treeGetAbort(tree):
    big = 0
    small = 10000
    for key in range(len(tree[1])):
        if big < tree[1][key]:
            big = tree[1][key]
    if small > tree[1][key]:
        small = tree[1][key]
    return big - small
def manySearch(tree):
    return tree[1][0]
def todaySearch(tree):
    return tree[1]
