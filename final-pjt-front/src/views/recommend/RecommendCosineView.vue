<template>
  <div class="row justify-content-center">
    <h3 v-if="userStore.profile" class="fw-bold text-center">👍 &nbsp;&nbsp;<u class="text-success">{{ userStore.profile.age }}세</u>
      자산이 <u class="text-success ">{{ userStore.profile.money }}원</u>이고 연봉이 <u
        class="text-success">{{ userStore.profile.salary }}만원</u>인 <u
        class="text-success">{{ userStore.profile.username }}</u>님께 추천하는 상품입니다.</h3>
    <div v-if="!store.cosProducts" class="loading-container text-center" style="max-height: 500px;">
      <img src="/src/assets/loading.gif" alt="Loading..." class="loading-image"
        style="margin-top: 100px; margin-bottom: 100px;">
    </div>
    <div v-else-if="store.cosProducts" class="row justify-content-center">
      <h3 class="fw-bold mt-4 text-center " >
        <u class="text-success">{{ userStore.profile.nickname }}</u>님과 비슷한 조건을 가진 
          <span class="text-danger"><u>{{ store.cosProducts[1] }}명</u></span>
          과 비교하여 상품을 추천하였습니다.</h3>
      <div class="row justify-content-center row-cols-2" id="content-box" style="max-width: 1200px;">
        <article class="row gy-4" style="padding-top: 0px; min-height:100px;"
          v-for="(product, index) in store.cosProducts[0]" :key="product[0]">
          <div class="row justify-content-center" style="box-sizing: border-box;">

            <div class="card text-center pt-4 pb-0" style="border: black 2px solid;">

              <h2 class="my-3 fw-bold d-flex justify-content-center align-items-center" style="min-height: 80px;"
                v-if="index === 0">
                👍 &nbsp; {{ product[0] }}
              </h2>

              <h2 class="my-3 fw-bold d-flex justify-content-center align-items-center" style="min-height: 80px;"
                v-else>
                &nbsp; {{ product[0] }}
              </h2>

              <hr>
              <div class="my-3">
                <h2>✔&nbsp;&nbsp;추천도</h2>
                <h2 class="my-4 ps-4" style="color:crimson">
                  {{ product[1] }}
                </h2>
              </div>
            </div>

          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
import { useUserStore } from '@/stores/user';
import { onMounted, ref } from 'vue';
const store = useProductStore()
const isLoading = ref(true);
const userStore = useUserStore()

onMounted(async () => {
  store.cosineRecommend();
  isLoading.value = false;
  userStore.getProfile(userStore.username)
});
</script>

<style scoped>
* {
  text-wrap: balance;
}

#content-box {
  min-height: 800px;
  margin-bottom: 150px;
}

.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 800px;
  width: 100%;
}

.loading-image {
  max-width: 300px;
  max-height: 300px;
}

.article-spacing {
  margin-bottom: 40px;
}

.article-border-spacing {
  margin: 20px;
}
</style>