<template>
  <div class="container-fluid">
    <header :class="['navbar-custom', { 'navbar-scrolled': isScrolled }]" style="width:100%">
      <nav class="navbar px-5 d-flex justify-content-between flex-nowrap" style="min-width: 1200px; max-width:1500px;"
        data-aos="fade-up" data-aos-duration="1500">
        <RouterLink :to="{ name: 'home' }" class="nav-brand pe-4">
          <img src="@/assets/tr_logo.png" alt="logo" style="width: 70px; height: 70px;">
        </RouterLink>
        <div class="container-custom d-flex flex-nowrap">
          <ul class="navbar-nav d-flex flex-row flex-nowrap">
            <li class="nav-item">
              <RouterLink :to="{ name: 'product', 
                params:{'type':'deposit', 'bank':'all', 'trm':'1000'} }" 
                class="nav-link" :style="{ 'color': isScrolledColor }">
                  예금/적금 비교
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'exchange' }" class="nav-link" :style="{ 'color': isScrolledColor }">환율 계산기
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'bank' }" class="nav-link" :style="{ 'color': isScrolledColor }">주변 은행 찾기
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'community', params: { board: '자유' } }" class="nav-link"
                :style="{ 'color': isScrolledColor }">커뮤니티</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ai' }" class="nav-link" :style="{ 'color': isScrolledColor }">상품 추천
              </RouterLink>
            </li>
            <li class="nav-item d-flex align-items-center" v-if="!store.isLogin">
              <div class="btn btn-success">
                <RouterLink :to="{ name: 'login' }" style="text-decoration: none; color: white; font-weight: bold;">
                  Sign In
                </RouterLink>
              </div>
            </li>
            <li class="dropdown nav-item d-flex align-items-center justify" v-else>
              <a href="#" class="align-items-center text-decoration-none dropdown-toggle d-flex"
                data-bs-toggle="dropdown" aria-expanded="false">
                <strong class="nav-link me-3" :style="{ 'color': isScrolledColor }">마이 페이지</strong>
              </a>
              <ul class="dropdown-menu text-small shadow" style="position: absolute;">
                <li>
                  <RouterLink class="dropdown-item fw-bold" 
                    :to="{name:'profile', params:{username:store.username}}">
                    Profile
                  </RouterLink>
                </li>
                <li>
                  <hr class="dropdown-divider">
                </li>
                <li><a class="dropdown-item fw-bold" href="#" @click="store.logoutEvent">Sign out</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>

    <footer class="row">
      <h3 class="fs-5 fw-bold">SSAFY Final Project - Financial</h3>
      <p class="mb-0">Hwang-Wooseong, Jeon-Gicheol - Service &nbsp;&nbsp;🏁</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted, onUnmounted, ref } from 'vue'
import { useUserStore } from '@/stores/user';

const isScrolled = ref(false)
const isScrolledColor = ref('')
const store = useUserStore()

const handleScroll = () => {
  if (window.scrollY > 0) {
    isScrolled.value = true
    isScrolledColor.value = 'black'
  } else {
    isScrolled.value = false
    isScrolledColor.value = 'white'
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

</script>

<style scoped>
* {
  white-space: nowrap;
  overflow: visible;
}

.container-custom {
  display: flex;
  align-items: center;
  justify-content: end;
}

.navbar-custom {
  width: 100%;
  position: fixed;
  top: 0;
  z-index: 1000;
  padding-top: 20px;
  border-bottom: 1px solid #818a92;
  font-weight: bold;
}

.navbar-scrolled {
  background-color: white;
}

.navbar-custom .navbar-brand img {
  width: 50px;
  height: 50px;
}

.navbar-custom .navbar-nav {
  display: flex;
  flex-direction: row;
}

.navbar-custom .navbar-nav .nav-link {
  color: #ffffff;
  margin-right: 50px;
  font-size: 27px;
}

.navbar-custom .navbar-nav .nav-link:hover {
  text-decoration: underline;
  text-underline-offset: 10px;
}

.nav-link-scrolled {
  color: black;
  margin-right: 50px;
  font-size: 27px;
}

footer {
  margin-top: 30px;
  margin-bottom: 0px;
  padding-top: 20px;
  background-color: whitesmoke;
  height: 100px;
  width: 100%;
  border-top: 2px solid whitesmoke;
  text-align: center;
  display: flex;
  align-content: start;
}
</style>
