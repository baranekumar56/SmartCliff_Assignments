
function isValidPassword(password) {
  if (typeof password !== 'string') return false;
  const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$/;
  return pattern.test(password);
}

console.log(isValidPassword("Abc@1234"))
console.log(isValidPassword("abc123"))