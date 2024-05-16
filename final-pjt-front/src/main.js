import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersisted from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

const pinia = createPinia()
const app = createApp(App)
pinia.use(piniaPluginPersisted)
app.use(pinia)
app.use(router)

app.mount('#app')