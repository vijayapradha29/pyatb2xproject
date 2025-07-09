def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code==expected_data,"Expected HTTP Status Code"+expected_data#this is used for verifying booking id
def verify_json_key_not_null(key):
    assert key!=0,"Key is Non-Empty"+key
    assert key>0,"Key is Greater than Zero"

def verify_response_key_not_none(key):
    assert key is not None

    