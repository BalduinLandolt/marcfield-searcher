from pymarc import MARCReader
from PyZ3950 import zoom

print("loading 'all numbers'...")
with open("all_numbers.txt") as f:
    res = f.readlines()
print("found numbers: " + str(len(res)))

f_505 = []
f_510 = []
f_525 = []

for sys_no in res:
    sys_no = sys_no.strip()
    print("Checking: {}".format(sys_no))
    try:
        conn = zoom.Connection('aleph.unibas.ch', 9909)
        conn.databaseName = 'dsv05'
        conn.preferredRecordSyntax = 'USMARC'

        query = zoom.Query('PQF', '@attr 1=1032 ' + sys_no)
        res = conn.search(query)
        data = bytes(res[0].data)
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
