from utils.helpers import parse_json_response


def test_get_booking_ids(api_client):
    response = api_client.get('/booking')
    assert response.status_code == 200

    data = parse_json_response(response)
    assert len(data) > 1


def test_get_booking_by_name(api_client):
    response = api_client.get('/booking', params={'firstname': 'Jim', 'lastname': 'Brown'})
    assert response.status_code == 200


def test_get_with_details_by_id(api_client):
    booking_id = 3365
    response = api_client.get(f'/booking/{booking_id}')
    assert response.status_code == 200

    data = parse_json_response(response)
    assert 'Jim' in data['firstname']
    assert 'Brown' in data['lastname']


def test_create_booking(api_client):

    json = {
        'firstname': 'Alex',
        'lastname': 'Zoo',
        'totalprice': 111,
        'depositpaid': True,
        'bookingdates': {
            'checkin': '2024-02-01',
            'checkout': '2024-02-10'
        },
        'additionalneeds': 'Breakfast'
    }

    response = api_client.post('/booking', json=json)
    assert response.status_code == 200

    data = parse_json_response(response)
    assert data['booking'] == json
