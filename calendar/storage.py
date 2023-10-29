from typing import List

from model import Event


class StorageException(Exception):
    pass


class LocalCalendarStorage:
    def __init__(self):
        self._storage = {}

    def create(self, event: Event) -> str:
        if any(event.date == stored_event.date for stored_event in self._storage.values()):
            raise StorageException("Only one event is allowed per day")
        event.id = str(len(self._storage)+1)
        self._storage[event.id] = event
        return event.id

    def list(self) -> List[Event]:
        return list(self._storage.values())

    def read(self, event_id: str) -> Event:
        if event_id not in self._storage:
            raise StorageException(f"Event ID {event_id} not found in storage")
        return self._storage[event_id]

    def update(self, event_id: str, event: Event):
        if event_id not in self._storage:
            raise StorageException(f"Event ID {event_id} not found in storage")
        self._storage[event_id] = event

    def delete(self, event_id: str):
        if event_id not in self._storage:
            raise StorageException(f"Event ID {event_id} not found in storage")
        del self._storage[event_id]
