from pymarc import MARCReader
from pymarc import Record, Field
from PyZ3950 import zoom
import os, io


def load_system_numbers():
    global sys_numbers
    file_name = "all_numbers.txt"
    print("loading: " + file_name)
    with open(file_name) as f:
        sys_numbers = f.readlines()
    print("found numbers: " + str(len(sys_numbers)))
    print("")


def load_marc_data():
    global marx, sys_numbers
    marx = []

    for sys_no in sys_numbers:
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
                sys_numbers = conn.search(query)
                data = bytes(sys_numbers[0].data)

                print("loaded from aleph: {}".format(sys_no))

                with open("cache/" + sys_no + ".marc", "wb") as f:
                    f.write(data)
            except zoom.ConnectionError:
                print("\n!!! Error: could not connect to aleph !!!\n")

        reader = MARCReader(bytes(data), force_utf8=True, to_unicode=True)
        mc = next(reader)

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

        for field in mc.get_fields('300'):
            if field is not None:
                tmp = [sys_no, field]
                f_300.append(tmp)


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
f_300 = []


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
        sufield_name = l[1]['4']
        if sufield_name == 'aut':
            s_aut = s_aut + 1
        elif sufield_name == 'rcp':
            s_rcp = s_rcp + 1
        elif sufield_name is None:
            s_none = s_none + 1
        else:
            f.write(sufield_name + "\n")
    f.write(u"None: " + unicode(s_none) + "\n")
    f.write(u"aut: " + unicode(s_aut) + "\n")
    f.write(u"rcp: " + unicode(s_rcp) + "\n")

with io.open("output/res_700_subfield_e_as_scr.txt", "w", encoding="utf-8") as f:
    f.write(u"\n\n\n700 sub e:\n\n")
    for l in f_700:
        sufield_name = l[1]['4']
        if sufield_name is not None and sufield_name.startswith('scr'):
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

with io.open("output/extra_res_300.txt", "w", encoding="utf-8") as f:
    f.write(u"300:\n\n")
    for l in f_300:
        f.write(u"{}\t{}\n".format(unicode(l[0]), unicode(l[1])))


with io.open("output/comparison_250_655.txt", "w", encoding="utf-8") as f:
    f.write(u"Siehe Zusammenfassung ganz am Schluss.\n\n\n\nSys.No.\t250\t655\n-------\t---\t---\n\n")
    ss = []
    for l in f_250:
        i = f_250.index(l)
        l2 = f_655[i]
        f.write(u"{}\t\t{}\t\t\t\t{}\n".format(unicode(l[0]), unicode(l[1]), unicode(l2[1])))
        ss.append(u"{}\t\t----\t\t{}\n".format(unicode(l[1].format_field()), unicode(l2[1].format_field())))
    f.write(u"\n\n\n\nOutline:\n\n")
    d = dict()
    for s in ss:
        if s in d:
            d[s] = d.get(s) + 1
        else:
            d[s] = 1
    for pair in d:
        f.write(u"{} Mal: {}".format(d[pair], pair))


"""
Cardinality short
"""

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

    zero = 0
    one = 0
    two = 0
    multiple = 0

    for m in marx:
        fields = m[1].get_fields('300')
        card = len(fields)
        if card == 0:
            zero = zero + 1
        elif card == 1:
            one = one + 1
        elif card == 2:
            two = two + 1
        else:
            multiple = multiple + 1
    f.write(u"300:\n\n")
    f.write(u"0: {}\n".format(unicode(zero)))
    f.write(u"1: {}\n".format(unicode(one)))
    f.write(u"2: {}\n".format(unicode(two)))
    f.write(u"+: {}\n".format(unicode(multiple)))

    f.write(u'\n\n------------------------------\n\n\n')


def print_subfield_cardinality():
    """
    Cardinality Subfields
    """
    with io.open("output/cardinality_subfields.txt", "w", encoding="utf-8") as f:
        f.write(u"Cardinality of Subfields:\n")
        f.write(u"=========================\n\n\n")

        fields = {
            '024': ['a'],
            '856': ['u'],
            '100': ['0', '4', 'a', 'b', 'c', 'd', 'e'],
            '600': ['0', 'a', 'b', 'c', 'd'],
            '700': ['0', '4', 'a', 'b', 'c', 'd', 'e'],
            '610': ['0', 'a', 'g'],
            '710': ['0', '4', 'a', 'b', 'e', 'g'],
            '250': ['a'],
            '264': ['a', 'c'],
            '300': ['a', 'b', 'c', 'e']
        }

        for field_name in fields:
            print_subfield_cardinality_for_field(f, fields, field_name)
            f.write(u"\n\n\n--------------------------------------------------------\n\n\n")


def print_subfield_cardinality_for_field(f, fields, field_name):
    f.write(u"Field: {}\n\n".format(field_name))
    for subfield_name in fields.get(field_name):
        print_cardinality_for_subfield(f, field_name, subfield_name)


def print_cardinality_for_subfield(f, field_name, subfield_name):
    f.write(u"{}:\n".format(subfield_name))
    cardinality = __Cardinality()
    for m in marx:
        mfields = m[1].get_fields(field_name)
        for mf in mfields:
            if mf is not None:
                subfields_val = mf.get_subfields(subfield_name)
                cardinality.add_cardinality(len(subfields_val))
    f.write(unicode(cardinality))


class __Cardinality:
    zero = 0
    one = 0
    multiple = 0

    def __init__(self):
        pass

    def __str__(self):
        res = u"0:\t{}\n1:\t{}\n+:\t{}\n\n".format(zero, one, multiple)
        return res

    def add_zero(self):
        self.zero = self.zero + 1

    def add_one(self):
        self.one = self.one + 1

    def add_multi(self):
        self.multiple = self.multiple + 1

    def add_cardinality(self, c):
        if c == 0:
            self.add_zero()
        elif c == 1:
            self.add_one()
        elif c > 1:
            self.add_multi()


if __name__ == "__main__":
    print("Running...")
    load_system_numbers()
    load_marc_data()
    print_subfield_cardinality()
