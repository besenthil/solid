from solid.lsp import Vehicle, Car,VehicleController,Bike

if __name__ == "__main__":
    v = VehicleController(Bike())
    v.start()
    v.stop()
    v.drive()