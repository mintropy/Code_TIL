interface Square {
  width: number;
  height: number;
}

const square: Square = {
  width: 10,
  height: 10,
}

console.log(square);
console.log("--------------------")

class Rectangle implements Square {
  width: number;
  height: number;
  constructor(width: number, height: number) {
    this.width = width;
    this.height = height;
  }

  getArea(): number {
    return this.width * this.height;
  }
}

const rectangle = new Rectangle(10, 20);

console.log(rectangle);
console.log(rectangle.getArea());
console.log("--------------------")

interface position {
  x: number;
  y: number;
}

class Rectangle2D implements Square {
  width: number;
  height: number;
  position: position;
  constructor(position: position, width: number, height: number) {
    this.width = width;
    this.height = height;
    this.position = {x: position.x, y: position.y};
  }

  getArea(): number {
    return this.width * this.height;
  }
}

const position = {x: 10, y: 20};
const rectangle2D = new Rectangle2D(position, 30, 40);

console.log(rectangle2D);
console.log(rectangle2D.getArea());
console.log("--------------------")
