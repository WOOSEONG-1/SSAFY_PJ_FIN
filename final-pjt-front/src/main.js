import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPersistedState from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import AOS from 'aos'
import 'aos/dist/aos.css'
import { useUserStore } from './stores/user'; 
import axios from 'axios'

const app = createApp(App)
const pinia = createPinia()
// Axios 인터셉터 설정
axios.interceptors.request.use(
  config => {
    if (config.url.endsWith('/logout/')) {
      return config;
    }
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers['Authorization'] = 'Bearer ' + token;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  response => {
    return response;
  },
  async error => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      await useUserStore().refreshTokenEvent();
      const newToken = localStorage.getItem('access_token');
      originalRequest.headers['Authorization'] = 'Bearer ' + newToken;
      return axios(originalRequest);
    }
    return Promise.reject(error);
  }
)

const kakaoMapApiKey = import.meta.env.VITE_MAP_API_KEY;
const script = document.createElement('script');
script.type = 'text/javascript';
script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoMapApiKey}&libraries=services`;
document.head.appendChild(script);

pinia.use(piniaPersistedState)
app.use(pinia)
app.use(router)
app.use(()=>AOS.init())
app.mount('#app')
