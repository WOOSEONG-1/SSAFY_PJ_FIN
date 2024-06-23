<template>
    <div class="row justify-content-center">
      <div v-if="!store.aiProducts" class="loading-container text-center" style="max-height: 500px;">
        <img src="/src/assets/loading.gif" alt="Loading..." class="loading-image" style="margin-top: 100px; margin-bottom: 100px;">
      </div>
    </div>
    <div id="board-list" class="mt-5" v-if="store.aiProducts">
        <h3 v-if="userStore.profile" class="fw-bold text-center">👍 &nbsp;&nbsp;<u class="text-success">{{userStore.profile.age}}세</u> 자산이 <u class="text-success">{{userStore.profile.money}}원</u>이고 연봉이 <u class="text-success">{{userStore.profile.salary}}만원</u>인 <u class="text-success">{{userStore.profile.nickname}}</u>님께 추천하는 상품입니다.</h3>
        <div class="container mt-5" v-if="store.aiProducts" style="min-width: 800px;">
            <h2 class="fw-bold">✔&nbsp; 예금 상품 추천</h2>
            <table class="board-table my-4" style="border-top: 2px black solid; border-bottom: 2px black solid;">
                <thead>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">상품명</th>
                        <th scope="col" class="th-title"><span class="text-primary"><u>{{ store.aiProducts['예금']['상품 이름'] }}</u></span></th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">옵션</th>
                        <th scope="col" class="th-title"><span>{{ store.aiProducts['예금']['옵션'] }}</span></th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">추천 이유</th>
                        <th scope="col" class="th-title" style="text-wrap:balance;">{{ store.aiProducts['예금']['추천 이유'] }}</th>
                    </tr>
                </thead>
            </table>
        </div>

        <div class="container" v-if="store.aiProducts" style="margin-top: 70px;">
            <h2 class="fw-bold">✔&nbsp; 적금 상품 추천</h2>
            <table class="board-table my-4" style="border-top: 2px black solid; border-bottom: 2px black solid;">
                <thead>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">상품명</th>
                        <th scope="col" class="th-title"><span class="text-primary"><u>{{ store.aiProducts['적금']['상품 이름'] }}</u></span></th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">옵션</th>
                        <th scope="col" class="th-title">{{ store.aiProducts['적금']['옵션'] }}</th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">추천 이유</th>
                        <th scope="col" class="th-title" style="text-wrap:balance;">{{ store.aiProducts['적금']['추천 이유'] }}</th>
                    </tr>
                </thead>
            </table>
        </div>
    </div>
</template>

<script setup>
import { onMounted, computed } from 'vue';
import { useProductStore } from '@/stores/product';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

const store = useProductStore()
const userStore = useUserStore()
const router = useRouter()

onMounted ( ()=> {
    store.aiRecommend()
    userStore.getProfile(userStore.username)
})
</script>

<style scoped>
table {
    border-collapse: collapse;
    border-spacing: 0;
}

.notice {
    padding: 20px 0;
}

.page-title {
    margin-bottom: 20px;
}

.page-title h3 {
    /* font-size: 28px; */
    font-size: 30px;
    color: #333333;
    font-weight: bold;
    text-align: start;
}

.board-table {
    font-size: 15px;
    width: 100%;
    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
}

/* 게시글 제목 */
.board-table a {
    color: #333;
    display: inline-block;
    line-height: 1.4;
    word-break: break-all;
    vertical-align: middle;
    text-decoration: none;
    font-size: 15px;
}

.board-table a:hover {
    text-decoration: underline;
}

.board-table th {
    text-align: center;
    font-size: 15px;
}

.board-table .th-num {
    width: 100px;
    text-align: center;
    font-size: 18px;
    text-wrap:balance
}

.board-table .th-title {
    text-align: center;
    font-size: 18px;
    text-wrap:balance
}

.board-table .th-date {
    width: 200px;
    font-size: medium;
}

.board-table th,
.board-table td {
    padding: 14px 0;
}

.board-table tbody td {
    border-top: 1px solid #e7e7e7;
    text-align: center;
}

.board-table tbody th {
    padding-left: 28px;
    padding-right: 14px;
    border-top: 1px solid #e7e7e7;
    text-align: left;
}

.board-table tbody th p {
    display: none;
}
</style>