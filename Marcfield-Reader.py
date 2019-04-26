from pymarc import MARCReader
from pymarc import Record, Field
from PyZ3950 import zoom
import os, io

file_name = "all_numbers.txt"

print("loading: " + file_name)
with open(file_name) as f:
    res = f.readlines()
print("found numbers: " + str(len(res)))
print("")

marx = []

f_024 = []
f_041 = []
f_246_3 = []
f_250 = []
f_490 = []
f_505 = []
f_510 = []
f_525 = []
f_533 = []
f_534 = []
f_544 = []
f_546 = []
f_581 = []
f_596 = []
f_600 = []
f_655 = []
f_700 = []
f_710 = []
f_856 = []


f_906 = []
f_046 = []
f_100 = []
f_600 = []
f_700 = []
f_610 = []
f_264 = []

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

    marx.append([sys_no, mc])

    for field in mc.get_fields('024'):
        if field is not None:
            tmp = [sys_no, field]
            f_024.append(tmp)

    for field in mc.get_fields('041'):
        if field is not None:
            tmp = [sys_no, field]
            f_041.append(tmp)

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

    for field in mc.get_fields('544'):
        if field is not None:
            tmp = [sys_no, field]
            f_544.append(tmp)

    for field in mc.get_fields('546'):
        if field is not None:
            tmp = [sys_no, field]
            f_546.append(tmp)
        if len(mc.get_fields('546')) > 1:
            f_546.append([u'\t\t !!!! Mehrfach !!!!', u''])

    for field in mc.get_fields('581'):
        if field is not None:
            tmp = [sys_no, field]
            f_581.append(tmp)

    for field in mc.get_fields('596'):
        if field is not None:
            tmp = [sys_no, field]
            f_596.append(tmp)

    for field in mc.get_fields('600'):
        if field is not None:
            tmp = [sys_no, field]
            f_600.append(tmp)

    for field in mc.get_fields('655'):
        if field is not None:
            tmp = [sys_no, field]
            f_655.append(tmp)

    for field in mc.get_fields('700'):
        if field is not None:
            tmp = [sys_no, field]
            f_700.append(tmp)

    for field in mc.get_fields('710'):
        if field is not None:
            tmp = [sys_no, field]
            f_710.append(tmp)

    for field in mc.get_fields('856'):
        if field is not None:
            tmp = [sys_no, field]
            f_856.append(tmp)

    for field in mc.get_fields('906'):
        if field is not None:
            tmp = [sys_no, field]
            f_906.append(tmp)

    for field in mc.get_fields('046'):
        if field is not None:
            tmp = [sys_no, field]
            f_046.append(tmp)

    for field in mc.get_fields('100'):
        if field is not None:
            tmp = [sys_no, field]
            f_100.append(tmp)

    for field in mc.get_fields('600'):
        if field is not None:
            tmp = [sys_no, field]
            f_600.append(tmp)

    for field in mc.get_fields('700'):
        if field is not None:
            tmp = [sys_no, field]
            f_700.append(tmp)

    for field in mc.get_fields('610'):
        if field is not None:
            tmp = [sys_no, field]
            f_610.append(tmp)

    for field in mc.get_fields('264'):
        if field is not None:
            tmp = [sys_no, field]
            f_264.append(tmp)


with io.open("output/res_024.txt", "w", encoding="utf-8") as f:
    f.write(u"024:\n\n")
    for l in f_024:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_041.txt", "w", encoding="utf-8") as f:
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

with io.open("output/res_544.txt", "w", encoding="utf-8") as f:
    f.write(u"544:\n\n")
    for l in f_544:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_581.txt", "w", encoding="utf-8") as f:
    f.write(u"581:\n\n")
    for l in f_581:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_596.txt", "w", encoding="utf-8") as f:
    f.write(u"596:\n\n")
    for l in f_596:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_600.txt", "w", encoding="utf-8") as f:
    f.write(u"600:\n\n")
    for l in f_600:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_655.txt", "w", encoding="utf-8") as f:
    f.write(u"655:\n\n")
    for l in f_655:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_700.txt", "w", encoding="utf-8") as f:
    f.write(u"700:\n\n")
    for l in f_700:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_700-12.txt", "w", encoding="utf-8") as f:
    f.write(u"700 12:\n\n")
    for l in f_700:
        if hasattr(l[1], 'indicator2'):
            in2 = l[1].indicator2
            if in2 != ' ':
                f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_710.txt", "w", encoding="utf-8") as f:
    f.write(u"710:\n\n")
    for l in f_710:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_856.txt", "w", encoding="utf-8") as f:
    f.write(u"856:\n\n")
    for l in f_856:
        f.write(u"{}\t{}\t\t{}\n".format(unicode(l[0]), unicode(l[1]), l[1].format_field()))



