

class Strategy:
    def get_pitch(self, *args, **kwargs):
        raise NotImplementedError()

    def get_velocity(self, *args, **kwargs):
        raise NotImplementedError()

    def get_note_value(self, *args, **kwargs):
        raise NotImplementedError()


class Translator:
    def translate(self):
        raise NotImplementedError()
