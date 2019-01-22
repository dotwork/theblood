# def harmonically_equivalent_to(self, other):
# if not isinstance(other, (Pitch, Note)):
#     raise TypeError(f'Cannot compare type {type(self)} to type {type(other)}')
#
# if self.name == other.name:
#     return True
# else:
#     if other.natural_name == self.next_natural_note.natural_name:
#         if other.is_flat:
#             if self.is_standard_sharp:
#                 return True
#             elif self.name == B.name and other.name == C_flat.name:
#                 return True
#             elif self.name == E.name and other.name == F_flat.name:
#                 return True
#         elif self.is_sharp:
#             if self.name == B_sharp.name and other.name == C.name:
#                 return True
#             elif self.name == E_sharp.name and other.name == F.name:
#                 return True
#         elif self.is_double_sharp and other.is_natural:
#             return True
#     elif other.natural_name == self.previous_natural_note.natural_name:
#         if self.is_flat:
#             if other.is_standard_sharp:
#                 return True
#             elif self.name == C_flat.name and other.name == B.name:
#                 return True
#             elif self.name == F_flat.name and other.name == E.name:
#                 return True
#         elif other.is_sharp:
#             if self.name == C.name and other.name == B_sharp.name:
#                 return True
#             elif self.name == F.name and other.name == E_sharp.name:
#                 return True
#         elif self.is_double_flat and other.is_natural:
#             return True
#     return False
#


# ########################################################################
# def generate_note_names():
#     names = []
#
#     for natural_note in NATURAL_NOTES:
#         flat = Note(natural_note + "b")
#         if flat.is_standard_flat:
#             names.append(flat.name)
#
#         names.append(natural_note)
#
#         sharp = Note(natural_note + "#")
#         if sharp.is_standard_sharp:
#             names.append(sharp.name)
#
#     return tuple(names)
#
#
# NOTE_NAMES = generate_note_names()
#
# NOTES = (
#     A,
#     A_sharp,
#     B,
#     C,
#     C_sharp,
#     D,
#     D_sharp,
#     E,
#     F,
#     F_sharp,
#     G,
#     G_sharp,
# )
#
#


####################################################################
@property
def all_notes(self):
    notes = [self.root_note]
    for step in self.steps:
        semitones = int(step * 2)
        for semitone in range(semitones):
            next_note = self.get_next_note(notes)
            notes.append(next_note)
    return notes


####################################################################
def get_scale_degrees(self, *degrees):
    return [self.scale_degree(d) for d in degrees]


