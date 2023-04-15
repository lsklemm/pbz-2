from Model.screen import Model
from View.screen import MainScreen
from View.search_popups import FoundPopupTechInspection, FoundPopupSearchEmployee, FoundPopupEquipment

class Controller:
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

        self.model = Model(controller = self, cursor = self.cursor, connection = self.connection)
        self.main_view = MainScreen(controller = self, model = self.model)

        self.currect_data_input = True

    # ----------------------ANIMALS ----------------------------

    def set_persona_animal_number(self, number):
        self.model.set_persona_animal_number(number)

    def set_personal_old_animal_number(self, number):
        self.model.set_personal_old_animal_number(number)

    def set_animals_name(self, name):
        self.model.set_animals_name(name)

    def set_birthday(self, birthday):
        self.model.set_birthday(birthday)

    def set_gender(self, gender):
        self.model.set_gender(gender)

    def set_Number_SMOTR(self, smotr):
        self.model.set_Number_SMOTR(smotr)

    def set_Number_VET(self, vet):
        self.model.set_Number_VET(vet)

    def set_diet(self, diet):
        self.model.set_diet(diet)

    def set_area(self, area):
        self.model.set_area(area)

    def add_animals(self):
        self.model.add_work_area()

    def remove_animals(self, number):
        self.model.remove_work_area(number)

    def update_animals(self):
        self.model.update_work_area()

    def get_table_animals(self):
        return self.model.get_table_animals()

    # ----------------------WORKER ---------------------------------------

    def set_worker_personal_number(self, worker_number):
        self.model.set_worker_personal_number(worker_number)

    def set_worker_old_personal_number(self, number):
        self.model.set_worker_old_personal_number(number)

    def set_worker_name(self, worker_name):
        if self.is_string(worker_name) and not self.is_empty(worker_name) and len(worker_name) <= 50:
            self.model.set_worker_name(worker_name)

    def set_worker_post(self, worker_post):
        if self.is_string(worker_post) and not self.is_empty(worker_post) and len(worker_post) <= 100:
            self.model.set_worker_post(worker_post)

    def set_worker_birthday(self, worker_birthday):
        self.model.set_worker_birthday(worker_birthday)

    def set_worker_number_of_telefhone(self, number_of_telephone):
        self.model.set_worker_number_of_telefhone(number_of_telephone)

    def set_worker_marital_status(self, worker_status):
        self.model.set_worker_marital_status(worker_status)

    def add_worker(self):
        self.model.add_worker()

    def remove_worker(self, number):
        self.model.remove_worker(number)

    def delete_worker(self):
        self.model.delete_worker()

    def update_worker(self):
        self.model.update_worker()

    # -----------------------FAMILY ------------------------

    def set_personal_number_wife(self, wife):
        self.model.set_personal_number_wife(wife)

    def set_personal_number_husband(self, husband):
        self.model.set_personal_number_husband(husband)

    # -----------------------DIET ------------------------

    def set_diet_number(self, number):
        self.model.set_diet_number(number)

    def set_diet_type(self, type):
        self.model.set_diet_type(type)

    def set_diet_name(self, name):
        self.model.set_diet_name(name)

    # -----------------------AREA ------------------------

    def set_area_number(self, number):
        self.model.set_diet_number(number)

    def set_area_name(self, aname):
        self.model.set_diet_type(aname)

    def set_area_specif(self, specif):
        self.model.set_diet_name(specif)

    # -----------------------BIRDS ------------------------

    def set_birds_number(self, number):
        self.model.set_birds_number(number)

    def set_birds_type(self, type):
        self.model.set_birds_type(type)

    def set_birds_wintering1(self, w1):
        self.model.set_birds_wintering1(w1)

    def set_birds_wintering2(self, w2):
        self.model.set_birds_wintering2(w2)

    # -----------------------REPTILE ------------------------

    def set_reptile_number(self, number):
        self.model.set_reptile_number(number)

    def set_reptile_type(self, type):
        self.model.set_reptile_type(type)

    def set_tempreture(self, temp):
        self.model.set_tempreture(temp)

    def set_slumber1(self, s1):
        self.model.set_slumber1(s1)

    def set_slumber2(self, s2):
        self.model.set_slumber2(s2)

    # -----------------------MAMMALS ------------------------

    def set_mammals_number(self, number):
        self.model.set_mammals_number(number)

    def set_mammals_type(self, type):
        self.model.set_mammals_type(type)

    def get_screen(self):
        return self.main_view

    # # ----------------- SEARCH --------------------------------
    # def set_search_tech_inspection_equipment_number(self, number):
    #     self.model.set_search_tech_inspection_equipment_number(number)
    # def search_tech_inspection(self):
    #     self.model.search_tech_inspection()
    # def show_table_search_tech_inspection(self):
    #     FoundPopupTechInspection(controller=self, model = self.model).open()
    #
    # def search_employee_date(self):
    #     self.model.search_employee()
    # def set_search_employee_date(self, date):
    #     self.model.set_search_employee_date(date)
    # def get_search_employee_date(self):
    #     self.model.return_table_search_employee()
    # def show_table_search_emeployee(self):
    #     FoundPopupSearchEmployee(controller=self, model=self.model).open()
    #
    # def set_search_equipment_date(self, date):
    #     self.model.set_search_equipment_date(date)
    # def search_equipment(self):
    #     self.model.search_equipment()
    # def show_table_search_equipment(self):
    #     FoundPopupEquipment(controller=self, model=self.model).open()
    #
    #
    # # ---------------------------------------------------------
    # # returns True if str, False if it is not
    # def is_string(self, string):
    #     numbers = '1234567890*+-/|,:;_&^%$#@=\'\"'
    #     for i in string:
    #         for j in numbers:
    #             if i == j:
    #                 return False
    #     return True
    #
    # # returns True if empty, False if it is not
    # def is_empty(self, string):
    #     if len(string) == 0:
    #         return True
    #     else:
    #         return False
    #
    #
    #
    # def get_table_work_area(self):
    #     return self.model.get_table_work_area()
    # def get_table_tech_inspection(self):
    #     return self.model.get_table_tech_inspection()
    # def get_table_equipment(self):
    #     return self.model.get_table_equipment()
    # def get_table_emp(self):
    #     return self.model.get_table_emp()
    def get_screen(self):
        return self.main_view