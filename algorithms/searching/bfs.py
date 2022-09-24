"""
BFS or Breadth First Search
is a traversal algorithm for a tree or graph,
where we start from the root node(for a tree)
And visit all the nodes level by level from left to right.
It requires us to keep track of the children of each node we visit
In a queue, so that after traversal through a level is complete,
our algorithm knows which node to visit next.
Time complexity     -   O(n)
Space complexity    -   O(n)
To implement BFS, we'll need a Binary Search Tree, which we have already coded. So we'll use that.
"""

# use Queue I have already coded using linked list
from data_structures.stacks_queues.queue_impl_linked_list import Queue


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)


class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.traverse(self.root))

    def traverse(self, node):
        if node:
            tree = {"value": node.value if node else "null",
                    "left": self.traverse(node.left) if node.left else "null",
                    "right": self.traverse(node.right) if node.right else "null"}
            return tree

    def insert(self, value):
        # check input
        node = Node(value)
        if not self.root:
            self.root = node
            return
        cur_node = self.root
        while cur_node:
            # left
            if value < cur_node.value:
                if not cur_node.left:
                    cur_node.left = node
                    return
                cur_node = cur_node.left
            # right
            elif value > cur_node.value:
                if not cur_node.right:
                    cur_node.right = node
                    return
                cur_node = cur_node.right
            # duplicate
            else:
                print("Duplicate value")
                return

    def lookup(self, value):
        if not self.root:
            print("Tree is empty")
        cur_node = self.root
        while cur_node:
            if value == cur_node.value:
                return cur_node
            if value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return None

    def remove(self, value):
        # check if tree is empty
        if not self.root:
            print("tree is empty")
            return
        # find current node for deleting and his parent
        cur_node, parent = self._search(value)
        # check cur_node and parent for None
        if cur_node:
            print(cur_node.value, end=" ")
        if parent:
            print(parent.value)
        if not cur_node:
            print(f"node {value} is not in the tree")
            return
        if not parent:
            print(f"node {value} is root node")

        # if cur_node is a leaf
        if self.is_leaf(cur_node):
            # check if cur_node is root
            if not parent:
                self.root = None
                print(f"node {value} is root node")
            # cur_node isn't a root node
            else:
                # delete cur_node
                self._delete(cur_node, parent)
            print(f"node {value} is deleted")

        # if cur_node has only one child
        elif self.has_one_child(cur_node):
            self.bypass(cur_node, parent)
            print(f"node {value} is deleted")
        # if cur_node has 2 children
        else:
            successor, suc_parent = self._find_successor(cur_node)
            self._replace(cur_node, parent, successor, suc_parent)
            print(f"node {value} is deleted")

    def _search(self, value):
        if not self.root:
            return None, None
        cur_node = self.root
        parent = None
        while cur_node:
            if value == cur_node.value:
                return cur_node, parent
            else:
                parent = cur_node
                if value < cur_node.value:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right
        return None, None

    def is_leaf(self, node):
        if node.left or node.right:
            return False
        return True

    def _delete(self, cur_node, parent):
        if cur_node and parent:
            # cur_node is a left child
            if parent.left == cur_node:
                parent.left = None
            # cur_node is a right child
            else:
                parent.right = None

    def has_one_child(self, node):
        if node.left and node.right:
            return False
        if self.is_leaf(node):
            return False
        return True

    def bypass(self, cur_node, parent):
        # current node has left child
        if cur_node.left:
            # save left child of cur_node to new_node
            new_node = cur_node.left
        # current node has right child
        else:
            # save right child of cur_node to new_node
            new_node = cur_node.right
        # then new_node will contain link to cur_node's child
        # check if cur_node ia a root
        if not parent:
                self.root = new_node
        else:
            # current node is left child
            if parent.left == cur_node:
                parent.left = new_node
            # current node is right child
            else:
                parent.right = new_node

    def _find_successor(self, node):
        successor = node.right
        suc_parent = node
        while successor.left:
            suc_parent = successor
            successor = successor.left
        return successor, suc_parent

    def _replace(self, cur_node, parent, successor, suc_parent):
        print(f"cur_node = {cur_node.value} parent = {parent.value} successor = {successor.value}"
              f" suc_parent = {suc_parent.value}")
        # link cur_node's left child instead of successor's left child
        successor.left = cur_node.left
        # if cur_node's right child is not a successor
        if cur_node.right != successor:
            # then link cur_node's right child instead of successor's right child
            successor.right = cur_node.right
            # delete link from successor's parent to successor (left child)
            suc_parent.left = None
        # check if cur_node is a root
        if not parent:
            self.root = successor
        # link from parent to successor
        if parent.left == cur_node:
            parent.left = successor
        else:
            parent.right = successor
        print(f"parent = {parent.value} parent.left = {parent.left.value} parent.right = {parent.right.value}")
        print(f"parent.left.left = {parent.left.left.value}")

    def breadth_first_search(self):
        cur_node = self.root
        # check if tree is empty
        if not cur_node:
            return None
        search_lst = []
        # queue = []
        # better use my implementation of Queue instead of using list
        # because list is not efficient to remove element from the beginning
        queue = Queue()
        # add the root to the queue first
        queue.enqueue(cur_node)

        # in loop check if queue is not empty
        while queue.length > 0:
            # and extract the first element of the queue and make it the current node
            cur_node = queue.dequeue()
            # add value of the current node to the result list as it is currently visited
            search_lst.append(cur_node.value)
            # if left child of the current node exists, than add it to the queue
            if cur_node.left:
                queue.enqueue(cur_node.left)
            # if right child of the current node exists, than add it to the queue
            if cur_node.right:
                queue.enqueue(cur_node.right)

        return search_lst

    def breadth_first_search_recursive(self):
        queue = Queue()
        queue.enqueue(self.root)
        return self.bfs_rec(queue, [])

    def bfs_rec(self, queue, search_lst):
        # base case for recursion
        # check if queue is empty
        if queue.length == 0:
            return search_lst
        # extract the first element of the queue and make it the current node
        cur_node = queue.dequeue()
        # add value of the current node to the result list as it is currently visited
        search_lst.append(cur_node.value)
        # if left child of the current node exists, than add it to the queue
        if cur_node.left:
            queue.enqueue(cur_node.left)
        # if right child of the current node exists, than add it to the queue
        if cur_node.right:
            queue.enqueue(cur_node.right)
        return self.bfs_rec(queue, search_lst)



if __name__ == "__main__":
    my_tree = BST()
    print(my_tree)
    my_tree.insert(9)
    print(my_tree)
    my_tree.insert(4)
    print(my_tree)
    my_tree.insert(6)
    my_tree.insert(20)
    my_tree.insert(170)
    my_tree.insert(15)
    my_tree.insert(1)
    my_tree.insert(5)
    my_tree.insert(7)

    print(my_tree)
    print(my_tree.traverse(my_tree.root))
    # BFS
    print(my_tree.breadth_first_search())
    # BFS recursive
    print(my_tree.breadth_first_search_recursive())