####################################################################
def scale_degree(self, degree):
    degree = int(degree)
    return self.notes[degree - 1]

    def get_next_from_double_flat(self, previous_note):
        next_flat = previous_note.next_natural_note.name + FLAT
        return Note(next_flat)

    def get_next_from_standard_flat(self, standard_flat):
        current_natural = standard_flat.natural_name
        return Note(current_natural)

    def get_next_from_standard_sharp(self, standard_sharp):
        next_natural = standard_sharp.next_natural_note.name
        return Note(next_natural)

    def get_next_from_double_sharp(self, double_sharp):
        next_sharp = double_sharp.next_natural_note.name + SHARP
        return Note(next_sharp)

    def get_next_note(self, notes):
        previous_note = notes[-1]

        if previous_note.is_double_flat:
            next_note = self.get_next_from_double_flat(previous_note)

        elif previous_note.is_standard_flat:
            next_note = self.get_next_from_standard_flat(previous_note)

        elif previous_note.is_natural:
            next_note = self.get_next_from_natural(previous_note)

        elif previous_note.is_standard_sharp:
            next_note = self.get_next_from_standard_sharp(previous_note)

        elif previous_note.is_double_sharp:
            next_note = self.get_next_from_double_sharp(previous_note)

        else:
            raise InvalidKeyError(f'Could not generate a diatonic scale from root note {self.root_note}.')

        return next_note






    ####################################################################
    def test_next__from_natural_to_flat(self):
        self.assertNotEqual(B_flat, A.next())
        self.assertEqual(B_flat, A.next(use_flats=True))

        self.assertNotEqual(D_flat, C.next())
        self.assertEqual(D_flat, C.next(use_flats=True))

        self.assertNotEqual(E_flat, D.next())
        self.assertEqual(E_flat, D.next(use_flats=True))

        self.assertNotEqual(G_flat, F.next())
        self.assertEqual(G_flat, F.next(use_flats=True))

        self.assertNotEqual(A_flat, G.next())
        self.assertEqual(A_flat, G.next(use_flats=True))

    ####################################################################
    def test_next__from_natural_to_natural(self):
        self.assertEqual(C, B.next())
        self.assertEqual(F, E.next())

    ####################################################################
    def test_next__from_sharp_to_natural(self):
        self.assertEqual(B, A_sharp.next())

        self.assertEqual(D, C_sharp.next())
        self.assertEqual(E, D_sharp.next())

        self.assertEqual(G, F_sharp.next())
        self.assertEqual(A, G_sharp.next())

    ####################################################################
    def test_next__from_sharp_to_sharp(self):
        self.assertEqual(C_sharp, B_sharp.next())
        self.assertEqual(F_sharp, E_sharp.next())

    ####################################################################
    def test_next__from_sharp_to_flat(self):
        self.assertNotEqual(C_flat, A_sharp.next())
        self.assertNotEqual(D_flat, B_sharp.next())
        self.assertNotEqual(F_flat, D_sharp.next())
        self.assertNotEqual(G_flat, E_sharp.next())

    ####################################################################
    def test_next__from_flat_to_natural(self):
        self.assertEqual(A, A_flat.next())
        self.assertEqual(B, B_flat.next())
        self.assertEqual(C, C_flat.next())
        self.assertEqual(D, D_flat.next())
        self.assertEqual(E, E_flat.next())
        self.assertEqual(F, F_flat.next())
        self.assertEqual(G, G_flat.next())

    ####################################################################
    def test_next__from_flat_to_sharp(self):
        self.assertNotEqual(B_sharp, C_flat.next())
        self.assertNotEqual(E_sharp, F_flat.next())

    ####################################################################
    def test_next__from_flat_to_flat(self):
        self.assertNotEqual(C_flat, B_flat.next())
        self.assertNotEqual(F_flat, E_flat.next())

    ####################################################################
    def test_previous__from_natural_to_sharp(self):
        self.assertEqual(G_sharp, A.previous(use_sharps=True))
        self.assertEqual(A_sharp, B.previous(use_sharps=True))
        self.assertEqual(C_sharp, D.previous(use_sharps=True))
        self.assertEqual(D_sharp, E.previous(use_sharps=True))
        self.assertEqual(F_sharp, G.previous(use_sharps=True))

    ####################################################################
    def test_previous__from_natural_to_flat(self):
        self.assertEqual(A_flat, A.previous())
        self.assertEqual(B_flat, B.previous())
        self.assertEqual(D_flat, D.previous())
        self.assertEqual(E_flat, E.previous())
        self.assertEqual(G_flat, G.previous())

    ####################################################################
    def test_previous__from_natural_to_natural(self):
        self.assertEqual(B, C.previous())
        self.assertEqual(E, F.previous())

    ####################################################################
    def test_previous__from_sharp_to_natural(self):
        self.assertEqual(A, A_sharp.previous())
        self.assertEqual(B, B_sharp.previous())
        self.assertEqual(C, C_sharp.previous())
        self.assertEqual(D, D_sharp.previous())
        self.assertEqual(E, E_sharp.previous())
        self.assertEqual(F, F_sharp.previous())
        self.assertEqual(G, G_sharp.previous())

    ####################################################################
    def test_previous__from_flat_to_natural(self):
        self.assertEqual(G, A_flat.previous())
        self.assertEqual(A, B_flat.previous())

        self.assertEqual(C, D_flat.previous())
        self.assertEqual(D, E_flat.previous())

        self.assertEqual(F, G_flat.previous())

    ####################################################################
    def test_previous__from_flat_to_sharp(self):
        self.assertEqual(A_sharp, C_flat.previous())
        self.assertEqual(D_sharp, F_flat.previous())

