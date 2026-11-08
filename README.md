# 🏋️‍♂️ Fitness Club Management System

A clean and scalable Python application designed to demonstrate the four fundamental principles of **Object-Oriented Programming (OOP)**: Inheritance, Polymorphism, Encapsulation, and Composition.

The system simulates gym operations, including trainer management, customer subscriptions, and class enrollments with strict validation rules.

---

## 🚀 Key OOP Principles Demonstrated

* **Inheritance:** 
  * `Person` serves as a base class containing shared attributes (`person_id`, `name`, `phone`).
  * `Member` and `Trainer` inherit from `Person` and extend functionality.
* **Polymorphism & Abstraction:** 
  * `Subscription` is an Abstract Base Class (`ABC`) enforcing core behaviors (`calculate_price`, `can_attend`, `use_entry`).
  * Subclasses `MonthlySubscription`, `PunchCardSubscription`, and `StudentSubscription` implement these methods uniquely.
* **Encapsulation:** 
  * `Member` keeps sensitive fields protected/private (`_balance`, `__attendance_count`).
  * Access is provided via controlled properties (`@property`) and state-modifying methods (`record_attendance`, `deposit`).
* **Composition:** 
  * `FitnessClass` contains references to an assigned `Trainer` and a dynamic list of enrolled `Member` instances.
  * `GymSchedule` aggregates multiple `FitnessClass` objects to manage the full timetable.

---

## 📁 Project Structure

```text
Fitness-Club-Management-System/
│
├── Person.py                 # Base class for people in the system
├── Member.py                 # Extends Person; handles wallet & attendance
├── Trainer.py                # Extends Person; handles specialties & hourly rates
├── Subscription.py           # Abstract Base Class (ABC) for subscriptions
├── MonthlySubscription.py    # Unlimited monthly access plan
├── PunchCardSubscription.py  # Fixed entries/punch-card plan
├── StudentSubscription.py    # Discounted rate plan inheriting MonthlySubscription
├── FitnessClass.py           # Class session model with capacity & member list
├── GymSchedule.py            # Timetable aggregator
├── main.py                   # Entry point running system simulation
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation