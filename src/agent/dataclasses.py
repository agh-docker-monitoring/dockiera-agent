import enum
from dataclasses import dataclass
from datetime import datetime
from typing import List

from dataclasses_json import LetterCase, dataclass_json


class MetricType(enum.Enum):
    memory_usage = "MEMORY_USAGE"
    disk_usage = "DISK_USAGE"
    cpu_usage = "CPU_USAGE"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BasicMetric:
    metric_type: MetricType
    value: float
    total: float
    percent: float


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ContainerSummary:
    id: str
    name: str
    image: str
    status: str
    metrics: List[BasicMetric]


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class HostSummary:
    id: str
    timestamp: datetime
    metrics: List[BasicMetric]
    containers: List[ContainerSummary]
