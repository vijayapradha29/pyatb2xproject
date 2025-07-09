class Utils(object):
    # you can create class or can directly create functions

    def common_headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml"
        }
    '''
    def common_header_put_patch_delete_with_basic_auth(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }
        return headers
        
    (or)
    '''
    def common_header_put_patch_delete_with_basic_auth(self,basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic "+str(basic_auth_value)
        }
        return headers

    def common_header_put_patch_delete_with_token(self,token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token)
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass