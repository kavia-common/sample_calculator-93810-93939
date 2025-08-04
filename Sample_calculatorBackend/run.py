from app import app

if __name__ == "__main__":
    # Optionally use environment variables for host/port if desired
    import os
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", "5000"))
    app.run(host=host, port=port)
