class Store:
    def __init__(self, printers_amount, scanners_amount, xeroxes_amount):
        self.printers_amount = printers_amount
        self.scanners_amount = scanners_amount
        self.xeroxes_amount = xeroxes_amount

    def amount_of_office_equipment(self):
        sum_off_eq = self.printers_amount + self.scanners_amount + self.xeroxes_amount
        print(f'На складе находится {sum_off_eq} единиц оргтехники')

    @staticmethod
    def get_office_equipment():
        equip_name = []
        equip_num = []
        print('Для завершения ввода введите "esc"')
        while True:
            for_equip_name = input('Введите наименование единцы оргтехники: ')
            if for_equip_name != "esc":
                for_equip_num = input(f'Введите количесвто единиц для оргтехники "{for_equip_name}": ')
                try:
                    if not for_equip_num.isdigit():
                        raise ValueError("Вы ввели не число!")
                except ValueError as err:
                    print(err)
                else:
                    for_equip_num += " ед"
                    equip_name.append(for_equip_name)
                    equip_num.append(for_equip_num)
            else:
                print('Ввод завершен')
                break

        equip_dict = dict(zip(equip_name, equip_num))
        print(f'На склад была принята оргтехника: \n {equip_dict}')

    @staticmethod
    def move_off_eq_to_com(eq_name, eq_amount, company):
        print(f'{eq_name} был передан в команию {company} в количестве {eq_amount} ед')


class OfficeEquipment(Store):
    def __init__(self, printer_name='HP Laser Jet Pro', scanner_name='EPSON WorkForce', xerox_name='Xerox B1022'):
        self.printer_name = printer_name
        self.scanner_name = scanner_name
        self.xerox_name = xerox_name

    def start_working(self, timer_1=0, timer_2=5, timer_3=10):
        print(f'{self.printer_name} начинает работу через {timer_1} c')
        print(f'{self.scanner_name} начинает работу через {timer_2} c')
        print(f'{self.xerox_name} начинает работу через {timer_3} c')

    def end_working(self):
        print(f'Работа {self.printer_name} завершена')
        print(f'Работа {self.scanner_name} завершена')
        print(f'Работа {self.xerox_name} завершена')


class Printer(OfficeEquipment):
    def print_text(self):
        print(f'{self.printer_name} печатает страницы с текстом')


class Scanner(OfficeEquipment):
    def scan_doc(self):
        print(f'{self.scanner_name} сканирует документ')


class Xerox(OfficeEquipment):
    def xerox_page(self):
        print(f'{self.xerox_name} копирует страницу')


equipment = Store(8, 10, 5)
equipment.amount_of_office_equipment()
equipment.get_office_equipment()
equipment.move_off_eq_to_com('Samsung-3200', 15, "ООО Радуга")

store = OfficeEquipment('Samsung-3200', 'Espada E-IScan', 'Canon Pixma')
store.start_working(4, 6, 10)
store.end_working()

printer = Printer('Samsung-3200')
printer.print_text()

scanner = Scanner()
scanner.scan_doc()

xerox = Xerox()
xerox.xerox_page()
