# Class representing each student
class Student:
    def _init_(self, student_id, name, preferred_room_type, preferred_proximity):
        self.student_id = student_id
        self.name = name
        self.preferred_room_type = preferred_room_type
        self.preferred_proximity = preferred_proximity

# Class representing each hostel room
class HostelRoom:
    def _init_(self, room_number, room_type, proximity_to_academic_building, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.proximity_to_academic_building = proximity_to_academic_building
        self.is_available = is_available

# Hostel system to manage allocation
class HostelSystem:
    def _init_(self):
        self.students = []
        self.rooms = []
    
    # Add student to the system
    def add_student(self, student):
        self.students.append(student)
    
    # Add room to the system
    def add_room(self, room):
        self.rooms.append(room)
    
    # Function to allocate rooms to students
    def allocate_rooms(self):
        for student in self.students:
            # Sort rooms based on proximity and availability
            available_rooms = sorted(
                [room for room in self.rooms if room.is_available and room.room_type == student.preferred_room_type],
                key=lambda x: x.proximity_to_academic_building
            )
            
            if available_rooms:
                # Allocate the closest available room
                allocated_room = available_rooms[0]
                allocated_room.is_available = False
                print(f"Allocated Room {allocated_room.room_number} to Student {student.name}")
            else:
                print(f"No available room for Student {student.name} with preference {student.preferred_room_type}")
                
# Sample data and system initialization
def main():
    hostel_system = HostelSystem()
    
    # Add some rooms
    hostel_system.add_room(HostelRoom("101", "Single", 5))
    hostel_system.add_room(HostelRoom("102", "Double", 3))
    hostel_system.add_room(HostelRoom("103", "Single", 7))
    hostel_system.add_room(HostelRoom("104", "Double", 2))
    
    # Add some students
    hostel_system.add_student(Student(1, "Alice", "Single", 5))
    hostel_system.add_student(Student(2, "Bob", "Double", 2))
    hostel_system.add_student(Student(3, "Charlie", "Single", 6))
    
    # Allocate rooms
    hostel_system.allocate_rooms()

# Run the program
if _name_ == "_main_":
    main()