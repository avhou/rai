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
        return DataSource(data[0], data[1], int(data[2]), datetime.datetime.strptime(data[3], "%Y%m%d").date(), True if data[4] == "True" else False, data[5])

