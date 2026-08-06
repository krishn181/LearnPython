from fastapi.testclient import TestClient
from myProject12 import app

client = TestClient(app)

#Test home api
def test_home_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello admin"}

def test_addition():
    response = client.get("/add?a=1&b=5")
    assert response.status_code == 200
    assert response.json() == {"result":6 }

# to run this open terminal and run "pytest"