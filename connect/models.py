from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int | None = None
    gender: str
    id_num: int | None = None
    animal: str
    food: str
    subject: str
    hobby: str
    flower: str
    person: str



