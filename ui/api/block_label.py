from kivy.uix.label import Label


class BlockLabel(Label):
    scale_factor = 1
    factor = dimension = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(width=self.on_texture_size)

    def on_texture_size(self, *args):
        if not self.factor:
            self.factor = [self.font_size / self.texture_size[0], self.font_size / self.texture_size[1]]

        if not self.dimension:
            self.dimension = 1 if self.texture_size[0] * self.size[1] < self.texture_size[1] * self.size[0] else 0

        self.font_size = self.size[self.dimension] * self.scale_factor * self.factor[self.dimension]
