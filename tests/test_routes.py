# testing homepage and that it loads
def test_home(app_test):  
    client = app_test.test_client() # client is a browser
    resp = client.get('/') 
    assert resp.status_code == 200 # assert testing a case, a test will only pass if an asset test case is true 
    assert b"WMG Teaching Support System" in resp.data


# testing that an unauthenticated user cannot access the /account page 
def test_account_setting(app_test):
    client = app_test.test_client()
    resp = client.get('/account')
    assert b"Profile Settings" not in resp.data
    assert resp.status_code == 302