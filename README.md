# BirthDayManager
App for managing birthdays. Based on flask

Pointers
   1. Using get request create token
    `http://127.0.0.1:5000/authenticate`
    JSON data for username and password.   
   2. Using get request with token to process data
    `http://127.0.0.1:5000/auth/username/process-data`
    Header: Authentication Bearer jwt-token
    Body: 
    - `{"type": "READ", "payload": {"name": "gupeh"}}`
    - `{"type": "DELETE", "payload": {"name": "gupeh"}}`
    - `{"type": "INSERT", "payload": {"name": "gupeh","birthday":"02-11""}}`
