/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{html,js,ts,jsx,tsx}",
        "./src/test_footer_standalone.html",
        "./src/test_navbar_standalone.html",
        "./design-system/**/*.md",
    ],
    theme: {
        extend: {
            colors: {
                axiara: {
                    obsidian: '#0D0D0D', // Primary Background
                    crimson: '#C41E3A',  // Accent Lines / Weave
                    white: '#FFFFFF',    // Primary Text
                    silver: '#A8A8A8',   // Secondary Text
                    charcoal: '#1A1A2E', // Glass Fallback
                    glass: 'rgba(26,26,46,0.4)',      // Frost Base
                    'glass-hover': 'rgba(26,26,46,0.8)', // Depth State
                    'crimson-glow': 'rgba(196,30,58,0.05)', // Button Hover
                }
            },
            fontFamily: {
                eng: ['Outfit', 'sans-serif'],        // Structure (Headings/Body)
                phil: ['Playfair Display', 'serif'],  // Philosophy (Italic Headlines)
                code: ['JetBrains Mono', 'monospace'], // Precision (Labels/Data)
            },
            borderRadius: {
                DEFAULT: '0px',
                sm: '0px',
                md: '0px',
                lg: '0px',
                xl: '0px',
                '2xl': '0px',
                '3xl': '0px',
                full: '0px', // Total denial of curvature
            },
            backgroundImage: {
                'axiara-gradient': 'linear-gradient(135deg, #0D0D0D 0%, #1A1A2E 100%)',
                'axiara-weave': 'repeating-linear-gradient(45deg, rgba(196,30,58,0.03) 0px, rgba(196,30,58,0.03) 1px, transparent 1px, transparent 10px)',
            },
            letterSpacing: {
                'axiara-wide': '0.05em',  // H1 spacing
                'axiara-label': '2px',    // Button/Label spacing
                'axiara-pretitle': '3px', // Tiny pre-title spacing
            },
            animation: {
                'fade-in-up': 'fadeInUp 0.8s ease-out forwards',
                'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
            },
            keyframes: {
                fadeInUp: {
                    '0%': { opacity: '0', transform: 'translateY(20px)' },
                    '100%': { opacity: '1', transform: 'translateY(0)' },
                }
            }
        }
    },
    plugins: [],
}
