from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivymd.uix.pickers import MDDatePicker




class AddPopupWorkArea(Popup, Widget):
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

class AddPopupEquipment(Popup, Widget):
    """
        Popup for EQUIPMENT table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    def set_equipment_number(self, number):
        self.controller.set_equipment_number(number)
    def set_equipment_name(self, name):
        self.controller.set_equipment_name(name)
    def set_equipment_type(self, type):
        self.controller.set_equipment_type(type)
    def add_equipment(self):
        self.controller.add_equipment()
        self.table.to_table_equipment()


class AddPopupTechInspection(Popup, Widget):
    """
        Popup for TECH INSPECTION table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    def set_tech_inspection_date(self, date):
        self.controller.set_tech_inspection_date(date)

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

    def choose_tech_inspection_date(self):
        date_dialog = MDDatePicker(min_year=2010, max_year=2022)
        date_dialog.bind(on_save=self.set_tech_inspection_date_calendar)
        date_dialog.open()
    def set_tech_inspection_date_calendar(self, instance, value, date_range):
        self.set_tech_inspection_date(str(value))
        self.ids.add_tech_inspection_date.text = str(value)


class AddPopupEmp(Popup, Widget):
    """
        Popup for EMPLOYEE table
        """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.model = model
        self.controller = controller
        self.table = table

    # set employee's number
    def set_employee_number(self, employee_number):
        self.controller.set_employee_number(employee_number)

    # set employee's fio
    def set_employee_fio(self, employee_fio):
        self.controller.set_employee_fio(employee_fio)

    # set employee's job
    def set_employee_job(self, employee_job):
        self.controller.set_employee_job(employee_job)

    # insert employee information into DB
    def add_employee(self):
        # add employee to DB
        self.controller.add_employee()
        # tell the table to update
        self.table.to_table_employee()