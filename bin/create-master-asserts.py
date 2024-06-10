import pandas as pd
import ast


def get_ast(source: str) -> ast.Module:
    try:
        tree = ast.parse(source)
    except:
        tree = None
    finally:
        return tree


def get_assert_nodes(tree: ast.Module) -> list[ast.Assert]:
    collector = AssertCollector()
    collector.visit(tree)
    return collector.nodes


class AssertCollector(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []

    def visit_Assert(self, node: ast.Assert) -> None:
        self.nodes.append(node)


if __name__ == "__main__":
    github = pd.read_csv(
        "data/shome2023notebook/github-assert-content.csv",
        header=None,
        names=["cell_type", "source", "notebook"],
    )

    kaggle = pd.read_csv(
        "data/shome2023notebook/quaranta2021kgtorrent-assert-content.csv",
        header=None,
        names=["cell_type", "source", "notebook"],
    )

    asserts = pd.concat([github, kaggle])

    asserts.loc[:, "ast"] = asserts["source"].apply(get_ast)
    asserts = asserts.loc[asserts["ast"].notna()]
    asserts = asserts.loc[
        asserts["ast"].map(lambda x: True if list(ast.walk(x)) else False)
    ]
    asserts.loc[:, "assert"] = asserts.loc[:, "ast"].apply(get_assert_nodes)
    asserts = asserts.explode("assert")
    asserts = asserts.loc[asserts["assert"].notna()]
    asserts.loc[:, "assert"] = asserts.loc[:, "assert"].apply(lambda x: ast.unparse(x))
    asserts = asserts.drop_duplicates(subset=["assert"])

    asserts.to_csv("data/shome2023notebook/assert-content.csv", columns=["notebook", "assert", "source"])
