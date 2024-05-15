from dataclasses import dataclass
import datetime
from typing import *

@dataclass
class DataSource:
    category: str
    youtube: str
    num: int
    date: datetime.date
    audio_to_speech: bool
    text: str

    @staticmethod
    def from_csv_entry(data: List[str]) -> Self:
        return DataSource(data[0], data[1], int(data[2]), datetime.datetime.strptime(data[3], "%Y%m%d").date(), bool(data[4]), data[5])

