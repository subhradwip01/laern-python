class RailwayForm:
    formType="Railway Form"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

subhrasApplication = RailwayForm()
subhrasApplication.name="Subhradwip Kulavi"
subhrasApplication.train="Rajdhani Expresss"
subhrasApplication.printData()