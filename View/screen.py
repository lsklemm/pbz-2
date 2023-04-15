import os
from kivy.lang import Builder

from kivy.properties import ObjectProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tooltip import MDTooltip
from kivy.factory import Factory

from View.add_popups import AddPopupEmp, AddPopupEquipment, AddPopupWorkArea, AddPopupTechInspection
from View.remove_popups import RemovePopupEquipment, RemovePopupWorkArea, RemovePopupTechInspection, RemovePopupEmployee
from View.update_popups import UpdatePopupEquipment, UpdatePopupWorkArea, UpdatePopupEmployee, UpdatePopupTechInspection
from View.search_popups import SearchPopupEmployee, SearchPopupEquipment, SearchPopupWorkArea, SearchPopupTechInspection, FoundPopupEquipment


class MainScreen(MDScreen):

    def __init__(self, controller,model,**kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.model = model

        self.current_table_id = 1
        self.unique_check = 0

        self.unique_info = []

        self.current_emp_number = 0

        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Номер", dp(60)),
                                     ("Название", dp(60)),
                                     ("Тип оборудования", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.controller.get_table_work_area())
        self.add_widget(self.table)
        self.table.bind(on_check_press=self.choose_record)


    def choose_record(self, instance, record_info):
        self.unique_info = []
        if self.current_table_id == 1:
            self.unique_info.append(record_info[0])
            self.unique_info.append(record_info[1])
            self.unique_info.append(record_info[2])
        elif self.current_table_id == 2:
            self.unique_info.append(record_info[0])
            self.unique_info.append(record_info[1])
            self.unique_info.append(record_info[2])
        elif self.current_table_id == 3:
            self.unique_info.append(record_info[0])
            self.unique_info.append(record_info[1])
            self.unique_info.append(record_info[2])
            self.unique_info.append(record_info[3])
            self.unique_info.append(record_info[4])
        elif self.current_table_id == 4:
            self.unique_info.append(record_info[0])
            self.unique_info.append(record_info[1])
            self.unique_info.append(record_info[2])



    # --------------- CHANGE MAIN TABLES ----------------

    # change to ПРОИЗВОДСТВЕННЫЙ_УЧАСТОК table
    def to_table_work_area(self):
        self.current_table_id = 1
        self.remove_widget(self.table)
        self.table = MDDataTable(pos_hint={'center_y':0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check = True,
                                 column_data=[
                                     ("Номер", dp(60)),
                                     ("Название", dp(60)),
                                     ("Тип оборудования", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.controller.get_table_work_area())
        self.add_widget(self.table)
        self.table.bind(on_check_press=self.choose_record)

    # change to ОБОРУВДОВАНИЕ table
    def to_table_equipment(self):
        self.current_table_id = 2
        self.remove_widget(self.table)
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Номер", dp(60)),
                                     ("Название", dp(60)),
                                     ("Тип", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.controller.get_table_equipment())
        self.add_widget(self.table)
        self.table.bind(on_check_press=self.choose_record)

    # change to ТЕХНИЧЕСКИЙ_ОСМОТР table
    def to_table_tech_inspection(self):
        self.remove_widget(self.table)
        self.current_table_id = 3
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Дата", dp(40)),
                                     ("Номер оборудования", dp(40)),
                                     ("Результат", dp(60)),
                                     ("ФИО проверяющего", dp(60)),
                                     ("Причина", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.controller.get_table_tech_inspection())
        self.add_widget(self.table)
        self.table.bind(on_check_press=self.choose_record)

    # change to СОТРУДНИК table
    def to_table_employee(self):
        self.remove_widget(self.table)
        self.current_table_id = 4
        self.table = MDDataTable(pos_hint={'center_y': 0.56, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("Табельный номер", dp(60)),
                                     ("ФИО", dp(60)),
                                     ("Должность", dp(60))], size_hint=(1, 0.7),
                                 row_data=self.controller.get_table_emp())
        self.add_widget(self.table)
        self.table.bind(on_check_press=self.choose_record)





    # --------------- POPUPS ---------------------
    # open ADD POPUPS
    def open_add_popup(self):
        if self.current_table_id == 1:
            Factory.AddPopupWorkArea(controller = self.controller, model = self.model, table = self).open()
        elif self.current_table_id == 2:
            Factory.AddPopupEquipment(controller = self.controller, model = self.model, table = self).open()
        elif self.current_table_id == 3:
            Factory.AddPopupTechInspection(controller = self.controller, model = self.model, table = self).open()
        elif self.current_table_id == 4:
            Factory.AddPopupEmp(controller = self.controller, model = self.model, table = self).open()
    # open REMOVE POPUP
    def open_remove_popup(self):
        if self.current_table_id == 1:
            remove_work_area = ObjectProperty()
            remove_work_area = RemovePopupWorkArea(controller = self.controller, model = self.model, table = self)
            remove_work_area.set_unique_work_area(self.unique_info)
            remove_work_area.open()
        elif self.current_table_id == 2:
            remove_equipment = RemovePopupEquipment(controller = self.controller, model = self.model, table = self)
            remove_equipment.set_unique_equipment(self.unique_info)
            remove_equipment.open()
        elif self.current_table_id == 3:
            remove_tech_inspection = RemovePopupTechInspection(controller = self.controller, model = self.model, table = self)
            remove_tech_inspection.set_unique_tech_inspection(self.unique_info)
            remove_tech_inspection.open()
        elif self.current_table_id == 4:
            remove_employee = RemovePopupEmployee(controller = self.controller, model = self.model, table = self)
            remove_employee.set_unique_employee(self.unique_info)
            remove_employee.open()
    # open UPDATE POPUP
    def open_update_popup(self):
        if self.current_table_id == 1:
            update_work_area = UpdatePopupWorkArea(controller = self.controller, model = self.model, table = self)
            update_work_area.set_previous_info(self.unique_info)
            update_work_area.open()
        elif self.current_table_id == 2:
            update_equipment = UpdatePopupEquipment(controller = self.controller, model = self.model, table = self)
            update_equipment.set_previous_info(self.unique_info)
            update_equipment.open()
        elif self.current_table_id == 3:
            update_tech_inspection = UpdatePopupTechInspection(controller = self.controller, model = self.model, table = self)
            update_tech_inspection.set_previous_info(self.unique_info)
            update_tech_inspection.open()
        elif self.current_table_id == 4:
            update_employee = UpdatePopupEmployee(controller = self.controller, model = self.model, table = self)
            update_employee.set_previous_info(self.unique_info)
            update_employee.open()

    # ------- OPEN SETCH POPUPS ----------
    def open_search_popup(self):
        if self.current_table_id == 1:
            pass
        elif self.current_table_id == 2:
            self.model.search_equipment()
            # search_equipment = FoundPopupEquipment(controller=self.controller, model=self.model, table=self)
            # search_equipment.open()
        elif self.current_table_id == 3:
            search_tech_inspection = SearchPopupTechInspection(controller=self.controller, model=self.model)
            search_tech_inspection.open()
        elif self.current_table_id == 4:
            search_employee = SearchPopupEmployee(controller=self.controller, model=self.model, table=self)
            search_employee.open()



    def return_controller(self):
        return self.controller
    def return_model(self):
        return self.model



Builder.load_file(os.path.join(os.path.dirname(__file__), "screen.kv"))