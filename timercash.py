from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton, MDRoundFlatButton
from kivy.lang import Builder
from input_field import *
from contact_form import SendEmail
from clock import startTime
from worker import Worker
from button_style import *
import kivy

kivy.require('2.3.0')


class TimerCash(MDApp):
    
    def build(self):
        theme = "Light"
        self.theme_cls.theme_style = "Light"
        self.username = Builder.load_string(username_helper)
        self.nome_datore = Builder.load_string(name_datore_helper)
        self.datore = Builder.load_string(datore_helper)
        self.specifica = Builder.load_string(specifica_helper)
        self.name_receiver = Builder.load_string(name_helper)
        self.surname = Builder.load_string(surname_helper)
        self.paga = Builder.load_string(paga_helper)
        
        self.worker = []

        self.file = ""
        
        self.receiver_name = ""
        self.started = False
        self.added = False
        
        self.add_worker_btn = Builder.load_string(add_worker_btn)

        self.start_btn = Builder.load_string(start_btn)
        
        self.end_btn = Builder.load_string(end_btn)

        screen = Screen()
        
        screen.add_widget(self.username)
        screen.add_widget(self.name_receiver)
        screen.add_widget(self.surname)
        screen.add_widget(self.datore)
        screen.add_widget(self.nome_datore)
        screen.add_widget(self.specifica)
        screen.add_widget(self.paga)
        screen.add_widget(self.add_worker_btn)
        
        screen.add_widget(self.start_btn)
        screen.add_widget(self.end_btn)
        
        return screen
    
    def add_worker(self):
        temp = Worker(self.name_receiver.text, self.surname.text, self.username.text, self.nome_datore.text, self.datore.text, self.specifica.text, self.paga.text)
        
        if not self.worker:
        
            self.worker.append(temp.lista)

            self.added = True
        
        else:
            self.worker[0] = temp.lista     
        
        print(self.worker)
        
    def start(self):
        
        if not self.started and self.added:
        
            SendEmail(False, self.worker[0], 0)

            self.start_time = startTime()
            
            self.started = True
        elif not self.added:
            pass
            #print("Worker not added")
        else:
            pass
            #print("Already Started")
        
    def stop(self):
        
        if self.started:
        
            self.end_time = startTime()
            
            pay = ( (self.end_time - self.start_time) / 3600 ) * float(self.worker[0][6])
            
            SendEmail(True, self.worker[0], pay)
            
            self.started = False
        else:
            pass
            #print("Not Started Yet")