import pandas as pd
import ast

def get_ast(source: str) -> ast.Module:
    try:
        tree = ast.parse(source)
    except:
        tree = None
    finally:
        return tree


def get_print_nodes(tree: ast.Module) -> list:
    collector = PrintCollector()
    collector.visit(tree)
    return collector.nodes


class PrintCollector(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []

    def visit_Call(self, node: ast.Call) -> None:
        if (isinstance(node.func, ast.Name) and node.func.id == "print"):
            self.nodes.append(node)

if __name__ == "__main__":
    print_frames = []
    text_frames = []
    for file in ["data/shome2023notebook/github-outputs.csv", "data/shome2023notebook/kaggle-outputs.csv"]:
        with pd.read_csv(
            file,
            header=None,
            names=["notebook", "source", "output_type", "text", "image", "has_html"],
            usecols=lambda x: x in ["notebook", "source", "output_type", "text"],
            engine="c",
            iterator=True,
        ) as reader:
            chunk = reader.get_chunk(100000)
            print(f"file: {file}, chunk: {chunk.shape}")
            chunk.loc[:, "ast"] = chunk["source"].apply(get_ast)
            chunk = chunk.loc[chunk["ast"].notna()]
            chunk = chunk.loc[
                chunk["ast"].map(lambda x: True if [node for node in ast.iter_child_nodes(x)] else False)
            ]

            prints = chunk.loc[chunk["output_type"] == "stream"]
            prints.loc[:, "print"] = prints.loc[:, "ast"].apply(get_print_nodes)
            prints = prints.explode("print")
            prints = prints.loc[prints["print"].notna()]
            prints.loc[:, "print"] = prints.loc[:, "print"].apply(lambda x: ast.unparse(x))
            print_frames.append(prints)

            texts = chunk.loc[chunk["output_type"] != "stream"]
            texts.loc[:, "last_node"] = texts.loc[:, "ast"].apply(lambda x: x.body[-1])
            texts.loc[:, "last_node"] = texts.loc[:, "last_node"].apply(lambda x: ast.unparse(x))
            text_frames.append(texts)


    prints = pd.concat(print_frames)
    texts = pd.concat(text_frames)

    prints = prints.drop_duplicates(subset=["print"])
    texts = texts.drop_duplicates(subset=["last_node"])

    prints.to_csv("data/shome2023notebook/output-prints.csv", columns=["notebook", "print", "text", "source"])
    texts.to_csv("data/shome2023notebook/output-texts.csv", columns=["notebook", "last_node", "text", "source"])
