class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        parent = self._find(self.root, parent_name)
        if not parent:
            print(f"Parent {parent_name} not found.")
            return

        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(child_name)
            else:
                print("Left child already exists.")
        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(child_name)
            else:
                print("Right child already exists.")
        else:
            print("Side must be 'left' or 'right'.")

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        return self._find(node.left, name) or self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []
        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []
        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

### A tree is a good data structure for the doctor reporting system because it shows a clear hierarchy. In a hospital, doctors usually report to a specific supervisor, and that creates a parent and child relationship. A binary tree works well because each doctor can have a limited number of direct reports. Using a tree also makes it easy to move through the structure using recursion and see how doctors are connected.Different tree traversals are useful for different situations. Preorder traversal is helpful when the supervisor needs to be handled before their team, such as when giving instructions from the top down. Inorder traversal is useful for displaying doctors in a structured and readable order. Postorder traversal is best when the child doctors should be handled before the supervisor, such as when reviewing work or removing doctors from the structure safely.A heap is useful for the emergency room system because it always keeps the most urgent patient at the front. In an emergency room, patients are not treated in the order they arrive, but by how serious their condition is. A min-heap makes sure the patient with the lowest urgency number, meaning the most urgent case, is always treated first. Insertions and removals are fast, which is important in real-time situations where new patients arrive constantly. This makes the heap a good choice for managing emergency patient intake.