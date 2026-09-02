import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import path from "path"

export default defineConfig({
    plugins: [react()],
    base: "/static/react/",

    build: {
        outDir: path.resolve(__dirname, "../static/react"),
        emptyOutDir: true,

        rollupOptions: {
            input: path.resolve(__dirname, "src/main.jsx"),

            output: {
                entryFileNames: "main.js",
                chunkFileNames: "assets/[name]-[hash].js",
                assetFileNames: (assetInfo) => {
                    if (assetInfo.name?.endsWith(".css")) {
                        return "main.css"
                    }

                    return "assets/[name]-[hash][extname]"
                },
            },
        },
    },

    server: {
        origin: "http://localhost:5173",
    },
})