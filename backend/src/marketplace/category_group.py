# for recursive dataclass
from __future__ import annotations

from copy import copy
from functools import lru_cache

import yaml
from attr import dataclass
from cms import settings
from mashumaro import DataClassDictMixin
from yaml import SafeLoader


@dataclass
class CategoryGroup(DataClassDictMixin):
    name: str
    ru: str


@dataclass
class CategoryGroupNode(CategoryGroup):
    child: list[CategoryGroupNode] = []


def _load() -> list[CategoryGroupNode]:
    with open(settings.CATEGORY_GROUP_FIXTURE) as f:
        data = yaml.load(f, Loader=SafeLoader)
        return [CategoryGroupNode.from_dict(d) for d in data]


@lru_cache()
def group_paths() -> dict[str, list[CategoryGroup]]:
    paths: dict[str, list[CategoryGroup]] = dict()
    for g in _load():
        paths.update(_collect_group_paths(g, []))

    return paths


def _collect_group_paths(group: CategoryGroupNode, node_path: list[CategoryGroup]) -> dict[str, list[CategoryGroup]]:
    node_path = copy(node_path)
    node_path.append(CategoryGroup(name=group.name, ru=group.ru))

    paths: dict[str, list[CategoryGroup]] = {
        group.name: node_path
    }

    for g in group.child:
        paths.update(_collect_group_paths(g, node_path))

    return paths


def group_path(name) -> list[CategoryGroup]:
    return group_paths()[name]
