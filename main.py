from node import node

def reverse_string(s):
    temp = []
    for i in range(len(s)-1, -1, -1):
        temp.append(s[i])    
    return ''.join(temp)

def apply_rule1(tree, parent_index, inp, out):
    s = tree[parent_index].val
    s = s.replace(inp, out)
    tree.append(node(s, 1, parent_index))

def apply_rule2(tree, parent_index, inp, out):
    s = tree[parent_index].val
    s = s.replace(inp, out)
    tree.append(node(s, 2, parent_index))
    
def apply_rule3(tree, parent_index, inp, out):
    s = tree[parent_index].val
    s = s.replace(inp, out)
    tree.append(node(s, 3, parent_index))

def print_tree(tree):
    for i in range(len(tree)):
        print(tree[i])

def find_sequence(tree, i):
    node = tree[i]
    to_ret = ""
    while (node.parent != -1):
        to_ret += str(node.rule)
        node = tree[node.parent]
    return reverse_string(to_ret)

if __name__=='__main__':
    axiom = "aab"
    theorem = "cacacb"
    in1 = "a"
    out1 = "c"
    in2 = "c"
    out2 = "ac"
    in3 = "cc"
    out3 = "ca"

    tree = []
    first = node(axiom, 0, -1)
    tree.append(first)
    i = 0
    current_node = tree[0]
    while(current_node.val != theorem):
        apply_rule1(tree, i, in1, out1)
        apply_rule2(tree, i, in2, out2)
        apply_rule3(tree, i, in3, out3)
        i += 1
        current_node = tree[i]
    seq = find_sequence(tree, i)
    print(seq)
