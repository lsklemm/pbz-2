from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivymd.uix.pickers import MDDatePicker


class UpdatePopupWorkArea(Popup, Widget):
    """
    Class for POPUP to remove WORK AREA
    """
    def __init__(self, controller, model, table,**kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table






    def set_previous_info(self, unique_info):
        self.set_work_area_number(unique_info[0])
        self.set_work_area_name(unique_info[1])
        self.set_work_area_old_number(unique_info[0])
        self.set_work_area_equipment_type(unique_info[2])
        self.ids.update_work_area_number.text = str(unique_info[0])
        self.ids.update_work_area_name.text = unique_info[1]
        self.ids.update_work_area_equipment_type.text = unique_info[2]

    def update_work_area(self):
        self.controller.update_work_area()
        self.table.to_table_work_area()

    def set_work_area_number(self, number):
        self.controller.set_work_area_number(number)
    def set_work_area_old_number(self, number):
        self.controller.set_work_area_old_number(number)
    def set_work_area_name(self, name):
        self.controller.set_work_area_name(name)
    def set_work_area_equipment_type(self, type):
        self.controller.set_work_area_equipment_type(type)

class UpdatePopupEquipment(Popup, Widget):
    """
    Class for POPUP to remove EQUIPMENT
    """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table

        self.unique_number = 0

    def set_previous_info(self, unique_info):
        self.set_equipment_old_number(unique_info[0])
        self.set_equipment_name(unique_info[1])
        self.set_equipment_type(unique_info[2])
        self.ids.update_equipment_number.text = str(unique_info[0])
        self.ids.update_equipment_name.text = unique_info[1]
        self.ids.update_equipment_type.text = unique_info[2]

    def set_equipment_number(self, number):
        self.controller.set_equipment_number(number)
    def set_equipment_old_number(self, number):
        self.controller.set_equipment_old_number(number)
    def set_equipment_name(self, name):
        self.controller.set_equipment_name(name)
    def set_equipment_type(self, type):
        self.controller.set_equipment_type(type)

    def update_equipment(self):
        self.controller.update_equipment()
        self.table.to_table_equipment()

class UpdatePopupTechInspection(Popup, Widget):
    """
    Class for POPUP to remove TECH INSPECTION
    """
    def __init__(self,controller,model,table,**kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table

        self.unique_number = 0

    def set_previous_info(self, unique_info):
        self.set_tech_inspection_old_date(unique_info[0])
        self.set_tech_inspection_equipment_number(unique_info[1])
        self.set_tech_inspection_result(unique_info[2])
        self.set_tech_inspection_worker_fio(unique_info[3])
        self.set_tech_inspection_reason(unique_info[4])
        self.ids.update_tech_inspection_date.text = unique_info[0]
        self.ids.update_tech_inspection_equipment_number.text = unique_info[1]
        self.ids.update_tech_inspection_result.text = unique_info[2]
        self.ids.update_tech_inspection_worker_fio.text = unique_info[3]
        self.ids.update_tech_inspection_reason.text = unique_info[4]

    def choose_tech_inspection_date(self):
        date_dialog = MDDatePicker(min_year=2010, max_year=2022)
        date_dialog.bind(on_save=self.set_tech_inspection_date_calendar)
        date_dialog.open()
    def set_tech_inspection_date_calendar(self, instance, value, date_range):
        self.set_tech_inspection_date(str(value))
        self.ids.update_tech_inspection_date.text = str(value)

    def update_tech_inspection(self):
        self.controller.update_tech_inspection()
        self.table.to_table_tech_inspection()

    def set_tech_inspection_date(self, date):
        self.controller.set_tech_inspection_date(date)
    def set_tech_inspection_old_date(self, date):
        self.controller.set_tech_inspection_old_date(date)
    def set_tech_inspection_equipment_number(self, number):
        self.controller.set_tech_inspection_equipment_number(number)

    def set_tech_inspection_result(self, result):
        self.controller.set_tech_inspection_result(result)

    def set_tech_inspection_worker_fio(self, worker_fio):
        self.controller.set_tech_inspection_worker_fio(worker_fio)

    def set_tech_inspection_reason(self, reason):
        self.controller.set_tech_inspection_reason(reason)

    def add_tech_inspection(self):
        self.controller.add_tech_inspection()
        self.table.to_table_tech_inspection()



class UpdatePopupEmployee(Popup, Widget):
    def __init__(self, controller,model,table,**kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table

        self.unique_number = 0

    def set_previous_info(self, unique_info):
        self.set_employee_number(unique_info[0])
        self.set_employee_old_number(unique_info[0])
        self.set_employee_fio(unique_info[1])
        self.set_employee_job(unique_info[2])
        self.ids.update_employee_number.text = str(unique_info[0])
        self.ids.update_employee_fio.text = unique_info[1]
        self.ids.update_employee_job.text = unique_info[2]



    def update_employee(self):
        self.controller.update_employee()
        self.table.to_table_employee()

    def set_employee_number(self, number):
        self.controller.set_employee_number(number)
    def set_employee_old_number(self,number):
        self.controller.set_employee_old_number(number)
    def set_employee_job(self, job):
        self.controller.set_employee_job(job)
    def set_employee_fio(self, fio):
        self.controller.set_employee_fio(fio)