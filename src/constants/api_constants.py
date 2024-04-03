# APIConstants - Class which contain all the endpoints. # Keep the URLs

# Concepts
# Static Method -> Which can be called by without the Object directly by using
# class you can call it


class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"
    
    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"
    
    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"
    
    # Update, PUT, PATCH, DELETE - bookingId
    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
