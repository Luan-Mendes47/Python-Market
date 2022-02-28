from barcode import EAN13
from barcode.writer import ImageWriter
from random import randint


def menu():
    a = ''
    print(f'_____________ Python Market ______________')
    print(f'Search By Product Name                 (1)')
    print(f'Search By Product Type                 (2)')
    print(f'Search By Product Number               (3)')
    print(f'List By Product Name                   (4)')
    print(f'List By Product Number                 (5)')
    print(f'Add/Edit Product                       (6)')
    print(f'Generate Bar Code for all products     (7)')
    print(f'{a:_^42}')


def list_byproduct(num):
    sorted_list = sorted(products, key=lambda k: k[num])
    items_name = ['Product Name: ', 'Product Number: ', 'Product Type: ']
    counter = 0
    for value in sorted_list:
        print(value['product_number'])
        for each_value in value.values():
            if counter > 2:
                counter = 0
            print(f'\t {items_name[counter]} {each_value}')
            counter += 1


def search_type(t):
    counter = 0
    for k in products:
        if t.capitalize() in k.values():
            counter += 1
            print('\t', k['product_name'])
    print(f'{counter} Product Found!')


def add_ed_product():
    product_name = input('Product Name:  ')
    product_number = input('Product Number:  ')
    product_type = input('Product Type:  ')
    products.append({'product_name': product_name.capitalize(),
                     'product_number': product_number,
                     'product_type': product_type.capitalize()})


def searchby_product_name(product_name):
    f = False
    items_name = ['Product Name: ', 'Product Number: ', 'Product Type: ']
    for value in products:
        if product_name == '':
            break
        if product_name.capitalize() in value.values():
            f = True
            counter = 0
            for each_value in value.values():
                print(f'\t{items_name[counter]} {each_value: <8}')
                counter += 1
    if not f: print('NOT FOUND!')

def barcode_generator():
    c = 0
    for item in products:
        item.update({'Barcode': str(randint(000000000000, 9999999999999))})
        for each_item in item:
            if 'product_name' in each_item:
                product_name = item[each_item]
        for each_item in item:
            if 'Barcode' in each_item:
                code = item[each_item]
                bar_code = EAN13(code, writer=ImageWriter())
                bar_code.save(product_name)
                c += 1
                print(f'{c} Barcodes Generated')


products = [
            {
                'product_name':   'Rice',
                'product_number': '12',
                'product_type':   'Food',
            },
            {
                'product_name':   'Microwave',
                'product_number': '456',
                'product_type':   'Home appliance',
            },
            {
                'product_name':   'Television',
                'product_number': '382',
                'product_type':   'Device',
            },
           ]


loop = True
while loop:
    menu()
    op = input('Input: ')
    if op == '1':
        n = input('Product: ')
        searchby_product_name(n)
    elif op == '2':
        t = input('Type: ')
        search_type(t)
    elif op == '3':
        t = input('Number: ')
        searchby_product_name(t)
    elif op == '4':
        list_byproduct('product_name')
    elif op == '5':
        list_byproduct('product_number')
    elif op == '6':
        add_ed_product()
    elif op == '7':
        barcode_generator()
    else:
        print('Msg Error: Invalid option!')
    s = input('Exit? y[es] n[any key] ')
    if s.lower() == 'y':
        loop = False
