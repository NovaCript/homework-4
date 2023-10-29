from flask import Flask, request
from model import Event
from logic import EventLogic

app = Flask(__name__)

_calendar_logic = EventLogic()


@app.route("/api/v1/calendar/", methods=["POST"])
def create_event():
    try:
        data = request.get_data().decode('utf-8')
        date, title, text = data.split('|')
        event = Event(None, date, title, text)
        event_id = _calendar_logic.create(event)
        return f"New event ID: {event_id}", 201
    except Exception as ex:
        return f"Failed to create event: {ex}", 404


@app.route("/api/v1/calendar/", methods=["GET"])
def list_events():
    try:
        events = _calendar_logic.list()
        event_data = ""
        for event in events:
            event_data += f"{event.date}|{event.title}|{event.text}\n"
        return event_data, 200
    except Exception as ex:
        return f"Failed to list events: {ex}", 404


@app.route("/api/v1/calendar/<event_id>/", methods=["GET"])
def read_event(event_id):
    try:
        event = _calendar_logic.read(event_id)
        event_data = f"{event.date}|{event.title}|{event.text}"
        return event_data, 200
    except Exception as ex:
        return f"Failed to read event: {ex}", 404


@app.route("/api/v1/calendar/<event_id>/", methods=["PUT"])
def update_event(event_id):
    try:
        data = request.get_data().decode('utf-8')
        date, title, text = data.split('|')
        event = Event(event_id, date, title, text)
        _calendar_logic.update(event_id, event)
        return "Event updated", 200
    except Exception as ex:
        return f"Failed to update event: {ex}", 404


@app.route("/api/v1/calendar/<event_id>/", methods=["DELETE"])
def delete_event(event_id):
    try:
        _calendar_logic.delete(event_id)
        return "Event deleted", 200
    except Exception as ex:
        return f"Failed to delete event: {ex}", 404
