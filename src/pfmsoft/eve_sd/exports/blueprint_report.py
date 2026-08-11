from dataclasses import dataclass


@dataclass
class BlueprintActivity:
    name: str


@dataclass
class Blueprint:
    type_id: int
    name: str
    market_group_id: int | None
    published: bool
    manufacturing: BlueprintActivity | None
    copying: BlueprintActivity | None
    invention: BlueprintActivity | None
    # etc


_MarkdownReport = """# Blueprint Report
## _market_path_
"""
