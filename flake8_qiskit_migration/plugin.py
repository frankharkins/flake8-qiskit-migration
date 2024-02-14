from __future__ import annotations

import ast
from dataclasses import dataclass
import importlib.metadata

from .deprecated_paths import DEPRECATED_PATHS, EXCEPTIONS


def deprecation_message(path: str, original_import_path: str | None = None) -> str | None:
    """
    Build deprecation message from `DEPRECATED_PATHS` dict.

    Args:
        path (str): Python import path of the form `qiskit.extensions.thing`

    Returns:
        str: Deprecation message if path is deprecated
        None: If no deprecations detected
    """
    original_import_path = original_import_path or path
    if "." not in path:
        return None
    if path in EXCEPTIONS:
        return None
    if path not in DEPRECATED_PATHS:
        parent = ".".join(path.split(".")[:-1])
        return deprecation_message(parent, original_import_path)
    return f"QKT100: " + DEPRECATED_PATHS[path].format(original_import_path)


class Visitor(ast.NodeVisitor):
    """
    Simple visitor to detect deprecated imports. Includes some support for
    aliases and scopes, but not assignments.
    """

    def __init__(self):
        self.problems: list[Problem] = []
        self.mappings: list[dict[str, str]] = [{}]  # track aliases for each scope

    def enter_scope(self) -> None:
        """Add new mapping for scoped aliases"""
        self.mappings.append({})

    def exit_scope(self) -> None:
        """Delete scoped aliases"""
        self.mappings.pop()

    def add_alias(self, alias: ast.alias) -> None:
        if alias.asname is None or alias.asname == alias.name:
            return
        self.mappings[-1][alias.asname] = alias.name

    def resolve_aliases(self, name: str) -> str:
        for mapping in reversed(self.mappings):
            name = mapping.get(name, name)
        return name

    def report_if_deprecated(self, path: str, node) -> bool:
        """
        Adds path to problems if deprecated, ignores otherwise
        Returns True if problem was reported
        """
        msg = deprecation_message(path)
        if msg is not None:
            self.problems.append(Problem(node, msg))
            return True
        return False

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.add_alias(alias)
            self.report_if_deprecated(alias.name, node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for alias in node.names:
            self.add_alias(alias)
            path = f"{node.module}.{alias.name}"
            self.report_if_deprecated(path, node)
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        def _get_parents(node):
            if isinstance(node, ast.Name):
                return node.id
            if isinstance(node, ast.Attribute):
                parents = _get_parents(node.value)
                parents = self.resolve_aliases(parents)
                return f"{parents}.{node.attr}"

        path = _get_parents(node)
        if not self.report_if_deprecated(path, node):
            self.generic_visit(node)

    # Push / pop scopes for aliases
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.enter_scope()
        self.generic_visit(node)
        self.exit_scope()

    def visit_AsyncFunctionDef(self, node: ast.FunctionDef):
        self.enter_scope()
        self.generic_visit(node)
        self.exit_scope()

    def visit_ClassDef(self, node: ast.FunctionDef):
        self.enter_scope()
        self.generic_visit(node)
        self.exit_scope()


class Plugin:
    name = "flake8_qiskit_migration"
    version = importlib.metadata.version("flake8_qiskit_migration")

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self):
        """
        Yields:
            int: Line number of problem
            int: Character number of problem
            str: Message for user
           Type: (unused)
        """
        v = Visitor()
        v.visit(self._tree)
        for problem in v.problems:
            yield problem.format()


@dataclass
class Problem:
    node: ast.AST
    msg: str

    def format(self):
        return (self.node.lineno, self.node.col_offset, self.msg, None)
