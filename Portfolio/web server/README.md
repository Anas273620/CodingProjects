# Portfolio Web Server (Flask)

A simple Flask web server for a personal portfolio website with contact form capture.

## Features

- Home and dynamic page routing
- Contact form endpoint (`/submit_form`)
- Submission persistence to `database.csv`

## Project Files

- `server.py` — Flask routes and form processing
- `database.csv` — captured form submissions
- `requirements.txt` — Python dependencies

## Run Locally

```bash
cd "Portfolio/web server"
pip install -r requirements.txt
python server.py
```

Then open `http://127.0.0.1:5000`.

## Notes

- Form submissions are appended to `database.csv`.
- This is a learning/portfolio project and can be extended with validation and production config.
