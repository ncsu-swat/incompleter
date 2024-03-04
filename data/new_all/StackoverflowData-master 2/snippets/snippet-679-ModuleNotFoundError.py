#Source: https://stackoverflow.com/questions/58591221/kivy-attribute-error-object-has-no-attribute-trying-to-connect-widgets-in-kv
# keysigchooser.py
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

chrom_scale = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
chrom_scale2 = ['C', 'C/D', 'D', 'D/E', 'E', 'F', 'F/G', 'G', 'G/A', 'A', 'A/B', 'B']


class ModeChooser(FloatLayout):
    pass


class RootNoteChooser(FloatLayout):
    note_idx = NumericProperty(0)

    def increment_note_idx(self):
        self.note_idx = (self.note_idx + 1) % 12

    def decrement_note_idx(self):
        self.note_idx = (self.note_idx - 1) % 12

    def on_note_idx(self, instance, value):
        self.note_text.text = chrom_scale[self.note_idx]


class KeySigChooserContainer(FloatLayout):
    def on_size(self, instance, value):
        target_ratio = 60/20
        width, height = self.size
        # check which size is the limiting factor
        if width / height > target_ratio:
            # window is "wider" than targeted, so the limitation is the height.
            self.ids.box.height = height
            self.ids.box.width = height * target_ratio
        else:
            self.ids.box.width = width
            self.ids.box.height = width / target_ratio


class KeySigChooserApp(App):
    def build(self):
        return KeySigChooserContainer()


if __name__ == "__main__":
    KeySigChooserApp().run()