<template>
  <div class="mt-4" style="margin-bottom: 100px;">
    <div id="board-list" class="mt-5" style="width: 100%;">
      <div class="container">

        <table class="board-table">
          <thead>
            <tr>
              <th scope="col" class="th-date">상품명</th>
              <th scope="col" class="th-date">금융회사명</th>
              <th scope="col" class="th-date">저축 기간</th>
              <th scope="col" class="th-date" @click="sortData('intr_rate')">
                저축 금리
                <span v-if="sortKey === 'intr_rate'">
                  {{ sortOrder === 'asc' ? '▲' : '▼' }}
                </span>
              </th>
              <th scope="col" class="th-date" @click="sortData('intr_rate2')">
                우대 금리
                <span v-if="sortKey === 'intr_rate2'">
                  {{ sortOrder === 'asc' ? '▲' : '▼' }}
                </span>
              </th>
            </tr>
          </thead>
          <tbody v-if="paginatedProducts.length">
            <tr v-for="product in paginatedProducts" :key="product.id" @click="goDetail(product.id)">
              <td class="text-center">{{ product.product.fin_prdt_nm }}</td>
              <td class="text-center">{{ product.product.kor_co_nm }}</td>
              <th class="text-center">{{ product.save_trm }}</th>
              <th class="text-center">{{ product.intr_rate }}</th>
              <td class="text-center">{{ product.intr_rate2 }}</td>
            </tr>
          </tbody>
        </table>

      </div>
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
        <button v-for="page in totalPages" :key="page" @click="currentPage = page"
          :class="{ active: currentPage === page }">
          {{ page }}
        </button>
        <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useProductStore } from '@/stores/product';
import { onMounted, computed, ref, watch } from 'vue';

const store = useProductStore()
const route = useRoute()
const router = useRouter()
const currentPage = ref(1);
const itemsPerPage = 10;
const sortKey = ref('intr_rate');
const sortOrder = ref('desc');

const goDetail = function (productId) {
  router.push({ name: 'productDetail', params: { type: route.params.type, productId: productId } });
}

const paginatedProducts = computed(() => {
  let products = store.filtered || [];
  if (sortKey.value) {
    products = products.slice().sort((a, b) => {
      let result = 0;
      if (a[sortKey.value] < b[sortKey.value]) {
        result = -1;
      } else if (a[sortKey.value] > b[sortKey.value]) {
        result = 1;
      }
      return sortOrder.value === 'asc' ? result : -result;
    });
  }
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return products.slice(start, end);
})

const totalPages = computed(() => {
  if (Array.isArray(store.filtered)) {
    return Math.ceil(store.filtered.length / itemsPerPage);
  }
  return 0;
});

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const fetchData = () => {
  if (route.params.type === 'deposit') {
    store.getDeposits(route.params.bank, route.params.trm)
  } else {
    store.getSavings(route.params.bank, route.params.trm)
  }
}

const sortData = (key) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc';
  } else {
    sortKey.value = key;
    sortOrder.value = 'asc';
  }
};

watch(() => route.params, () => {
  fetchData();
});

watch(() => store.filtered, () => {
  currentPage.value = 1;
});

onMounted(() => {
  fetchData();
});
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
  font-size: medium;
}

.board-table .th-title {
  text-align: center;
  font-size: medium;
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

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.pagination button {
  margin: 0 5px;
  padding: 5px 10px;
  border: none;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.pagination button.active {
  background-color: #0056b3;
}

.pagination button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

tr:hover {
  background-color: whitesmoke;
  font-weight: bold;
  
}
</style>
