<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/8.webp" alt="main_img" data-aos="zoom-out" data-aos-duration="600"
      style="filter:brightness(0.5)">
    <h1 data-aos="fade-down" data-aos-duration="1500">상품 추천 서비스</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">GPT-4o와 빅데이터를 이용한</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">금융 상품 추천 서비스를 제공합니다.</h4>
  </section>
  <div class="container-content d-flex flex-column align-items-center" style="max-width: 1400px;">
    <h1 class="fw-bold">🛒 &nbsp;&nbsp;금융 상품 추천 서비스</h1>
    <hr>

    <div class="ms-4 mt-5" style="min-width:1000px;">

      <div class="row" style="height: 60px; border:2px gray solid;">
        <div 
          class="col-6 d-flex justify-content-center" 
          :style="[ 
            { backgroundColor: isSelected === 'ai' ? '#0d6efd' : 'transparent' },
            { color: isSelected === 'ai' ? 'white' : 'black' } 
          ]" 
          @click="goBoard('ai')"
        >
          <div class="d-flex align-items-center justify-content-center">
            <p class="fs-3 fw-bold mb-0" style="text-decoration: none;">
              AI 상품 추천
            </p>
          </div>
        </div>

        <div 
          class="col-6 d-flex justify-content-center" 
          style="border-left: 2px gray solid;" 
          :style="[ 
            { backgroundColor: isSelected === 'cosine' ? '#0d6efd' : 'transparent' },
            { color: isSelected === 'cosine' ? 'white' : 'black' } 
          ]" 
          @click="goBoard('cosine')"
        >
          <div class="d-flex align-items-center justify-content-center">
            <p class="fs-3 fw-bold mb-0" style="text-decoration: none;">
              빅데이터 상품 추천
            </p>
          </div>
        </div>
      </div>
      <RouterView :key="$route.fullPath" class="mt-5"/>
    </div>
  </div>

</template>

<script setup>
import { useProductStore } from '@/stores/product'
import { ref, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const store = useProductStore()
const userStore = useUserStore()
const router = useRouter()
const isSelected = ref('ai')

const goBoard = (type) => {
  isSelected.value = type
  if (type === 'ai') {
    router.push({ name: 'ai', params: { 'username': userStore.username } })
  } else {
    router.push({ name: 'cosine' })
  }
}

</script>
