<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/2.webp" alt="main_img"
    data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">프로필 보기</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">내 정보를 관리합니다.</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">내 상품들을 확인할 수 있습니다.</h4>
  </section>
  <div>
    <RouterView />
  </div>

</template>

<script setup>
    import { ref } from 'vue';
    import { useUserStore } from '@/stores/user';
    import { useRouter, RouterView } from 'vue-router';

    const store = useUserStore()
    const router = useRouter()


</script>

<style scoped>

</style>