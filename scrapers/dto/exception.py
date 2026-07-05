from pydantic import BaseModel
from datetime import datetime

class ExceptionModel(BaseModel):
    error: str
    consult_date: str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def to_dict(self):
        return self.model_dump()