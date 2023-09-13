import enum


class AutoNameEnum(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class OperationType(AutoNameEnum):
    sell = enum.auto()
    buy = enum.auto()
