class WaterfallModel:
    def __init__(self, requirements, design, implementation, testing, deployment, maintenance):
        self.requirements = requirements
        self.design = design
        self.implementation = implementation
        self.testing = testing
        self.deployment = deployment
        self.maintenance = maintenance

    def gather_requirements(self):
        print("Gathering requirements: {}".format(self.requirements))
        print()

    def create_design(self):
        print("Creating design: {}".format(self.design))
        print()

    def implement_system(self):
        print("Implementing system: {}".format(self.implementation))
        print()

    def perform_testing(self):
        print("Performing testing: {}".format(self.testing))
        print()

    def deploy_system(self):
        print("Deploying system: {}".format(self.deployment))
        print()

    def provide_maintenance(self):
        print("Providing maintenance: {}".format(self.maintenance))
        print()

def calculate_temperature(time, a, b, c):
    temperature = a * (time ** 2) + (b * time) + c
    return temperature

requirements = "Take coefficients for the formula"
design = "Define the function to calculate temperature based on time and coefficients"
implementation = "Run the formula using the coefficients and time provided"
testing = "No testing required in this context"
deployment = "Display the temperature output"
maintenance = "No maintenance required in this context"

waterfall_model = WaterfallModel(requirements, design, implementation, testing, deployment, maintenance)

waterfall_model.gather_requirements()

a = float(input("Enter coefficient a: ")) 
b = float(input("Enter coefficient b: ")) 
c = float(input("Enter coefficient c: ")) 
time = float(input("Enter time: "))

waterfall_model.create_design()

temp = calculate_temperature(time, a, b, c)

waterfall_model.implement_system()

waterfall_model.deploy_system()

print(f"Temperature at {time} is {temp} degrees Celsius.")


waterfall_model.provide_maintenance()