from .base import Resource


def coerce_from_str(cls: Resource) -> callable:
    def _coerce(name_or_resource):
        if isinstance(name_or_resource, str):
            return cls(name=name_or_resource, stub=True)
        else:
            return name_or_resource

    return _coerce


def listify(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]
