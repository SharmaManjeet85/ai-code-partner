from tree_sitter_language_pack import get_parser


def get_language(file_path):

    if file_path.endswith(".py"):
        return "python"

    if file_path.endswith(".js"):
        return "javascript"

    if file_path.endswith(".ts"):
        return "typescript"

    if file_path.endswith(".java"):
        return "java"

    if file_path.endswith(".cs"):
        return "c_sharp"

    if file_path.endswith(".go"):
        return "go"

    if file_path.endswith(".cpp") or file_path.endswith(".cc"):
        return "cpp"

    return None


def extract_structure(file_path, code):

    language = get_language(file_path)

    if language is None:
        return {"classes": [], "methods": []}

    try:
        parser = get_parser(language)
    except:
        return {"classes": [], "methods": []}

    tree = parser.parse(bytes(code, "utf8"))
    root = tree.root_node

    classes = []
    methods = []

    def walk(node):

        # class nodes vary by language
        if node.type in ["class_definition", "class_declaration"]:
            name_node = node.child_by_field_name("name")
            if name_node:
                classes.append(code[name_node.start_byte:name_node.end_byte])

        # function nodes vary by language
        if node.type in [
            "function_definition",
            "method_definition",
            "function_declaration"
        ]:
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