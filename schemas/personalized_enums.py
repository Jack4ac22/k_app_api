import enum


class Genders_person(enum.Enum):
    male = 'male'
    female = 'female'


class Task_status(enum.Enum):
    open = 'open'
    close = 'close'
    standby = 'standby'
