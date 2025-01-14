import json
import argparse
import pandas as pd
from io import StringIO
import os
import ast


class PrintCollector(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            self.nodes.append(node)


class AssertionNodeCollector(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []

    def visit_Assert(self, node: ast.Assert) -> None:
        self.nodes.append(node)

    def visit_Call(self, node: ast.Call) -> None:
        self.nodes.append(node)


class FunctionNameCollector(ast.NodeVisitor):
    def __init__(self):
        self.names = []

    def visit_Name(self, node: ast.Name) -> None:
        self.names.append(node.id)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        # capture function name if in module.func format
        self.names.append(node.attr)


def get_ast(source: str) -> ast.Module | None:
    try:
        tree = ast.parse(source)
    except:
        tree = None
    finally:
        return tree


def get_assertion_nodes(tree: ast.Module) -> list:
    collector = AssertionNodeCollector()
    collector.visit(tree)
    return collector.nodes


def get_print_nodes(tree: ast.Module) -> list:
    collector = PrintCollector()
    collector.visit(tree)
    return collector.nodes


def is_assertion_node(node):
    if isinstance(node, ast.Call):
        collector = FunctionNameCollector()
        collector.visit(node.func)
        return "assert" in "".join(collector.names)

    if isinstance(node, ast.Assert):
        return True


parser = argparse.ArgumentParser(
    description="Compute various statistics about Python assert statements in Jupyter Notebooks"
)
parser.add_argument(
    "notebook",
    help="Path to Jupyter Notebook",
)
args = parser.parse_args()
print(f"INPUT:{args.notebook}")

try:
    with open(args.notebook) as f:
        cells = json.load(f)["cells"]
        df = pd.read_json(StringIO(json.dumps(cells)), orient="records")
        df = df.loc[df["cell_type"] == "code"]
        # NOTE: remove empty cells
        # These can be of three types: NaN (float) "" (str) or [] (list)
        df = df.loc[df["source"].notna()]  # handle NaN
        df = df.loc[df["source"].map(lambda x: bool(x))]  # handle empty "" or []
except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
    print(f"An error occured: {e}")
    df = pd.DataFrame()

# NOTE: early exit if invalid JSON or no code cells in notebook
df.empty and exit()

# NOTE: convert `source` to str dtype
# NOTE: `source` can be str or list; following lambda function works on both cases
df.loc[:, "source"] = df["source"].apply(lambda x: "".join(x))

import_cells = df.loc[df["source"].str.contains("import")]
(
    import_cells.empty
    or import_cells.loc[
        import_cells["source"].str.contains(
            r"sklearn|torch|tensorflow|keras", regex=True
        )
    ].empty
) and exit()

# NOTE: create AST from source, remove cells with empty ASTs
df.loc[:, "ast"] = df["source"].apply(get_ast)
df = df.loc[df["ast"].notna()]
df = df.loc[df["ast"].map(lambda x: bool([node for node in ast.iter_child_nodes(x)]))]

asserts = df.loc[:, ["ast"]]
asserts.loc[:, "assert"] = asserts.loc[:, "ast"].apply(get_assertion_nodes)
asserts = asserts.explode("assert")
asserts = asserts.loc[asserts["assert"].notna()]
asserts = asserts.loc[asserts["assert"].map(lambda x: is_assertion_node(x))]
asserts.loc[:, "assert"] = asserts.loc[:, "assert"].map(lambda x: ast.unparse(x))

prints = df.loc[:, ["ast"]]
prints.loc[:, "print"] = prints.loc[:, "ast"].apply(get_print_nodes)
prints = prints.explode("print")
prints = prints.loc[prints["print"].notna()]
prints.loc[:, "print"] = prints.loc[:, "print"].map(lambda x: ast.unparse(x))

# NOTE: this will contain duplicate of prints that are also the last statement
lasts = df.loc[:, ["ast", "outputs"]]

# NOTE: remove cells with no outputs
# These can be of two type: NaN (float) or [] (list)
lasts = lasts.loc[lasts["outputs"].notna()]  # handle NaN
lasts = lasts.loc[lasts["outputs"].apply(lambda x: bool(x))]  # handle empty []

# NOTE: only keep cells with execute_results output type
lasts = lasts.loc[
    lasts["outputs"].map(
        lambda x: "execute_result" in [output["output_type"] for output in x]
    )
]
lasts.loc[:, "last"] = lasts.loc[:, "ast"].apply(lambda x: x.body[-1])
lasts.loc[:, "last"] = lasts.loc[:, "last"].map(lambda x: ast.unparse(x))

dirname, filename = os.path.split(args.notebook)
dirname = dirname.replace("data/", "data/shome2023notebook/", 1)
if not os.path.exists(dirname):
    os.makedirs(dirname)

name = os.path.join(dirname, os.path.splitext(filename)[0] + "-stats.csv")
pd.DataFrame(
    {
        "notebook": [args.notebook],
        "num_cells": [len(df)]
    }
).to_csv(name, header=False)
print(f"OUTPUT: {name}")

if not asserts.empty:
    asserts.loc[:, "notebook"] = args.notebook
    name = os.path.join(dirname, os.path.splitext(filename)[0] + "-asserts.csv")
    asserts.to_csv(name, header=False, columns=["notebook", "assert"])
    print(f"OUTPUT:{name}")

if not prints.empty:
    prints.loc[:, "notebook"] = args.notebook
    name = os.path.join(dirname, os.path.splitext(filename)[0] + "-prints.csv")
    prints.to_csv(name, header=False, columns=["notebook", "print"])
    print(f"OUTPUT:{name}")

if not lasts.empty:
    lasts.loc[:, "notebook"] = args.notebook
    name = os.path.join(dirname, os.path.splitext(filename)[0] + "-lasts.csv")
    lasts.to_csv(name, header=False, columns=["notebook", "last"])
    print(f"OUTPUT:{name}")
