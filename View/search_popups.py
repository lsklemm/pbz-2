from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp




class SearchPopupWorkArea(Popup, Widget):
    """
    Popup for WORK AREA table
    """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    def set_work_area_number(self, number):
        self.controller.set_work_area_number(number)
    def set_work_area_name(self, name):
        self.controller.set_work_area_name(name)
    def set_work_area_equipment_type(self, type):
        self.controller.set_work_area_equipment_type(type)
    def add_work_area(self):
        self.controller.add_work_area()
        self.table.to_table_work_area()

class SearchPopupEquipment(Popup, Widget):
    """
        Popup for EQUIPMENT table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    def set_search_equipment_date(self, date):
        self.controller.set_search_equipment_date(date)

    def search_equipment(self):
        self.controller.search_equipment()

    def choose_search_equipment(self):
        date_dialog = MDDatePicker(min_year=2010, max_year=2022)
        date_dialog.bind(on_save=self.set_search_equipment_date_calendar)
        date_dialog.open()
    def set_search_equipment_date_calendar(self, instance, value, date_range):
        self.set_search_equipment_date(str(value))
        self.ids.search_equipment_date.text = str(value)


class FoundPopupEquipment(Popup, Widget):
    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.found_list = self.model.return_table_search_equipment()
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Дата", dp(40)),
                                     ("Название оборудования", dp(40)),
                                     ("Тип оборудования", dp(40)),
                                     ("Название участка", dp(40)),
                                     ("Причина отказа", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.found_list)

        self.add_widget(self.table)


class SearchPopupTechInspection(Popup, Widget):
    """
        Popup for TECH INSPECTION table
        """
    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller


    def set_search_tech_inspection_equipment_number(self, number):
        self.controller.set_search_tech_inspection_equipment_number(number)

    def search_tech_inspection(self):
        self.controller.search_tech_inspection()

class FoundPopupTechInspection(Popup, Widget):
    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.found_list = self.model.return_table_search_tech_inspection()
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Дата", dp(40)),
                                     ("Номер оборудования", dp(40)),
                                     ("Название",dp(40)),
                                     ("Тип", dp(40)),
                                     ("Результат", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.found_list)

        self.add_widget(self.table)





class SearchPopupEmployee(Popup, Widget):
    """
        Popup for EMPLOYEE table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller

    def set_search_employee_date(self, date):
        self.controller.set_search_employee_date(date)

    def search_employee_date(self):
        self.controller.search_employee_date()

    def choose_search_employee(self):
        date_dialog = MDDatePicker(min_year=2010, max_year=2022)
        date_dialog.bind(on_save=self.set_search_employee_date_calendar)
        date_dialog.open()
    def set_search_employee_date_calendar(self, instance, value, date_range):
        self.set_search_employee_date(str(value))
        self.ids.search_employee_date.text = str(value)


class FoundPopupSearchEmployee(Popup, Widget):
    def __init__(self, controller, model, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.found_list = self.model.return_table_search_employee()
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Дата", dp(60)),
                                     ("ФИО", dp(70)),
                                     ("Должность", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.found_list)

        self.add_widget(self.table)