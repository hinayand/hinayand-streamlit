import hashlib


def sha256(something):
    return hashlib.sha256(something.encode('utf-8')).hexdigest()


def sha512(something):
    return hashlib.sha512(something.encode('utf-8')).hexdigest()


def md5(something):
    print('MD5 don`t secret!')
    return hashlib.md5(something.encode('utf-8')).hexdigest()


def sha1(something):
    return hashlib.sha1(something.encode('utf-8')).hexdigest()


def sha384(something):
    return hashlib.sha384(something.encode('utf-8')).hexdigest()


def sha3_224(something):
    return hashlib.sha3_224(something.encode('utf-8')).hexdigest()


def sha3_256(something):
    return hashlib.sha3_256(something.encode('utf-8')).hexdigest()


def sha3_384(something):
    return hashlib.sha3_384(something.encode('utf-8')).hexdigest()
