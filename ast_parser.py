from tree_sitter_language_pack import get_parser
# choose parser (python for now)
parser = get_parser("python")


def extract_structure(code):

    tree = parser.parse(bytes(code, "utf8"))
    root = tree.root_node

    classes = []
    methods = []

    def walk(node):

        if node.type == "class_definition":
            name_node = node.child_by_field_name("name")
            if name_node:
                classes.append(code[name_node.start_byte:name_node.end_byte])

        if node.type == "function_definition":
            name_node = node.child_by_field_name("name")
            if name_node:
                methods.append(code[name_node.start_byte:name_node.end_byte])

        for child in node.children:
            walk(child)

    walk(root)

    return {
        "classes": classes,
        "methods": methods
    }