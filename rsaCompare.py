#!/usr/bin/python
# coding=utf-8

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
from Crypto import Random
from Crypto.Hash import MD5
import os

def compare(a1, a2):
    result = []
    # 伪随机数生成器
    random_generator = Random.new().read

    # 生成2048比特秘钥对(pk, sk)
    rsa = RSA.generate(2048, random_generator)
    private_pem = rsa.exportKey()
    with open('master-privatekey.pem', 'w') as f:
        f.write(str(private_pem, encoding="utf8"))
    public_pem = rsa.publickey().exportKey()
    with open('master-publickey.pem', 'w') as f:
        f.write(str(public_pem, encoding="utf8"))

    with open(a1, "rb") as f:
        message1 = f.read()

    # 对消息进行签名
    h = MD5.new(message1)
    private_key = RSA.importKey(open('master-privatekey.pem').read())
    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(h)

    # 对消息进行签名验证
    with open(a2, "rb") as f:
        message2 = f.read()
    h = MD5.new(message2)
    public_key = RSA.importKey(open('master-publickey.pem', 'r').read())
    verifier = PKCS1_v1_5.new(public_key)
    if verifier.verify(h, signature):
        result.append(a1+"和"+a2+"一致")
    else:
        result.append(a1+"和"+a2+"不一致")
    return "\n".join(result)


if __name__ == '__main__':
    compare()
