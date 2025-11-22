# LINKED LISTS - Complete Reference for ICPC
# Singly and Doubly Linked Lists with all operations

# ============ NODE CLASS ============

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    """Node for Doubly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# ============ SINGLY LINKED LIST ============

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # INSERT
    def insert_at_head(self, data):
        """Insert at beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert at end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_position(self, data, pos):
        """Insert at specific position (0-indexed)"""
        if pos == 0:
            self.insert_at_head(data)
            return

        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if not curr:
                return
            curr = curr.next

        if curr:
            new_node.next = curr.next
            curr.next = new_node

    # DELETE
    def delete_head(self):
        """Delete first node"""
        if self.head:
            self.head = self.head.next

    def delete_tail(self):
        """Delete last node"""
        if not self.head or not self.head.next:
            self.head = None
            return

        curr = self.head
        while curr.next and curr.next.next:
            curr = curr.next
        curr.next = None

    def delete_value(self, data):
        """Delete first occurrence of value"""
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next

    def delete_at_position(self, pos):
        """Delete at specific position"""
        if pos == 0:
            self.delete_head()
            return

        curr = self.head
        for _ in range(pos - 1):
            if not curr or not curr.next:
                return
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next

    # SEARCH
    def search(self, data):
        """Check if value exists"""
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    # TRAVERSE
    def display(self):
        """Print all values"""
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(values))

    def to_list(self):
        """Convert to Python list"""
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    # UTILITIES
    def length(self):
        """Get length"""
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverse(self):
        """Reverse the linked list"""
        prev = None
        curr = self.head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        self.head = prev

    def get_at_index(self, index):
        """Get value at index"""
        curr = self.head
        for _ in range(index):
            if not curr:
                return None
            curr = curr.next
        return curr.data if curr else None

    def find_middle(self):
        """Find middle node (slow and fast pointer)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def is_palindrome(self):
        """Check if linked list is palindrome"""
        values = self.to_list()
        return values == values[::-1]

    def has_cycle(self):
        """Detect cycle using Floyd's algorithm"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# ============ DOUBLY LINKED LIST ============

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        """Insert at beginning"""
        new_node = DNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert at end"""
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def delete_head(self):
        """Delete first node"""
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def reverse(self):
        """Reverse doubly linked list"""
        curr = self.head
        while curr:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        self.head = curr if self.head else self.head

    def display_forward(self):
        """Print forward"""
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        print(" <-> ".join(values))

    def display_backward(self):
        """Print backward"""
        if not self.head:
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        values = []
        while curr:
            values.append(str(curr.data))
            curr = curr.prev
        print(" <-> ".join(values))
