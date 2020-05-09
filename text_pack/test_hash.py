import hashlib

"""new_md5 = hashlib.new('md5', b'python').hexdigest()  # hexdigest()返回16进制
print(new_md5)
new_md5 = hashlib.md5("python".encode()).hexdigest()
print(new_md5)
new_md5 = hashlib.sha1('python'.encode()).hexdigest()
print(new_md5)

sha1 = hashlib.sha1()
sha1.update('hello ubuntu'.encode('utf-8'))
sha1.update('python'.encode())
print(sha1)
sha1 = hashlib.sha1('hello ubuntu'.encode('utf-8')).hexdigest()
print(sha1)
sha1 = hashlib.sha1('hello ubuntu'.encode()).digest()  # 返回二进制数
print(sha1)"""

from Crypto.cipher import AES
# 加密与解密所使用的密钥，长度必须是16的倍数
secret_key = "this is secretkey"
# 要加密的明文数据，长度必须是16的倍数
plain_data = "hello ubuntu"
# IV参数，长度必须是16的倍数
iv_param = 'this is an IV456'
# 数据加密
aes1 = AES.new(secret_key, AES.MODE_CBC, iv_param)
cipher_data = aes1.encrypt(plain_data)
print(cipher_data)
# 数据解密
aes2 = AES.new(secret_key, AES.MODE_CBC, 'this is an IV456')
plain_data2 = aes2.encrypt(plain_data)
print(plain_data2)




"""import rsa

# 生成密钥：生成RSA公钥和秘钥
(pubkey, privkey) = rsa.newkeys(1024)

# 保存密钥(一个公钥一个私钥)
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())
with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())

# 导入密钥
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

# 明文
message = "python"

# 公钥对明文加密，得到密文
crypto = rsa.encrypt(message.encode(), pubkey)

# 私钥对密文解密，得到明文
message = rsa.decrypt(crypto, privkey).decode()
print(message)

message = "这是服务器发的消息！"
# 私钥签名
signature = rsa.sign(message.encode("utf-8"), privkey, 'SHA-1')
# 公钥验证：同时收到指令明文、密文，然后用公钥验证，进行身份确认
result = rsa.verify(message.encode("utf-8"), signature, pubkey)
print(result)

from passlib.hash import pbkdf2_sha512

# 对love字符串进行加密，love是明文，password_hash是密文。
password_hash = pbkdf2_sha512.encrypt("love")
print(password_hash)  # 结果：$pbkdf2-sha512$25000$wnjvvdf6XytFyHlPyVkLAQ$2kL4UztPbWoQmblT4TRxOUoCiDNYvSwGd1EYOWcqhrYUpH9MXHfzaFFw3fGyRsfIZy8SDlXD1HP2U4AlIsdBTA

# 对love字符串进行验证，love是明文，password_hash是密文。
result = pbkdf2_sha512.verify("love", password_hash)
print(result)  # 结果：True
"""