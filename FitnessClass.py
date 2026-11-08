from Trainer import Trainer
from Member import Member
from Subscription import Subscription

class FitnessClass:
    def __init__(self, title, trainer: Trainer, capacity):
        self.title = title
        self.trainer = trainer
        self.capacity = capacity
        self.enrolled_members: list[Member] = []

    def enroll(self, member: Member):
        if len(self.enrolled_members) >= self.capacity:
            print(f'Cannot enroll {member.name}: Class is full')
            return False
        if not member.subscription or not member.subscription.can_attend():
            print(f'Cannot enroll {member.name}: Invalid or depleted subscription')
            return False
        
        member.subscription.use_entry()
        member.record_attendance()
        self.enrolled_members.append(member)
        print(f"Successfully enrolled {member.name} in {self.title}.")
        return True