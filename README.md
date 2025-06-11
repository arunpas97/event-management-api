
Event Management API

This repository contains an Event Management API built with Django and Django REST Framework. It allows users to create events, register attendees, and retrieve event and attendee details. 

Table of Contents
1. [Setup Instructions](#setup-instructions)
2. [Assumptions](#assumptions)
3. [API Endpoints](#api-endpoints)
   - [Create Event](#create-event)
   - [List Events](#list-events)
   - [Register Attendee](#register-attendee)
   - [List Attendees for an Event](#list-attendees-for-an-event)
4. [Sample API Requests](#sample-api-requests)

---

Setup Instructions

Prerequisites
- Python 3.10+
- Django 4.x
- PostgreSQL (or any preferred database)
- Virtual Environment (recommended)

Steps
1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api

2. Create a Virtual Environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply Migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the Development Server:

   ```bash
   python manage.py runserver
   ```

6. Access the API:
   Visit `http://127.0.0.1:8000/api/` in your browser or API client.

---

## Assumptions

1. **Timezones**:

   * All events are stored as timezone-aware datetime objects.
   * Clients can specify their timezone to view event times.

2. **Duplicate Registration**:

   * An attendee cannot register twice for the same event.

3. **Capacity Validation**:

   * Attendees cannot register if the event capacity is reached.

4. **Pagination**:

   * Attendee lists are paginated with a default limit of 10 per page.

5. **Error Handling**:

   * Meaningful error messages are returned for validation failures and exceptions.

---

## API Endpoints

### 1. Create Event

**POST** `/api/events/`

* **Body**:

  ```json
  {
    "name": "Tech Conference 2025",
    "location": "Virtual",
    "start_time": "2025-07-10, 10:00 AM",
    "end_time": "2025-07-10, 03:00 PM",
    "max_capacity": 100
  }
  ```
* **Response**:

  ```json
  {
    "id": 1,
    "name": "Tech Conference 2025",
    "location": "Virtual",
    "start_time": "2025-07-10, 10:00 AM",
    "end_time": "2025-07-10, 03:00 PM",
    "max_capacity": 100
  }
  ```

---

### 2. List Events

**GET** `/api/events/`

* **Query Params** (Optional):

  * `timezone`: Adjust event times to the specified timezone (default: UTC).
* **Response**:

  ```json
  [
    {
      "id": 1,
      "name": "Tech Conference 2025",
      "location": "Virtual",
      "start_time": "2025-07-10, 10:00 AM",
      "end_time": "2025-07-10, 03:00 PM",
      "max_capacity": 100
    }
  ]
  ```

---

### 3. Register Attendee

**POST** `/api/events/<event_id>/register/`

* **Body**:

  ```json
  {
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
  ```
* **Response**:

  ```json
  {
    "id": 1,
    "event": 1,
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
  ```

---

### 4. List Attendees for an Event

**GET** `/api/events/<event_id>/attendees/`

* **Response**:

  ```json
  {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": 1,
        "event": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
      }
    ]
  }
  ```

---

## Sample API Requests

### Using cURL

1. **Create Event**:

   ```bash
   curl -X POST http://127.0.0.1:8000/api/events/ \
   -H "Content-Type: application/json" \
   -d '{"name": "Tech Conference 2025", "location": "Virtual", "start_time": "2025-07-10, 10:00 AM", "end_time": "2025-07-10, 03:00 PM", "max_capacity": 100}'
   ```

2. **List Events**:

   ```bash
   curl -X GET http://127.0.0.1:8000/api/events/
   ```

3. **Register Attendee**:

   ```bash
   curl -X POST http://127.0.0.1:8000/api/events/1/register/ \
   -H "Content-Type: application/json" \
   -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}'
   ```

4. **List Attendees**:

   ```bash
   curl -X GET http://127.0.0.1:8000/api/events/1/attendees/
   ```
