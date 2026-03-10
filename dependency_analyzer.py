import networkx as nx
import re


def extract_imports(code):

    imports = []

    # Python imports
    imports += re.findall(r'import\s+(\w+)', code)
    imports += re.findall(r'from\s+(\w+)', code)

    # JS / TS imports
    imports += re.findall(r'import.*from\s+[\'"](.+)[\'"]', code)

    # C# using
    imports += re.findall(r'using\s+([\w\.]+)', code)

    # Java imports
    imports += re.findall(r'import\s+([\w\.]+)', code)

    return imports


def build_dependency_graph(files):

    graph = nx.DiGraph()

    for file_path, code in files.items():

        graph.add_node(file_path)

        imports = extract_imports(code)

        for imp in imports:
            graph.add_edge(file_path, imp)

    return graph


def detect_cycles(graph):

    try:
        cycles = list(nx.simple_cycles(graph))
        return cycles
    except:
        return []