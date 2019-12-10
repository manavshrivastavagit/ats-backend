import jwt, time

class JWT():
    def encode(payload):
       return jwt.encode(payload, 'secret', algorithm='HS256')

    def decode(encoded_jwt):
        return  jwt.decode(encoded_jwt, 'secret', algorithm='HS256')

    def is_valid(encoded_jwt):
        decoded = jwt.decode(encoded_jwt.split()[1], 'secret', algorithm='HS256')
        td_mins = int( round ( abs(  int(time.time() * 1000) - int(decoded.get('createdAt'))  )/60 )/60  )
        if td_mins < 100:
            return True 
        else:
            return False 
        
