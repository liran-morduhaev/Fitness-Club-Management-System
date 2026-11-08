from FitnessClass import FitnessClass
from Member import Member
from MonthlySubscription import MonthlySubscription
from PunchCardSubscription import PunchCardSubscription
from Trainer import Trainer

if __name__ == "__main__":
  # 1. Create trainer and fitness class
  trainer = Trainer("T01", "Alex Rivers", "050-1111111", "Yoga", 120.0)
  yoga_class = FitnessClass("Morning Yoga", trainer, capacity=2)

  # 2. Create members
  dana = Member("M01", "Dana", "054-1234567")
  ron = Member("M02", "Ron", "052-7654321")

  # 3. Assign subscriptions (Polymorphism)
  dana.subscription = MonthlySubscription()
  ron.subscription = PunchCardSubscription(entries=1)

  # 4. First enrollment round
  print("--- First Round of Enrollments ---")
  yoga_class.enroll(dana)  # Successful
  yoga_class.enroll(ron)  # Successful (used up his only entry)

  # 5. Test restrictions
  print("\n--- Testing Edge Cases & Restrictions ---")
  yoga_class.enroll(ron)  # Fails: punch card is now depleted

  yossi = Member("M03", "Yossi", "050-9999999")
  yossi.subscription = MonthlySubscription()
  yoga_class.enroll(yossi)  # Fails: class capacity (2) is full

  # 6. Verify encapsulation
  print("\n--- Member Attendance Stats ---")
  print(f"{dana.name} - Total Attendances: {dana.attendance_count}")
  print(f"{ron.name} - Total Attendances: {ron.attendance_count}")