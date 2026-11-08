from FitnessClass import FitnessClass

class GymSchedule:

  def __init__(self):
    self.classes: list[FitnessClass] = []

  def add_class(self, fitness_class: FitnessClass) -> None:
    self.classes.append(fitness_class)

  def display_schedule(self) -> None:
    for fc in self.classes:
      print(f'{fc.title} (Trainer: {fc.trainer.name}) - Enrolled: ,{len(fc.enrolled_members)}/{fc.capacity}')

