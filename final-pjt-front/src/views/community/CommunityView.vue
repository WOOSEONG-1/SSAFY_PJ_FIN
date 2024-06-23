<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/13.webp" alt="main_img" data-aos="zoom-out" data-aos-duration="600">>
    <h1 data-aos="fade-down" data-aos-duration="1500">커뮤니티</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">각종 상품에 대한 리뷰와 정보를</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">소통하며 정보를 공유해보세요 !</h4>
  </section>

  <div class="container-content" style="min-width: 1400px; min-height: 1200px;">
    <h1 class="fw-bold">🗨 &nbsp;&nbsp;커뮤니티</h1>
    <hr>
    <div class="row">
      <div class="col-3" style="position: relative;">
        <div class="d-flex flex-column flex-shrink-0 p-3 bg-dark" style="width: 100%; max-width: 280px;">
          <p class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
            <svg class="bi pe-none me-2" width="40" height="32">
            </svg>
            <span class="fs-4 text-center">게시판 목록</span>
          </p>
          <hr style="border:2px white solid;">
          <ul class="nav nav-pills flex-column mb-auto row gy-2">
            <li class="nav-item" v-for="board in store.boards">
              <RouterLink :to="{name:'community', params:{board:board.name}}" 
              class="nav-link text-light" @click="goBoard(board.name)">
                <svg class="bi pe-none me-2" width="16" height="16">
                  <use xlink:href="#home" />
                </svg>
                {{ board.name }}
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
      <RouterView :key="$route.fullPath" class="col-9"/>
    </div>
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { onMounted, ref } from 'vue';
import { useRouter, RouterView, RouterLink, onBeforeRouteUpdate } from 'vue-router';

const store = useCommunityStore()
const router = useRouter()

const goBoard = function (board) {
  router.push({name:'community', params:{board:board}})
}

onMounted( ()=> {
  store.getBoards()
})

</script>

<style scoped>
.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}

.b-example-divider {
  width: 100%;
  height: 3rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
}

.b-example-vr {
  flex-shrink: 0;
  width: 1.5rem;
  height: 100vh;
}

.bi {
  vertical-align: -.125em;
  fill: currentColor;
}

.nav-scroller {
  position: relative;
  z-index: 2;
  height: 2.75rem;
  overflow-y: hidden;
}

.nav-scroller .nav {
  display: flex;
  flex-wrap: nowrap;
  padding-bottom: 1rem;
  margin-top: -1px;
  overflow-x: auto;
  text-align: center;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}

.btn-bd-primary {
  --bd-violet-bg: #712cf9;
  --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

  --bs-btn-font-weight: 600;
  --bs-btn-color: var(--bs-white);
  --bs-btn-bg: var(--bd-violet-bg);
  --bs-btn-border-color: var(--bd-violet-bg);
  --bs-btn-hover-color: var(--bs-white);
  --bs-btn-hover-bg: #6528e0;
  --bs-btn-hover-border-color: #6528e0;
  --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
  --bs-btn-active-color: var(--bs-btn-hover-color);
  --bs-btn-active-bg: #5a23c8;
  --bs-btn-active-border-color: #5a23c8;
}

.bd-mode-toggle {
  z-index: 1500;
}

.bd-mode-toggle .dropdown-menu .active .bi {
  display: block !important;
}
</style>