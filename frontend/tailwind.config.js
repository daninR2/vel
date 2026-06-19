/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#000000',
        primary: '#FFFFFF',
        cardbg: '#111111',
      },
      letterSpacing: {
        editorial: '0.25em',
      },
    },
  },
  plugins: [],
}