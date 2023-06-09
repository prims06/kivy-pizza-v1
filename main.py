from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import  CoverBehavior
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "chevre, emmental, brie, comté", 9.5, False),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons", 10, True),
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.get_dictionary() for pizza in self.pizzas]

with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())
class PizzaApp(App):
    def build(self):
        return MainWidget()

PizzaApp().run()