const data = [
  {
    "id": "ORD1001",
    "customer": "Alice Johnson",
    "items": [
      { "name": "Laptop", "price": 75000 },
      { "name": "Wireless Mouse", "price": 1500 }
    ],
    "status": "delivered"
  },
  {
    "id": "ORD1002",
    "customer": "Ravi Kumar",
    "items": [
      { "name": "Smartphone", "price": 30000 },
      { "name": "Phone Case", "price": 500 },
      { "name": "Screen Protector", "price": 300 }
    ],
    "status": "pending"
  },
  {
    "id": "ORD1003",
    "customer": "Sophia Lee",
    "items": [
      { "name": "Desk Chair", "price": 6500 }
    ],
    "status": "delivered"
  },
  {
    "id": "ORD1004",
    "customer": "Mohammed Ali",
    "items": [
      { "name": "LED TV", "price": 42000 },
      { "name": "Wall Mount", "price": 1200 }
    ],
    "status": "pending"
  },
  {
    "id": "ORD1005",
    "customer": "Emma Davis",
    "items": [
      { "name": "Blender", "price": 3500 },
      { "name": "Cookbook", "price": 700 }
    ],
    "status": "delivered"
  }
]

function main(){

    let customers = data.map((order) => order.customer)
    console.log("Customers: ", customers)

    let delivered_orderd = data.filter((order) => order.status === 'delivered')
    console.log("Delivered Orderd: ", delivered_orderd)

    let total_revenue = data.reduce((sum, order) => sum + order.items.price, 0)
    console.log("Total Revenue: ", total_revenue)

    data.forEach(Element => {
        console.log(Element)
    })

}

main()