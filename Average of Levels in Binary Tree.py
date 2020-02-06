import _collections
#
# We will be storing two Dictionaries , one for maintaing sum of a level ,
# another for maintaining num of nodes at that level. We will Iterate untill
# our queue becomes empty (keeping in mind that we are appending non-None nodes,
# therefore we exhaust at some point)


# Zip is an inbuilt function which simultaneously indexes over two lists at the same pace.



def averageOfLevels(self, root: TreeNode) -> List[float]:
    if not root:
        return

    result = []

    queue = [[root, 1]]

    hsh = collections.defaultdict(int)
    hsh1 = collections.defaultdict(int)

    while queue:
        root, level = queue.pop(0)

        hsh[level] += root.val
        hsh1[level] += 1
        if root.left:
            queue.append([root.left, level + 1])
        if root.right:
            queue.append([root.right, level + 1])

    for a, b in zip(hsh.values(), hsh1.values()):
        result.append(a / b)

    return result