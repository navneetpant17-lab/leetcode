
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length of linked list
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make the list circular
        tail.next = head

        # Step 3: Find new tail position
        k = k % length
        steps = length - k

        new_tail = head

        for i in range(steps - 1):
            new_tail = new_tail.next

        # Step 4: Set new head and break circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head

        