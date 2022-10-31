from dataclasses import dataclass
from datetime import datetime

NOW = datetime.now()


@dataclass
class Promo:
    name: str
    expires: datetime

    @property
    def expired(self):
        return self.expires < NOW
