def levelOrder(self, root):
    ans = ''
    if root is None:
        return ans

    q = collections.deque()
    q.append(root)

    while q:
        currSize = len(q)
        currList = []

        while currSize > 0:
            currNode = q.popleft()
            currList.append(currNode.data)
            currSize -= 1

            if currNode.left is not None:
                q.append(currNode.left)
            if currNode.right is not None:
                q.append(currNode.right)

        ans += ' '.join(map(str, currList)) + ' '

    print(ans)


import collections