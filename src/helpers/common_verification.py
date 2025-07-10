def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code==expected_data,"Expected HTTP Status Code"+expected_data#this is used for verifying booking id
def verify_json_key_not_null(key):
    assert key!=0,"Key is Non-Empty"+key
    assert key>0,"Key is Greater than Zero"

def verify_json_key_not_null_token(key):
    assert key!=0,"Key is Non-Empty"+key


def verify_response_key_not_none(key):
    assert key is not None

def verify_response_text_type(text):
    assert isinstance(text, str), "Expected text to be a string"

def verify_response_text(response_data,expected_text):
    assert response_data==expected_text

def verify_response_key(key,expected_data):
    assert key==expected_data
    