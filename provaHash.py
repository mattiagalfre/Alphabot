import hashlib
mex = "abc"
result = hashlib.md5(mex.encode())
print(result.hexdigest())