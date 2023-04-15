from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class RemovePopupWorkArea(Popup, Widget):
    """
    Class for POPUP to remove WORK AREA
    """
    def __init__(self, controller, model, table,**kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table





    def set_unique_work_area(self, unique_info):
        self.ids.remove_work_area_number.text = str(unique_info[0])
        self.ids.remove_work_area_name.text = unique_info[1]

    def remove_work_area(self):
        self.controller.remove_work_area(self.ids.remove_work_area_number.text)
        self.table.to_table_work_area()

class RemovePopupEquipment(Popup, Widget):
    """
    Class for POPUP to remove EQUIPMENT
    """
    def __init__(self, controller, model, table, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table

        self.unique_number = 0

    def set_unique_equipment(self, unique_info):
        self.ids.remove_equipment_number.text = str(unique_info[0])
        self.ids.remove_equipment_name.text = unique_info[1]
        self.ids.remove_equipment_type.text = unique_info[2]

    def remove_equipment(self):
        self.controller.remove_equipment(self.ids.remove_equipment_number.text)
        self.table.to_table_equipment()

class RemovePopupTechInspection(Popup, Widget):
    """
    Class for POPUP to remove TECH INSPECTION
    """
    def __init__(self,controller,model,table,**kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table

        self.unique_number = 0

    def set_unique_tech_inspection(self, unique_info):
        self.ids.remove_tech_inspection_date.text = unique_info[0]
        self.ids.remove_tech_inspection_result.text = unique_info[1]
        self.ids.remove_tech_inspection_worker_fio.text = unique_info[2]
        self.ids.remove_tech_inspection_reason.text = unique_info[3]

    def remove_tech_inspection(self):
        self.controller.remove_tech_inspection(self.ids.remove_tech_inspection_date.text)
        self.table.to_table_tech_inspection()

class RemovePopupEmployee(Popup, Widget):
    def __init__(self, controller,model,table,**kw):
        super().__init__(**kw)
        self.controller = controller
        self.model = model
        self.table = table

        self.unique_number = 0

    def set_unique_employee(self, unique_info):
        self.ids.remove_employee_number.text = str(unique_info[0])
        self.ids.remove_employee_fio.text = unique_info[1]
        self.ids.remove_employee_job.text = unique_info[2]



    def remove_employee(self):
        self.controller.remove_employee(self.ids.remove_employee_number.text)
        self.table.to_table_employee()