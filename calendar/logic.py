from typing import List
from model import Event
from storage import LocalCalendarStorage, StorageException

TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class EventLogic:
    def __init__(self):
        self._calendar_storage = LocalCalendarStorage()

    @staticmethod
    def _validate_event(event: Event):
        if len(event.title) > TITLE_LIMIT:
            raise LogicException(f"Title length > MAX: {TITLE_LIMIT}")
        if len(event.text) > TEXT_LIMIT:
            raise LogicException(f"Text length > MAX: {TEXT_LIMIT}")

    def create(self, event: Event) -> str:
        self._validate_event(event)
        try:
            return self._calendar_storage.create(event)
        except StorageException as ex:
            raise LogicException(f"Failed to create event: {ex}")

    def list(self) -> List[Event]:
        try:
            return self._calendar_storage.list()
        except StorageException as ex:
            raise LogicException(f"Failed to list events: {ex}")

    def read(self, event_id: str) -> Event:
        try:
            return self._calendar_storage.read(event_id)
        except StorageException as ex:
            raise LogicException(f"Failed to read event: {ex}")

    def update(self, event_id: str, event: Event):
        self._validate_event(event)
        try:
            self._calendar_storage.update(event_id, event)
        except StorageException as ex:
            raise LogicException(f"Failed to update event: {ex}")

    def delete(self, event_id: str):
        try:
            self._calendar_storage.delete(event_id)
        except StorageException as ex:
            raise LogicException(f"Failed to delete event: {ex}")
