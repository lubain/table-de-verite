import type { Config } from "tailwindcss";
import { ACCENT, BLACK, DESTRUCTIVE, MUTED, PRIMARY, SECONDARY, ORANGE } from "./src/shared/constants/Color";
import tailwindcssAnimate from "tailwindcss-animate";

export default {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        black: {
          DEFAULT: BLACK,
          foreground: "#FFFFFF",
        },
        orange: {
          DEFAULT: ORANGE,
          foreground: "#FFFFFF",
        },
        primary: {
          DEFAULT: PRIMARY,
          foreground: "#FFFFFF",
        },
        secondary: {
          DEFAULT: SECONDARY,
          foreground: "#1A202C",
        },
        destructive: {
          DEFAULT: DESTRUCTIVE,
          foreground: "#FFFFFF",
        },
        muted: {
          DEFAULT: MUTED,
          foreground: "#64748B",
        },
        accent: {
          DEFAULT: ACCENT,
          foreground: "#1A202C",
        },
      },
      keyframes: {
        "fade-in": {
          "0%": { opacity: "0", transform: "translateY(10px)" },
          "100%": { opacity: "1", transform: "translateY(0)" }
        },
        "slide-in": {
          "0%": { transform: "translateX(-100%)" },
          "100%": { transform: "translateX(0)" }
        }
      },
      animation: {
        "fade-in": "fade-in 0.5s ease-out",
        "slide-in": "slide-in 0.5s ease-out"
      }
    },
  },
  plugins: [tailwindcssAnimate],
} satisfies Config;