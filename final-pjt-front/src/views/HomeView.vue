<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/10.webp" alt="main_img" 
      data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">돈</span>
      <span class="me-2 brand-sub-name">나무</span>
      와 함께라면
    </h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">금융 서비스를 더욱 간편하게 ! </h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">한 번에, 손 쉽게 !</h4>
  </section>
  <div class="container-content">
    <ArticleComponent/>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ArticleComponent from '@/components/ArticleComponent.vue';  

</script>

<style scoped>
  .brand-name {
    background: linear-gradient(45deg, #FFD700, #FFFFFF 25%, #FFD700);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 100px;
    font-weight: bold;
    text-shadow: 0 0 0 rgba(255, 215, 0, 0.7), 0 0 5px rgba(255, 215, 0, 0.5), 0 0 5px rgba(255, 215, 0, 0.3);
  }

  .brand-sub-name {
    background: linear-gradient(45deg, #FFD700, #FFFFFF 25%, #FFD700);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 80px;
    text-shadow: 0 0 0 rgba(255, 215, 0, 0.7), 0 0 5px rgba(255, 215, 0, 0.5), 0 0 0px rgba(255, 215, 0, 0.3);  }
</style>
