import jwt

class JWT():
    def encode(payload):
       return jwt.encode(payload, 'secret', algorithm='HS256')

    def decode(encoded_jwt):
        return  jwt.decode(encoded_jwt, 'secret', algorithm='HS256')
 
