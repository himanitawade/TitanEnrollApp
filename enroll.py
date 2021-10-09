from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from databaseconnection import getlistofavailablecourses


class MainApp(MDApp):
    def getRowData(self, dbList): 
        data = []
		#append each row of data fetched from db into an array
        for i in dbList:
            data.append(i)
        return data

    def build(self):
        # Define Screen
        screen = Screen()
		#connect to db and get the list of available courses
        dbList = getlistofavailablecourses(
            'Computer Science', 'Master in Computer Science')
        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},#position
            size_hint=(0.9, 0.6),						#size
            use_pagination=True,						#pagination
            rows_num=3,									#initial no for pagination
            pagination_menu_height='240dp',				#menu height for pagination
            pagination_menu_pos="auto",					#menu position
            background_color=[1, 0, 0, .5],				#backgnd color
			#define column data
            column_data=[
                ("ClassId", dp(30)),
                ("CourseID", dp(30)),
                ("Course Name", dp(30)),
                ("Prefessor Name", dp(30)),
                ("Timeslot", dp(30)),
                ("Remaining Slots", dp(30))
            ],
			#define row data
            row_data=self.getRowData(dbList)
        )

        # Bind the table
        table.bind(on_row_press=self.checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # Add table widget to screen
        screen.add_widget(table)
        return screen

    # Function for row presses
    def checked(self, instance_table, instance_row):
		#get the dblist
        dbList = self.getRowData(getlistofavailablecourses('Computer Science', 'Master in Computer Science'))
        if(instance_row.index/6>=0):
			#get the selecetd row value
            print(dbList[int(instance_row.index/6)])


MainApp().run()
