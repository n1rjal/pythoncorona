from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from app import userdata
from app import notify
from tocsv import csv

class CustomWidget(Widget):
    last_name_text_input = ObjectProperty()
    ego = NumericProperty()
    surname = StringProperty()
    
    def getcsv(self):
        csv()

    def submit_surname(self):
        self.name = self.last_name_text_input.text
        print("Assign surname: {}".format(self.name))
        self.title,self.body=userdata(self.name)
        self.name = ''
        notify(title=self.title,body=self.body)
          

class CustomWidgetApp(App):
    def build(self):
        return CustomWidget()

if __name__ == "__main__":
    CustomWidgetApp().run()

