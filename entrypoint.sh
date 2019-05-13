#!/bin/bash
 export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export PYTHONPATH=/app
cd audio_serve
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST="0.0.0.0"
flask run
