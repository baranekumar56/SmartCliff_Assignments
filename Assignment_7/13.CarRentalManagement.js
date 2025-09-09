const {consoleRW} = require('./consoleRW')
const crw = new consoleRW()

class Car{
    constructor(brand, model, rentalPricePDay, availability){
        this.brand = brand
        this.rentalPricePDay = rentalPricePDay
        this.availability = availability
        this.model = model
    }

    rentCar(days) {
        if (this.availability) {
            this.availability = false;
            return {...this, cost: this.rentalPricePDay * days}
        }else return "Cannot Book car";
    }

    returnCar(){
        this.availability = true;
    }

    getInfo(){
        return `Brand: ${this.brand}, Model: ${this.model}, Rental Price Per Day: ${this.rentalPricePDay}, Availability: ${this.availability}`;
    }
}

async function proc() {
    const car1 = new Car("Toyota", "A1", 100, true)
    const car2 = new Car("Honda", "B", 200, false)

    console.log(car1.getInfo())
    console.log(car2.getInfo())

    console.log(car1.rentCar(10))
    console.log(car2.rentCar(10))

    car1.returnCar()
    car2.rentCar()
}

async function main(){
    await proc()
    crw.close()
}

main()