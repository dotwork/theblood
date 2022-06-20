def __run():
    """
    This is the while loop to copy over to the micropython device
    """
    import board
    import adafruit_msa301
    import adafruit_midi
    import usb_midi
    from composer.translators.accelerometer import AccelerometerTranslator, AccelerometerStrategy
    from the_blood.models import Key

    i2c = board.I2C()  # uses board.SCL and board.SDA
    msa = adafruit_msa301.MSA301(i2c)
    msa.enable_tap_detection()

    translator = AccelerometerTranslator(AccelerometerStrategy, Key('Bb'), bpm=120)
    midi_controller = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

    midi_note = None
    while True:
        translator.receive(msa)
        if not midi_note:
            midi_note = translator.translate()
            start_command = midi_note.get_start_command()
            midi_controller.send(start_command)
            print(start_command)
        else:
            end_command = midi_note.get_end_command()
            if end_command:
                midi_controller.send(end_command)
                print(end_command)
                midi_note = None