with io.open("output/extra_res_906.txt", "w", encoding="utf-8") as f:
    f.write(u"906:\n\n")
    for l in f_906:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/extra_res_046.txt", "w", encoding="utf-8") as f:
    f.write(u"046:\n\n")
    for l in f_046:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/extra_res_100.txt", "w", encoding="utf-8") as f:
    f.write(u"100:\n\n")
    for l in f_100:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/extra_res_600.txt", "w", encoding="utf-8") as f:
    f.write(u"600:\n\n")
    for l in f_600:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/extra_res_600_subfield_2.txt", "w", encoding="utf-8") as f:
    f.write(u"600:\n\n")
    for l in f_600:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1]['2'])))

with io.open("output/extra_res_700_subfield_4_and_e.txt", "w", encoding="utf-8") as f:
    f.write(u"700 sub 4:\n\n")
    for l in f_700:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1]['4'])))
    f.write(u"\n\n\n700 sub e:\n\n")
    for l in f_700:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1]['e'])))
    f.write(u"\n\n\noverview:\n\n")
    s_aut = 0
    s_rcp = 0
    s_none = 0
    for l in f_700:
        val = l[1]['4']
        if val == 'aut':
            s_aut = s_aut + 1
        elif val == 'rcp':
            s_rcp = s_rcp + 1
        elif val is None:
            s_none = s_none + 1
        else:
            f.write(val + "\n")
    f.write(u"None: " + unicode(s_none) + "\n")
    f.write(u"aut: " + unicode(s_aut) + "\n")
    f.write(u"rcp: " + unicode(s_rcp) + "\n")

with io.open("output/res_700_subfield_e_as_scr.txt", "w", encoding="utf-8") as f:
    f.write(u"\n\n\n700 sub e:\n\n")
    for l in f_700:
        val = l[1]['4']
        if val is not None and val.startswith('scr'):
            f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/extra_res_700.txt", "w", encoding="utf-8") as f:
    f.write(u"700:\n\n")
    for l in f_700:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/extra_res_610.txt", "w", encoding="utf-8") as f:
    f.write(u"610:\n\n")
    for l in f_610:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_264.txt", "w", encoding="utf-8") as f:
    f.write(u"264:\n\n")
    for l in f_264:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))

with io.open("output/res_264_subfield_b.txt", "w", encoding="utf-8") as f:
    f.write(u"264 sub b:\n\n")
    for l in f_264:
        s_b = l[1]['b']
        if s_b is not None:
            f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(s_b)))



with io.open("output/cardinality.txt", "w", encoding="utf-8") as f:
    f.write(u"024:\n\n")
    for m in marx:
        fields = m[1].get_fields('024')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"856:\n\n")
    for m in marx:
        fields = m[1].get_fields('856')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"100:\n\n")
    for m in marx:
        fields = m[1].get_fields('100')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"600:\n\n")
    for m in marx:
        fields = m[1].get_fields('600')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"700:\n\n")
    for m in marx:
        fields = m[1].get_fields('700')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"610:\n\n")
    for m in marx:
        fields = m[1].get_fields('610')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"710:\n\n")
    for m in marx:
        fields = m[1].get_fields('710')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"250:\n\n")
    for m in marx:
        fields = m[1].get_fields('250')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')

    f.write(u"264:\n\n")
    for m in marx:
        fields = m[1].get_fields('264')
        card = len(fields)
        f.write(u"{}\t{}\n".format(unicode(m[0]), unicode(card)))

    f.write(u'\n\n------------------------------\n\n\n')


with io.open("output/cardinality_short.txt", "w", encoding="utf-8") as f:
    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('024')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"024:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('856')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"856:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('100')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"100:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('600')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"600:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('700')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"700:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('610')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"610:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('710')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"710:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('250')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"250:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('264')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"264:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')
