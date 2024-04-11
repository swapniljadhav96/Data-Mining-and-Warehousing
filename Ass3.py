class TreeNode:
    def __init__(self, item, count, parent):
        self.item = item  # Item name
        self.count = count  # Count of occurrences of the item
        self.parent = parent  # Parent node
        self.children = {}  # Children nodes

def construct_fp_tree(transactions, min_support):
    # Step 1: Create the header table to store support counts for each item
    header_table = {}
    for transaction in transactions:
        for item in transaction:
            header_table[item] = header_table.get(item, 0) + 1

    # Remove items below min support
    header_table = {k: v for k, v in header_table.items() if v >= min_support}

    frequent_items = set(header_table.keys())

    # Step 2: Sort items by frequency, descending
    sorted_items = sorted(header_table.items(), key=lambda x: (-x[1], x[0]))

    # Step 3: Construct the FP-tree
    root = TreeNode("null", 0, None)
    for transaction in transactions:
        filtered_transaction = [item for item in transaction if item in frequent_items]
        filtered_transaction.sort(key=lambda x: (-header_table[x], x))
        current_node = root
        for item in filtered_transaction:
            if item in current_node.children:
                current_node.children[item].count += 1
            else:
                new_node = TreeNode(item, 1, current_node)
                current_node.children[item] = new_node
                # Update the node-link structure
                if header_table[item][1] is None:
                    header_table[item][1] = new_node
                else:
                    update_node_link(header_table[item][1], new_node)
            current_node = current_node.children[item]

    return root, header_table

def update_node_link(node_to_test, target_node):
    while node_to_test.nodeLink is not None:
        node_to_test = node_to_test.nodeLink
    node_to_test.nodeLink = target_node

def main():
    transactions = [
        {'A', 'B', 'D'},
        {'B', 'C', 'E'},
        {'A', 'B', 'D', 'E'},
        {'A', 'B', 'C', 'E'},
        {'A', 'B', 'C', 'D', 'E'},
        {'B', 'C', 'D'}
    ]
    min_support = 2

    root, header_table = construct_fp_tree(transactions, min_support)

    # Display the FP-tree
    display_fp_tree(root)

    # a) Find maximum frequent itemset.
    max_frequent_itemset = []
    for item in header_table:
        max_frequent_itemset.append([item])
        conditional_pattern_bases = find_prefix_path(header_table[item][1])
        conditional_fp_tree, _ = construct_fp_tree(conditional_pattern_bases, min_support)
        if len(conditional_fp_tree.children) > 0:
            max_frequent_itemset.extend(find_frequent_itemsets(conditional_fp_tree, []))

    print("Maximum frequent itemset:", max_frequent_itemset)

    # b) How many transactions does it contain?
    num_transactions = sum(header_table[item][0] for item in header_table)
    print("Number of transactions containing maximum frequent itemset:", num_transactions)

def find_prefix_path(base_node):
    conditional_pattern_bases = []
    while base_node is not None:
        prefix_path = []
        current_node = base_node
        while current_node.parent.item != "null":
            prefix_path.append(current_node.parent.item)
            current_node = current_node.parent
        if len(prefix_path) > 0:
            conditional_pattern_bases.append(prefix_path)
        base_node = base_node.nodeLink
    return conditional_pattern_bases

def find_frequent_itemsets(tree_node, prefix):
    frequent_itemsets = []
    for item in tree_node.children:
        new_prefix = prefix.copy()
        new_prefix.append(item)
        frequent_itemsets.append(new_prefix)
        if len(tree_node.children[item].children) > 0:
            frequent_itemsets.extend(find_frequent_itemsets(tree_node.children[item], new_prefix))
    return frequent_itemsets

def display_fp_tree(node, indent=0):
    print('  ' * indent + str(node.item) + ' ' + str(node.count))
    for child in node.children.values():
        display_fp_tree(child, indent + 1)

if __name__ == "__main__":
    main()
