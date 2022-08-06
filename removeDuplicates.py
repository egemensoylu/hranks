def removeDuplicates(self, head):
    node = head
    while node.next is not None:
        if node is not None:
            if node.next is not None:
                if node.next.data == node.data:
                    node.next = node.next.next

            if node.next is not None:
                if node.data != node.next.data:
                    node = node.next
    return head