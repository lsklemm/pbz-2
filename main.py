from kivymd.app import MDApp
from Controller.screen import Controller
from db import cur, con
import os
from kivy.lang import Builder

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controller(cursor = cur, connection = con)

    def build(self):
        return self.controller.get_screen()


MyApp().run()



# cur.execute("select * from оборудование")
# rows = cur.fetchall()
# for r in rows:
#     print(r[0],r[1],r[2])
#
# cur.execute("insert into оборудование(номер,название,тип) values(12,'Хаю','хай')")
# con.commit()
# cur.close()
# con.close()