from operator import itemgetter

class OS:
    def __init__(self, id, name, version, comp_id):
        self.id = id
        self.name = name
        self.version = version
        self.comp_id = comp_id

class Comp:
    def __init__(self, id, type):
        self.id = id
        self.type = type

class OSComp:
    def __init__(self, os_id, comp_id):
        self.os_id = os_id
        self.comp_id = comp_id

comps = [
    Comp(1, 'Ноутбук'),
    Comp(2, 'ПК'),
    Comp(3, 'Сервер'),

    Comp(11, '(другой) Ноутбук'),
    Comp(22, '(другой) ПК'),
    Comp(33, '(другой) Сервер'),
]

oss = [
    OS(1, 'Windows', 10, 1),
    OS(2, 'Windows', 11, 2),
    OS(3, 'macOS', 14.5, 3),
    OS(3, 'Linux', 7.3, 4),
]

oss_comps = [
    OSComp(1,1),
    OSComp(2,2),
    OSComp(3,3),
    OSComp(3,4),
    OSComp(11,1),
    OSComp(22,2),
    OSComp(33, 3),
    OSComp(33, 4),
]

def main():
    one_to_many = [(o.name, o.version, c.type)
                   for o in oss
                   for c in comps
                   if o.comp_id == c.id]
    many_to_many_temp = [(c.type, oc.comp_id, oc.os_id)
                    for c in comps
                    for oc in oss_comps
                    if c.id == oc.comp_id]
    many_to_many = [(o.name, o.version, comp_type)
                    for comp_type, comp_id, os_id, in many_to_many_temp
                    for o in oss if o.id==os_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for c in comps:
        c_oss = list(filter(lambda i: i[2]==c.type, one_to_many))
        if len(c_oss)>0:
            c_versions = [version for _,version,_ in c_oss]
            c_versions_sum = sum(c_versions)
            res_12_unsorted.append((c.type, c_versions_sum))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


if __name__ == '__main__':
    main()