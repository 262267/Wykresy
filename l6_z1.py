
import matplotlib.pyplot as plt
import numpy as np
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)
        
        # set columns 
        self.cols = 2
        # Add widgets
        self.add_widget(Label(text="function: "))
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)
        self.add_widget(Label(text="set x-axis_min: "))
        self.xaxis_min = TextInput(multiline=False)
        self.add_widget(self.xaxis_min)
        self.add_widget(Label(text="set x-axis_max: "))
        self.xaxis_max = TextInput(multiline=False)
        self.add_widget(self.xaxis_max)
        self.add_widget(Label(text="set y-axis_min: "))
        self.yaxis_min = TextInput(multiline=False)
        self.add_widget(self.yaxis_min)
        self.add_widget(Label(text="set y-axis_max: "))
        self.yaxis_max = TextInput(multiline=False)
        self.add_widget(self.yaxis_max)
        self.add_widget(Label(text="graph title: "))
        self.graph_title = TextInput(multiline=False)
        self.add_widget(self.graph_title)
        self.add_widget(Label(text="x-axis title: "))
        self.xaxis_title = TextInput(multiline=False)
        self.add_widget(self.xaxis_title)
        self.add_widget(Label(text="y-axis title: "))
        self.yaxis_title = TextInput(multiline=False)
        self.add_widget(self.yaxis_title)
        self.add_widget(Label(text="legend? (yes/no)"))
        self.legend = CheckBox(active=False)
        self.legend.bind(active=self.show_legend)
        self.add_widget(self.legend)
     
        #optional buttons for building a function pattern
        
        self.sum_of = Button(text="+", size_hint_y = None, height = 30)
        self.sum_of.bind(on_press=self.press)
        self.add_widget(self.sum_of)
        self.minus = Button(text="-", size_hint_y = None, height = 30)
        self.minus.bind(on_press=self.press)
        self.add_widget(self.minus)
        self.division = Button(text="/", size_hint_y = None, height = 30)
        self.division.bind(on_press=self.press)
        self.add_widget(self.division)
        self.multiplication = Button(text="*", size_hint_y = None, height = 30)
        self.multiplication.bind(on_press=self.press)
        self.add_widget(self.multiplication)
        self.left_bracket = Button(text="(", size_hint_y = None, height = 30)
        self.left_bracket.bind(on_press=self.press)
        self.add_widget(self.left_bracket)
        self.right_bracket = Button(text=")", size_hint_y = None, height = 30)
        self.right_bracket.bind(on_press=self.press)
        self.add_widget(self.right_bracket)
        self.square_power = Button(text="x**2", size_hint_y=None, height=30)
        self.square_power.bind(on_press=self.press)
        self.add_widget(self.square_power)
        self.third_power = Button(text="x**3", size_hint_y=None, height=30)
        self.third_power.bind(on_press=self.press)
        self.add_widget(self.third_power)
        self.np_sinx = Button(text="np.sin(x)", size_hint_y=None, height=30)
        self.np_sinx.bind(on_press=self.press)
        self.add_widget(self.np_sinx)
        self.np_cosx = Button(text="np.cos(x)", size_hint_y=None, height=30)
        self.np_cosx.bind(on_press=self.press)
        self.add_widget(self.np_cosx)
        self.math_tan = Button(text="np.tan(x)", size_hint_y=None, height=30)
        self.math_tan.bind(on_press=self.press)
        self.add_widget(self.math_tan)
        self.abs_value = Button(text="abs(x)", size_hint_y=None, height=30)
        self.abs_value.bind(on_press=self.press)
        self.add_widget(self.abs_value)
        self.draw = Button(text="draw function")
        self.draw.bind(on_press=self.plot_draw)
        self.add_widget(self.draw)
        self.clear = Button(text="clear function")
        self.clear.bind(on_press=self.clear_fuction)
        self.add_widget(self.clear)
    
    def plot_draw(self, button):
        if float(self.xaxis_max.text) > float(self.xaxis_min.text):
            d = self.name.text.splitlines()
            x = np.linspace(float(self.xaxis_min.text), float(self.xaxis_max.text), 100)
            for i in d:
                plt.plot(x, eval(i), label = "%s" %i)
            if self.add_legend.text == "added":
                plt.legend()
            else: 
                pass
            plt.xlim(float(self.xaxis_min.text), float(self.xaxis_max.text))
        else:
            raise ValueError("replace value self.xaxis_max.text with value self.xaxis_min.text!")
        if float(self.yaxis_max.text) > float(self.yaxis_min.text):
            plt.ylim(float(self.yaxis_min.text), float(self.yaxis_max.text))
        else:
            raise ValueError("replace value self.yaxis_max.text with value self.yaxis_min.text!")

        if self.graph_title.text:
            plt.title(self.graph_title.text)
        if self.xaxis_title.text:
            plt.xlabel(self.xaxis_title.text)
        if self.yaxis_title.text:
            plt.ylabel(self.yaxis_title.text)
            plt.show()
        

    def clear_fuction(self, button):
        self.name.text = ''
        self.xaxis_min.text = ''
        self.xaxis_max.text = ''
        self.yaxis_min.text = ''
        self.yaxis_max.text = ''
        self.graph_title.text = ''
        self.xaxis_title.text = ''
        self.yaxis_title.text = ''


    def show_legend(self, checkbox, isactive):
        if isactive:
            self.add_legend = TextInput(text="added")
        else:
            self.add_legend = TextInput(text="unadded")


    def press(self, button):
        sum_of = self.name.text
        minus = self.name.text
        division = self.name.text
        multiplication = self.name.text
        ln_logarithm = self.name.text
        left_bracket = self.name.text
        right_bracket = self.name.text
        eulier = self.name.text
        square_power = self.name.text
        third_power = self.name.text
        root = self.name.text
        log = self.name.text
        np_sinx = self.name.text
        np_cosx = self.name.text
        math_pi = self.name.text
        math_tan = self.name.text
        self.name.text = f"{sum_of}{button.text}"
        self.name.text = f"{minus}{button.text}"
        self.name.text = f"{division}{button.text}"
        self.name.text = f"{multiplication}{button.text}"
        self.name.text = f"{ln_logarithm}{button.text}"
        self.name.text = f"{left_bracket}{button.text}"
        self.name.text = f"{right_bracket}{button.text}"
        self.name.text = f"{eulier}{button.text}"
        self.name.text = f"{square_power}{button.text}"
        self.name.text = f"{third_power}{button.text}"
        self.name.text = f"{root}{button.text}"
        self.name.text = f"{log}{button.text}"
        self.name.text = f"{np_sinx}{button.text}"
        self.name.text = f"{np_cosx}{button.text}"
        self.name.text = f"{math_pi}{button.text}"
        self.name.text = f"{math_tan}{button.text}"
        


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()