class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def insertion_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next
        sorted_head = insert_into_sorted(sorted_head, current)
        current = next_node

    return sorted_head

def insert_into_sorted(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return sorted_head

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

if __name__ == "__main__":
    head = Node(3)
    head.next = Node(1)
    head.next.next = Node(4)
    head.next.next.next = Node(2)

    # Reverse the linked list
    reversed_head = reverse_linked_list(head)
    print("Reversed Linked List:")
    current = reversed_head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

    # Sort the linked list using insertion sort
    sorted_head = insertion_sort_linked_list(reversed_head)
    print("Sorted Linked List:")
    current = sorted_head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

    # Create two sorted linked lists
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)

    # Merge the two sorted linked lists
    merged_list = merge_sorted_lists(list1, list2)
    print("Merged Sorted Lists:")
    current = merged_list
    while current is not None:
        print(current.data, end=" ")
        current = current.next