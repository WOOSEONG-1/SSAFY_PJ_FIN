import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useUserStore } from './user'
import {useRouter} from 'vue-router'
export const useProductStore = defineStore('product', () => {
  const API_URL = 'http://localhost:8000/api/v1/backend/products'
  const REC_API_URL = 'http://localhost:8000/api/v1/backend/recommend'
  const products = ref(null)
  const filtered = ref(null)
  const store = useUserStore()
  const product = ref(null)
  const cosProducts = ref(null)
  const aiProducts = ref(null)
  const router =useRouter()
  const subscribe= ref(null)
  store.depositchart(store.username)
  store.savingchart(store.username)
  // API 은행 목록( 테스트용 )
  const banks = [
    "국민은행",
    "한국산업은행",
    "신한은행",
    "농협은행주식회사",
    "대구은행",
    "부산은행",
    "제주은행",
    "수협은행",
    "광주은행",
    "주식회사 케이뱅크",
    "토스뱅크 주식회사",
    "우리은행",
    "한국스탠다드차타드은행",
    "전북은행",
    "경남은행",
    "중소기업은행",
    "하나은행",
    "주식회사 카카오뱅크",
  ]

  // 예금 데이터 필터링 ( bank : 은행명, trm : 저축기간 )
  const getDeposits = function (bank, trm) {
    axios({
      method: 'get',
      url: `${API_URL}/deposit_options/`,
    })
      .then((res) => {
        products.value = res.data
      })
      .then(() => {
        if (bank !== 'all') {
          filtered.value = products.value.filter((e) => {
            return e.product.kor_co_nm === bank;
          })
        }
        else {
          filtered.value = products.value
        }
      })
      .then(() => {
        if (trm !== '1000') {
          filtered.value = filtered.value.filter((e) => {
            return e.save_trm === Number(trm)
          })
        }
      })
      .catch(err => console.error(err))
  }

  // 예금 데이터 상세 조회
  const getDepositsDetail = function (pid) {
    axios({
      method: 'get',
      url: `${API_URL}/deposit_options/${pid}`,
    })
      .then((res) => {
        product.value = res.data
      })
      .then( ()=> {
        store.depositchart(store.username)
      })
      .catch(err => console.error(err))
  }
  // 적금 데이터 상세 조회
  const getSavingsDetail = function (pid) {
    axios({
      method: 'get',
      url: `${API_URL}/savings_options/${pid}`,
    })
      .then((res) => {
        product.value = res.data
      })
      .then( ()=> {
        store.savingchart(store.username)
      })
      .catch(err => console.error(err))
  }

  // 적금 데이터 필터링 ( bank : 은행명, trm : 저축기간 )
  const getSavings = function (bank, trm) {
    axios({
      method: 'get',
      url: `${API_URL}/savings_options/`,
    })
      .then((res) => {
        products.value = res.data
      })
      .then(() => {
        if (bank !== 'all') {
          filtered.value = products.value.filter((e) => {
            return e.product.kor_co_nm === bank;
          })
        }
        else {
          filtered.value = products.value
        }
      })
      .then(() => {
        if (trm !== '1000') {
          filtered.value = filtered.value.filter((e) => {
            return e.save_trm === Number(trm)
          })
        }
      })
      .catch(err => console.error(err))
  }

  const toggleMyDeposit = function(pid) {
    axios({
      method: 'post',
      url: `${store.API_URL}/${store.username}/subdeposits/${pid}/`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      },
    })
      .then((res) => {
        router.push({name:'product',params:{'type':'deposit', 'bank':'all', 'trm':'1000'}})
      })
  }

  const toggleMySavings = function(pid) {
    axios({
      method: 'post',
      url: `${store.API_URL}/${store.username}/subsavings/${pid}/`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      },
    })
      .then((res) => {
      router.push({name:'product',params:{'type':'saving', 'bank':'all', 'trm':'1000'}})
      })
  }


  const aiRecommend = function () {
    axios({
      method: 'get',
      url: `${REC_API_URL}/ai_product/`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      },
    })
      .then((res) => {
        aiProducts.value = res.data
      })
      .catch(err => console.error(err))
  }

  const cosineRecommend = function () {
    axios({
      method: 'get',
      url: `${REC_API_URL}/similar_user`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      },
    })
      .then((res) => {
        cosProducts.value = res.data
      })
      .catch(err => console.error(err))
  }

  return {
    products, filtered, banks, product, cosProducts, aiProducts,
    getDeposits, getSavings, toggleMyDeposit, 
    toggleMySavings, getDepositsDetail, getSavingsDetail,
    cosineRecommend, aiRecommend
  }
})
