#!/bin/bash
cd src
# Run app mapping the port 8000 to the container
uvicorn main:app --port 8000 --host 0.0.0.0

