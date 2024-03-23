#Source: https://stackoverflow.com/questions/65432781/kivy-multiprocessing-throws-a-typeerror
from kivy.app import App
from kivy.uix.button import Button
from multiprocessing import Process

class myApp(App):
    def f(self):
        print('test')

    def test(self, caller):
        pr = Process(target=self.f)
        pr.start()

    def build(self):
        btn = Button(text='Go')
        btn.bind(on_press=self.test)

        return btn

if __name__ == '__main__':
    myApp().run()