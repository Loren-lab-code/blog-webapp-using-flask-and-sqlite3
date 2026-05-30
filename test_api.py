import pytest
from app import app, db, Category

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Disconnects regular DB
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

# --- POSITIVE TESTS ---
def test_create_category_success(client):
    response = client.post('/api/categories', json={'name': 'Tech', 'description': 'Gadgets'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'Tech'

def test_get_categories_success(client):
    client.post('/api/categories', json={'name': 'Lifestyle'})
    response = client.get('/api/categories')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_update_category_success(client):
    res = client.post('/api/categories', json={'name': 'Old Title'})
    cat_id = res.get_json()['id']
    response = client.put(f'/api/categories/{cat_id}', json={'name': 'New Title'})
    assert response.status_code == 200
    assert response.get_json()['name'] == 'New Title'

def test_delete_category_success(client):
    res = client.post('/api/categories', json={'name': 'Trash'})
    cat_id = res.get_json()['id']
    response = client.delete(f'/api/categories/{cat_id}')
    assert response.status_code == 200

# --- NEGATIVE TESTS (Error Handling) ---
def test_create_category_missing_fields(client):
    response = client.post('/api/categories', json={'description': 'No Name'})
    assert response.status_code == 400

def test_create_category_duplicate(client):
    client.post('/api/categories', json={'name': 'Unique'})
    response = client.post('/api/categories', json={'name': 'Unique'})
    assert response.status_code == 400

def test_update_category_not_found(client):
    response = client.put('/api/categories/9999', json={'name': 'Ghost'})
    assert response.status_code == 404

def test_update_category_no_data(client):
    res = client.post('/api/categories', json={'name': 'Data'})
    cat_id = res.get_json()['id']
    # Sending empty body triggers 400 condition
    response = client.put(f'/api/categories/{cat_id}', json=None)
    assert response.status_code == 400

def test_delete_category_not_found(client):
    response = client.delete('/api/categories/9999')
    assert response.status_code == 404



