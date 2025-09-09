

function extractNumbers(text) {
  if (typeof text !== "string") return [];

  const matches = text.match(/\d+(\.\d+)?/g);

  return matches ? matches.map(Number) : [];
}

console.log(extractNumbers("The price is 45.50 and discount is 5")); 

console.log(extractNumbers("Room 101 costs 1200.75")); 

console.log(extractNumbers("ekjhgkjerghlekjgh")); 
