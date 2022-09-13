import hmac
import hashlib
from urllib import parse
def get_md5(password,token):
	return hmac.new(token.encode(), password.encode(), hashlib.md5).hexdigest()


if __name__ == '__main__':
	password="123"
	token="8975424a6a063b318bb715f853a9e53fb4ea3f7dfff176624f202a5d1331a821"
	print(get_md5(password,token))