/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html"],
  theme: {
    extend: {
      screens:{
        xs: "450px"
      },
      colors:{
        yellow:{
          500:"FED000",
          700:"F9C70C",
          300:"FFE338"
        }
      }
    },
  },
  plugins: [],
}

