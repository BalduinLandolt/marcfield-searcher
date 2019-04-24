from pymarc import MARCReader
from PyZ3950 import zoom
import os, codecs, io

file_name = "all_numbers.txt"

print("loading: " + file_name)
with open(file_name) as f:
    res = f.readlines()
print("found numbers: " + str(len(res)))
print("")

f_041 = []
f_546 = []
f_246_3 = []
f_250 = []
f_490 = []
f_505 = []
f_510 = []
f_525 = []
f_533 = []
f_534 = []

for sys_no in res:
    sys_no = sys_no.strip()

    if os.path.isfile("cache/" + sys_no + ".marc"):
        with open("cache/" + sys_no + ".marc", "rb") as f:
            data = f.read()
        print("read from cache: {}".format(sys_no))
    else:
        try:
            conn = zoom.Connection('aleph.unibas.ch', 9909)
            conn.databaseName = 'dsv05'
            conn.preferredRecordSyntax = 'USMARC'

            query = zoom.Query('PQF', '@attr 1=1032 ' + sys_no)
            res = conn.search(query)
            data = bytes(res[0].data)

            print("loaded from aleph: {}".format(sys_no))

            with open("cache/" + sys_no + ".marc", "wb") as f:
                f.write(data)
        except zoom.ConnectionError:
            print("\n!!! Error: could not connect to aleph !!!\n")

    reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
    mc = next(reader)

    ff = []
    """
    for field in mc.get_fields('505'):
        print(unicode(field))
        print(str(mc))
        ff.append(field)
    if len(ff) == 0:
        print("No field 505 in: {}".format(sys_no))
    else:
        print(str(mc))
    """

    for field in mc.get_fields('041'):
        if field is not None:
            tmp = [sys_no, field]
            f_041.append(tmp)

    for field in mc.get_fields('546'):
        if field is not None:
            tmp = [sys_no, field]
            f_546.append(tmp)
        if len(mc.get_fields('546')) > 1:
            f_546.append([u'\t\t !!!! Mehrfach !!!!', u''])

    for field in mc.get_fields('246'):
        if field is not None:
            tmp = [sys_no, field]
            f_246_3.append(tmp)

    for field in mc.get_fields('250'):
        if field is not None:
            tmp = [sys_no, field]
            f_250.append(tmp)

    for field in mc.get_fields('490'):
        if field is not None:
            tmp = [sys_no, field]
            f_490.append(tmp)

    for field in mc.get_fields('505'):
        if field is not None:
            tmp = [sys_no, field]
            f_505.append(tmp)

    for field in mc.get_fields('510'):
        if field is not None:
            tmp = [sys_no, field]
            f_510.append(tmp)

    for field in mc.get_fields('525'):
        if field is not None:
            tmp = [sys_no, field]
            f_525.append(tmp)

    for field in mc.get_fields('533'):
        if field is not None:
            tmp = [sys_no, field]
            f_533.append(tmp)

    for field in mc.get_fields('534'):
        if field is not None:
            tmp = [sys_no, field]
            f_534.append(tmp)

"""
print("\n\n\n505:\n")
for l in f_505:
    print(u"{}\t{}".format(unicode(l[0]), unicode(l[1])))

print("\n\n\n510:\n")
for l in f_510:
    print(u"{}\t{}".format(unicode(l[0]), unicode(l[1])))

print("\n\n\n525:\n")
for l in f_525:
    print(u"{}\t{}".format(unicode(l[0]), unicode(l[1])))
"""

with io.open("output/res_401.txt", "w", encoding="utf-8") as f:
    f.write(u"041:\n\n")
    for l in f_041:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_546.txt", "w", encoding="utf-8") as f:
    f.write(u"546:\n\n")
    for l in f_546:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_246.txt", "w", encoding="utf-8") as f:
    f.write(u"246 3:\n\n")
    for l in f_246_3:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_250.txt", "w", encoding="utf-8") as f:
    f.write(u"250:\n\n")
    for l in f_250:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_490.txt", "w", encoding="utf-8") as f:
    f.write(u"490:\n\n")
    for l in f_490:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_505.txt", "w", encoding="utf-8") as f:
    f.write(u"505:\n\n")
    for l in f_505:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_510.txt", "w", encoding="utf-8") as f:
    f.write(u"510:\n\n")
    for l in f_510:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_525.txt", "w", encoding="utf-8") as f:
    f.write(u"525:\n\n")
    for l in f_525:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_533.txt", "w", encoding="utf-8") as f:
    f.write(u"533:\n\n")
    for l in f_533:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_534.txt", "w", encoding="utf-8") as f:
    f.write(u"534:\n\n")
    for l in f_534:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

"""
    ff = []

    for field in mc.get_fields('505'):
        print(unicode(field))
        print(str(mc))
        ff.append(field)
    if len(ff) == 0:
        print("No field 505 in: {}".format(sys_no))
    else:
        print(str(mc))
"""
