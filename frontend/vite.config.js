import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0',
    port: 12001,
    cors: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    proxy: {
      '/api': {
        target: 'http://localhost:12000',
        changeOrigin: true,
        secure: false,
      }
    },
    allowedHosts: [
      'work-1-dnefeptwsfosubzj.prod-runtime.all-hands.dev',
      'work-2-dnefeptwsfosubzj.prod-runtime.all-hands.dev',
      'localhost'
    ]
  },
})
