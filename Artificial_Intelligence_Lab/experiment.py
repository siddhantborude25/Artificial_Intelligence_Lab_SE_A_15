from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='architecture'), StudentFacts(likes='design'))
    def civil(self):
        print("Suggested Career Path: Civil Engineering")
    @Rule(StudentFacts(likes='AI'), StudentFacts(likes='DS'))
    def AIDS(self):
        print("Suggested Career Path: AIDS Engineering")
    
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("\nSelect a subject you are intrsted in\n")
    print("1.maths\n2.physics\n3.biology\n4.graphics\n5.architecture\n6.mechanics\n7.chemistry\n8.programming\n9.biology\n10.design.\nMachine_learning\nAI\nDS")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming):\n").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()

