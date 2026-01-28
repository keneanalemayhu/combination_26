class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.map = {}

    def arrive(self, name):
        """Regular walk-in joins at the back (tail)."""
        node = Node(name)
        self.map[name] = node
        if not self.head:  # Empty list
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def arrive_vip(self, name):
        """VIP joins at the front (head)."""
        node = Node(name)
        self.map[name] = node
        if not self.head:  # Empty list
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def leave(self, name):
        """Remove a person from anywhere in O(1)."""
        node = self.map.get(name)
        if not node:
            print(f"{name} not found in line.")
            return
        # Update links
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next  # Leaving head
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  # Leaving tail
        del self.map[name]

    def seat(self):
        """Host seats the person at the front (head)."""
        if not self.head:
            print("No one to seat.")
            return
        name = self.head.name
        print(f"Seating {name}.")
        self.leave(name)

    def show_line(self):
        """Print the current line order."""
        curr = self.head
        line = []
        while curr:
            line.append(curr.name)
            curr = curr.next
        print("Line:", " -> ".join(line) if line else "Empty")


# ---------------- CLI Simulation ----------------
def run_cli():
    dll = DoublyLinkedList()
    print("VIP Restaurant Manager")
    print("Commands: ARRIVE <name>, ARRIVE_VIP <name>, LEAVE <name>, SEAT, SHOW_LINE, EXIT")

    while True:
        cmd = input("> ").strip().split()
        if not cmd:
            continue

        action = cmd[0].upper()

        if action == "ARRIVE" and len(cmd) == 2:
            dll.arrive(cmd[1])
            dll.show_line()

        elif action == "ARRIVE_VIP" and len(cmd) == 2:
            dll.arrive_vip(cmd[1])
            dll.show_line()

        elif action == "LEAVE" and len(cmd) == 2:
            dll.leave(cmd[1])
            dll.show_line()

        elif action == "SEAT":
            dll.seat()
            dll.show_line()

        elif action == "SHOW_LINE":
            dll.show_line()

        elif action == "EXIT":
            break

        else:
            print("Invalid command.")
            
if __name__ == "__main__":
    run_cli()
