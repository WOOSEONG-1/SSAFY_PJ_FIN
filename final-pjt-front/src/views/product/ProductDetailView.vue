<template>
    <div id="board-list" class="mt-5" v-if="store.product">
        <div class="container">
            <table class="board-table" style="border-top: 2px black solid; border-bottom: 2px black solid;">
                <thead>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">상품명</th>
                        <th scope="col" class="th-title"><span class="text-success"><u>{{ store.product[0].product.fin_prdt_nm }}</u></span></th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">은행명</th>
                        <th scope="col" class="th-title"><span class="text-success"><u>{{ store.product[0].product.kor_co_nm }}</u></span></th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">유의사항</th>
                        <th scope="col" class="th-title" style="text-wrap:balance;">{{ store.product[0].product.etc_note }}</th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">가입 방법</th>
                        <th scope="col" class="th-title">{{ store.product[0].product.join_way }}</th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">만기 후 이자율</th>
                        <th scope="col" class="th-title"  style="text-wrap:balance;"> {{ store.product[0].product.mtrt_int }}</th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">저축 기간</th>
                        <th scope="col" class="th-title"> {{ store.product[0].save_trm }}개월</th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">저축 금리</th>
                        <th scope="col" class="th-title text-danger" style="text-decoration: underline;">
                            {{ store.product[0].intr_rate }}
                        </th>
                    </tr>
                    <tr class="border-bottom">
                        <th scope="col" class="th-num">우대 금리</th>
                        <th scope="col" class="th-title text-danger" style="text-decoration: underline;">
                            {{ store.product[0].intr_rate2 }}
                        </th>
                    </tr>
                </thead>
            </table>
        </div>
        <div class="text-center mt-4">
            <button class="btn btn-success fs-5" v-if="!isMyProduct" @click="toggleMyProduct">내 상품 추가</button>
            <button class="btn btn-danger fs-5" v-if="isMyProduct" @click="toggleMyProduct">내 상품 제거</button>
            <button class="btn btn-secondary fs-5 ms-5" @click="goBack">목록으로</button>
        </div>
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
import { useUserStore } from '@/stores/user';
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const store = useProductStore()
const userStore = useUserStore()
const route = useRoute()
const router = useRouter()
const goBack = ()=> router.back()
const toggleMyProduct = function () {
    if ( route.params.type == 'deposit' ) {
        store.toggleMyDeposit(store.product[0].fin_prdt_cd)
    }
    else {
        store.toggleMySavings(store.product[0].fin_prdt_cd)
    }
}


const isMyProduct = computed( ()=> {
    if ( route.params.type == 'deposit' ) {

        if (userStore.deposit.deposit_list==null){
            return false
        }
        for (const deposit of userStore.deposit.deposit_list) {
            if (deposit.fin_prdt_cd == store.product[0].product.fin_prdt_cd){
                return true
            }
        }
        return false
    }
    else {
        if (userStore.saving.saving_list==null){
            return false
        }
        for (const saving of userStore.saving.saving_list) {
            if (saving.fin_prdt_cd == store.product[0].product.fin_prdt_cd){
                return true
            }
        }
        return false
    }
})

onMounted ( ()=> {
    if( route.params.type == 'deposit'){
        store.getDepositsDetail(route.params.productId)        
    }
    else {
        store.getSavingsDetail(route.params.productId)
        // userStore.savingchart(userStore.username)
    }
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