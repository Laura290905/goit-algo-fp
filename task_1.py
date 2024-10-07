class ListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def add(self, value):
        new_node = ListNode(value)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def reverse_list(self):
        previous = None
        current = self.head_node
        while current:
            next_temp = current.next_node
            current.next_node = previous
            previous = current
            current = next_temp
        self.head_node = previous

    def sort_list(self):
        sorted_head = None
        current = self.head_node
        while current:
            next_temp = current.next_node
            sorted_head = self.insert_sorted(sorted_head, current)
            current = next_temp
        self.head_node = sorted_head

    def insert_sorted(self, head, node_to_insert):
        current = head
        if not head or head.value >= node_to_insert.value:
            node_to_insert.next_node = head
            head = node_to_insert
        else:
            while current.next_node and current.next_node.value < node_to_insert.value:
                current = current.next_node
            node_to_insert.next_node = current.next_node
            current.next_node = node_to_insert
        return head

    def merge_lists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.value < list2.value:
                tail.next_node = list1
                list1 = list1.next_node
            else:
                tail.next_node = list2
                list2 = list2.next_node
            tail = tail.next_node
        tail.next_node = list1 if list1 else list2
        return dummy.next_node

    def display(self):
        current = self.head_node
        while current:
            print(current.value, end=" -> ")
            current = current.next_node
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
print("Original list:")
linked_list.display()

linked_list.reverse_list()
print("Reversed list:")
linked_list.display()

linked_list.sort_list()
print("Sorted list:")
linked_list.display()

# Merging two sorted lists
list1 = LinkedList()
list1.add(10)
list1.add(30)
list1.add(50)

list2 = LinkedList()
list2.add(20)
list2.add(40)
list2.add(60)

merged_list = LinkedList()
merged_list.head_node = merged_list.merge_lists(list1.head_node, list2.head_node)
print("Merged sorted list:")
merged_list.display()