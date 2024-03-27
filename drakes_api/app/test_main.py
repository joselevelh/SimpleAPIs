from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_system_check():
    response = client.get("/syscheck")
    assert response.status_code == 200
    assert response.json() == True


def test_get_lookbook():
    response = client.get("/lookbooks/paris")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["lookbook_name"] == "autumn-in-paris-lookbook"


def test_get_lookbooks_any():
    response = client.get("/lookbooks/any/?tags=2017")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    assert response.json()[0]["tags"] == [
                                          "spring-summer",
                                          "2017",
                                          "casual",
                                          "menswear"]

# TODO: Add tests for empty and invalid lookbooks
