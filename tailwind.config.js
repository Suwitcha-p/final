/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        dark: {
          bg: "#0B1120",
          sidebar: "#111827",
          card: "#151F32",
          cardHover: "#1E293B",
          border: "rgba(255, 255, 255, 0.08)",
          borderHighlight: "rgba(59, 130, 246, 0.3)"
        },
        brand: {
          primary: "#3B82F6",
          secondary: "#06B6D4",
          success: "#10B981",
          warning: "#F59E0B",
          danger: "#EF4444",
          indigo: "#6366F1",
          purple: "#A855F7"
        }
      },
      fontFamily: {
        sans: ['Inter', 'Sarabun', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace']
      }
    },
  },
  plugins: [],
}
