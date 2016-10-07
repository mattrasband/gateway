import pytest


@pytest.fixture(autouse=True)
def patch_loop(loop, monkeypatch):
    monkeypatch.setattr('asyncio.get_event_loop', lambda: loop)

