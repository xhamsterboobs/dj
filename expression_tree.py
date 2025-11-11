class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class ExpressionTree:
    def __init__(self):
        self.root = None

    # Check if the character is an operator
    def is_operator(self, c):
        return c in ['+', '-', '*', '/', '^']

    # Construct expression tree from prefix expression
    def construct_from_prefix(self, prefix):
        stack = []
        # Traverse from right to left
        for ch in prefix[::-1]:
            node = Node(ch)
            if self.is_operator(ch):
                # Pop two nodes for operator's left and right child
                node.left = stack.pop()
                node.right = stack.pop()
            stack.append(node)
        self.root = stack[-1]
        print("✅ Expression Tree constructed successfully.")

    # Non-recursive Postorder Traversal
    def postorder_non_recursive(self):
        if not self.root:
            print("⚠️ Tree is empty.")
            return

        stack1 = []
        stack2 = []

        stack1.append(self.root)
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        print("🌀 Postorder Traversal (Non-Recursive): ", end="")
        while stack2:
            print(stack2.pop().key, end=" ")
        print()

    # Delete the entire tree
    def delete_tree(self):
        self.root = None
        print("🗑️  Tree deleted successfully.")


# Menu-driven program
def main():
    tree = ExpressionTree()

    while True:
        print("\n========== EXPRESSION TREE MENU ==========")
        print("1. Construct Expression Tree (Prefix)")
        print("2. Display Postorder Traversal (Non-Recursive)")
        print("3. Delete Tree")
        print("4. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            prefix = input("Enter prefix expression: ")
            tree.construct_from_prefix(prefix)

        elif choice == '2':
            tree.postorder_non_recursive()

        elif choice == '3':
            tree.delete_tree()

        elif choice == '4':
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
