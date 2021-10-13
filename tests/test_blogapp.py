from blogapp import __version__
from blogapp.app import app

app.testing = True
client = app.test_client()


def test_version():
    assert __version__ == "0.1.0"
