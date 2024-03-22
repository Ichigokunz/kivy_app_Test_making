from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
 
class ScrButton(Button):
   def __init__(self, screen, direction='right', goal='main', **kwargs):
       super().__init__(**kwargs)
       self.screen = screen
       self.direction = direction
       self.goal = goal
   def on_press(self):
       self.screen.manager.transition.direction = self.direction
       self.screen.manager.current = self.goal
      
class MainScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
       hl = BoxLayout()
       txt = Label(text= 'FastHand : Reflect')
 
       vl.add_widget(ScrButton(self, direction='down', goal='first', text="Play"))
       vl.add_widget(ScrButton(self, direction='left', goal='second', text="Account linking"))
       vl.add_widget(ScrButton(self, direction='up', goal='third', text="Settings"))
       vl.add_widget(ScrButton(self, direction='right', goal='fourth', text="Exit"))
 
       hl.add_widget(txt)
       hl.add_widget(vl)
       self.add_widget(hl)
 
class FirstScr(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
       
       self.time_left = 0
       self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
    
       self.label = Label(text=str(self.time_left))
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
       
       self.start_button = Button(text='Unranked', on_press=self.start_timer)
       self.start_button2 = Button(text='Ranked : Gold Matching', on_press=self.start_timer)
       self.stop_button = Button(text='Cancel', on_press=self.stop_timer)
       btn_back = ScrButton(self, direction='up', goal='main', text="Back", size_hint=(.5, 1), pos_hint={'right': 1})
       
       self.layout.add_widget(self.start_button)
       self.layout.add_widget(self.start_button2)
       self.layout.add_widget(self.stop_button)
       vl.add_widget(btn_back)
       self.add_widget(vl)
       
       return self.layout
       
    
    def start_timer(self, instance):
        Clock.schedule_interval(self.update_timer,"Searching A Match For", 1,"Second")

    def stop_timer(self, instance):
        Clock.unschedule(self.update_timer)

    def update_timer(self, dt):
        self.time_left += 1  
        self.label.text = str(self.time_left)
        
    def update_timer(self, dt):
        self.time_left += 1  
        self.label.text = str(self.time_left)
        
    def next_screen(self, *args):
        self.manager.current = 'second'
 
class SecondScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical')
 
       self.txt = Label(text= '') 
       vl.add_widget(self.txt)

       hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
       lbl1 = Label(text='Enter your Username & Pass:', halign='right')
       self.input = TextInput(multiline=False)
       self.input2 = TextInput(multiline=False)

       hl_0.add_widget(lbl1)
       hl_0.add_widget(self.input)
       hl_0.add_widget(self.input2)
       vl.add_widget(hl_0)
 
       
       hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
       btn_false = Button(text="OK!")
       btn_back = ScrButton(self, direction='right', goal='main', text="Back")

       hl.add_widget(btn_false)
       hl.add_widget(btn_back)
       vl.add_widget(hl)
       self.add_widget(vl)
       btn_false.on_press = self.change_text
 
   def change_text(self):
       self.txt.text = 'You Just Disconnected from the internet so It did not work , try again later...'       
 
 
class ThirdScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       layout = BoxLayout(orientation='vertical')
       btn_back = ScrButton(self, direction='down', goal='main', text="back", size_hint=(1, None), height='40sp')
       test_label = Label(text = "Cant access the Settings file on your AppData Try To Restart, To Set Up Your Quality Of Game")
       layout.add_widget(test_label)
       layout.add_widget(btn_back)
       self.add_widget(layout)

class FourthScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', spacing=8)
       a = 'STARTING TO FORCE CLOSING THE PROGRAM ,' + 'CLOSING THE PROGRAM... , Failed to close the program , please close manually , code repeating for 20 times..... ' * 20 + '(The Exit Button Is Error , Try to Cancel and Try Again, Or Exit For Manually)'
 
       test_label = Label(text = "PROGRAM CLOSING LOG, THE APP GET BUGGED, BUT YOU CAN GO BACK",size_hint=(0.2,None))

       btn_back = ScrButton(self, direction='left', goal='main', text="Cancel", size_hint=(1, .2), pos_hint={'center-x': 0.5})
 
       self.label = Label(text=a, size_hint_y=None, font_size='24sp', halign='justify', valign='top')  
       self.label.bind(size=self.resize)
       self.scroll = ScrollView(size_hint=(1, 1))
       self.scroll.add_widget(self.label)

       vl.add_widget(test_label)
       vl.add_widget(btn_back)
       vl.add_widget(self.scroll)
       self.add_widget(vl)
 
   def resize(self, *args):
       self.label.text_size = (self.label.width, None)
       self.label.texture_update()
       self.label.height = self.label.texture_size[1]

class MyApp(App):
   def build(self):
       sm = ScreenManager()
       sm.add_widget(MainScr(name='main'))
       sm.add_widget(FirstScr(name='first'))
       sm.add_widget(SecondScr(name='second'))
       sm.add_widget(ThirdScr(name='third'))
       sm.add_widget(FourthScr(name='fourth'))
 
       return sm
 
if __name__ == '__main__':
    MyApp().run()


