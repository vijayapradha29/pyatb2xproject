class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_auth():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def url_put_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)