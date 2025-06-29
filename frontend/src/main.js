import { createApp } from 'vue'
import { MotionPlugin } from '@vueuse/motion'
import App from './App.vue'
import router from './router'
import pinia from './store'
import './assets/styles/main.scss'

const app = createApp(App)

// Use plugins
app.use(router)
app.use(pinia)
app.use(MotionPlugin)

// Mount app
app.mount('#app')
