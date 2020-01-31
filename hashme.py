import hashlib

with open("unhashed.txt") as i:
    with open('hashed.txt',"w") as o:
        for l in i:
            x = l.strip().split("\t")
            hashed_email = hashlib.sha256(
                x[1].lower().encode('utf-8')).hexdigest()
            o.write("%s\t%s\n" % (x[0], hashed_email))
