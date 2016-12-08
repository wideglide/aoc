from hashlib import md5

door_id = "uqwqemis"
pwd = ""
pwd2 = [None] * 8
first_eight = [4515059,6924074,8038154,13432968,13540621,14095580,14821988,16734551]


#while len(pwd) < 8:
for i in first_eight:
    digest = " " * 5
    while digest[:5] != "00000":
        h = md5()
        h.update(door_id + str(i))
        digest = h.hexdigest()
    print digest, digest[5], pwd, i, pwd2
    pwd += digest[5]
    if '0' <= digest[5] < '8' and pwd2[int(digest[5])] == None:
        pwd2[int(digest[5])] = digest[6]
print pwd

next_nine =[ 17029030,17670493,17743256,18333805,19112977,20616595,21658552,21926249,26326685 ]
i = 17029030
while None in pwd2:
    digest = " " * 5
    while digest[:5] != "00000":
        h = md5()
        h.update(door_id + str(i))
        digest = h.hexdigest()
        i += 1
    print digest, digest[5], pwd, (i-1), pwd2
    if '0' <= digest[5] < '8' and pwd2[int(digest[5])] == None:
        pwd2[int(digest[5])] = digest[6]
print ''.join(pwd2)
