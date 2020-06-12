from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # before the list is full, keep adding item to the tail and track the most recent addition
        if len(self.storage) < self.capacity:
            self.current = self.storage.add_to_tail(item)
        # when the list is full
        elif len(self.storage) == self.capacity:
            if self.current.next == None:
                self.storage.remove_from_head()
                self.current = self.storage.add_to_head(item)
            else:
                self.current.next.delete()
                self.current = self.current.insert_after(item)

    def get(self):
        list_buffer_content = []
        curr = self.storage.head

        if curr is not None:
            while curr.next is not None:
                list_buffer_content.append(curr.value)
                curr = curr.next
            list_buffer_content.append(curr.value)

        return list_buffer_content
