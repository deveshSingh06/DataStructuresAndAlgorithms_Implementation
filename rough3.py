# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.children = []
#         self.parent = None
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level
#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 2
#         prefix = spaces + "|__ " if self.parent else ''
#         print(prefix + self.value)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()
#
#
# if __name__ == "__main__":
#     root = TreeNode("NSUT")
#     courses = TreeNode("Courses")
#
#     mtech = TreeNode("M.Tech")
#     mtech.add_child(TreeNode("CSE"))
#     mtech.add_child(TreeNode("IT"))
#     mtech.add_child(TreeNode("ICE"))
#     mtech.add_child(TreeNode("ECE"))
#     mtech.add_child(TreeNode("EE"))
#
#     btech = TreeNode("B.Tech")
#     btech.add_child(TreeNode("CSE"))
#     btech.add_child(TreeNode("IT"))
#     btech.add_child(TreeNode("ICE"))
#     btech.add_child(TreeNode("ECE"))
#     btech.add_child(TreeNode("EE"))
#
#     courses.add_child(mtech)
#     courses.add_child(btech)
#     root.add_child(courses)
#     root.print_tree()


class TreeNode:
    def __init__(self, data):
        self.value = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__ " if self.parent else ''
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()


root = TreeNode('Processors')

intel = TreeNode('Intel')
intel.add_child(TreeNode('i3'))
intel.add_child(TreeNode('i5'))
intel.add_child(TreeNode('i7'))
intel.add_child(TreeNode('i9'))

amd = TreeNode('AMD')
amd.add_child(TreeNode('Ryzen 3'))
amd.add_child(TreeNode('Ryzen 5'))
amd.add_child(TreeNode('Ryzen 7'))
amd.add_child(TreeNode('Ryzen 9'))

root.add_child(intel)
root.add_child(amd)
root.print_tree()