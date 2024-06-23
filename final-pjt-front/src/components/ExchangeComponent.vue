<template>
    <div class="row mt-5 px-4 justify-content-center">
      <div class="converter row" style="max-width: 1300px; min-height:600px;">
        <div class="col-10">
          <div>
            <select v-model="MoneySelection" class="form-select fs-4 fw-bold" style="min-height: 50px; font-size: 20px; padding-left: 20px;">
              <option v-for="Option in ExchangeSelection" :key="Option" :value="Option">
                {{ Option }}
              </option>
            </select>
          </div>
          <div class="mt-3">
            <select v-model="CountrySelection" class="form-select fs-4 fw-bold" style="min-height: 50px; font-size: 20px; padding-left: 20px;">
              <option disabled hidden selected value="">
                국가를 선택해주세요.
              </option>
              <option v-for="country in CountryList" :key="country" :value="country">
                {{ country }}
              </option>
            </select>
          </div>
        </div>
        <div class="col-2 pt-3" style="position: relative;" v-if="CountrySelection">
          <img :src="flagSrc" alt="Country Flag" style="height:100%; width: 100%; align-items: center;">
        </div>
        <div class="mt-4 text-start row">
          <div class="input-group align-items-center position-relative">
            <span class="input-group-text fs-5 fw-bold text-center d-flex" id="basic-addon1" style="min-height: 80px; width: 100px; padding-left: 20px;">To</span>
            <input type="text" v-model.number="KRW" id="KRW" style="min-height: 80px; padding-right: 50px; padding-left: 20px;" @input="Paychanged((KRW / rate) * currencyUnit)" placeholder="KRW" class="form-control fs-4" aria-describedby="basic-addon1" />
            <span class="input-text-addon fw-bold fs-4">원</span>
          </div>
          <div class="input-group align-items-center">
            <span class="input-group-text fs-5 fw-bold text-center d-flex" id="basic-addon2" style="min-height: 80px; width:100px; padding-left: 20px;">From</span>
            <input type="text" v-model.number="payment" id="KRWCHG" style="min-height: 80px; padding-right: 50px; padding-left: 20px;" @input="KRWChanged((payment * rate) / currencyUnit)" placeholder="Money" class="form-control fs-4" aria-describedby="basic-addon2" />
            <span class="input-text-addon fw-bold fs-4">{{ currencyName }}</span>
          </div>
        </div>
        <div id="board-list" class="mt-5" v-if="CountrySelection">
          <div class="container">
            <table class="board-table">
              <thead>
                <tr class="border-bottom">
                  <th scope="col" class="th-num">환율</th>
                  <th scope="col" class="th-title"><span class="text-success"><u>{{changeratio}}{{ currencyName }} 당 {{ basePrice }} 원</u></span></th>
                </tr>
                <tr class="border-bottom">
                  <th scope="col" class="th-num">전일 대비</th>
                  <th scope="col" class="th-title">✔ &nbsp;&nbsp;{{ currencyName }} (은/는) 기준일 대비 <u>{{ changePrice }} 원</u> <span class="text-danger">{{ change }}</span></th>
                </tr>
                <tr>
                  <th scope="col" class="th-num">기준일</th>
                  <th scope="col" class="th-title">✔ &nbsp;&nbsp; {{ date }}</th>
                </tr>
              </thead>
            </table>
          </div>
        </div>
        <div id="board-list" class="mt-5" v-else>
          <div class="container">
            <table class="board-table">
              <thead>
                <tr class="border-bottom">
                  <th scope="col" class="th-num"></th>
                  <th scope="col" class="th-title"></th>
                </tr>
                <tr class="border-bottom">
                  <th scope="col" class="th-num"></th>
                  <th scope="col" class="th-title"></th>
                </tr>
                <tr>
                  <th scope="col" class="th-num"></th>
                  <th scope="col" class="th-title"></th>
                </tr>
              </thead>
            </table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import axios from 'axios'
  
  const CountryList = ref([
    "미국", "일본", "영국", "중국", "호주", "캐나다",
    "스위스", "뉴질랜드", "스웨덴", "싱가포르", "노르웨이", "멕시코",
    "러시아", "브라질", "남아공", "이스라엘",
    "사우디", "아랍에미리트", "말레이시아", "태국", "인도네시아", "필리핀",
    "폴란드", "헝가리", "체코", 
    "쿠웨이트", "카타르", "이집트", "파키스탄",
    "베트남"
  ])
  
  const CurrencyType = {
    미국: "USD", 일본: "JPY", 영국: "GBP", 중국: "CNY", 호주: "AUD",
    캐나다: "CAD", 스위스: "CHF", 뉴질랜드: "NZD", 스웨덴: "SEK", 싱가포르: "SGD",
    노르웨이: "NOK", 멕시코: "MXN", 인도: "INR", 러시아: "RUB", 브라질: "BRL",
    남아공: "ZAR", 터키: "TRY", 이스라엘: "ILS", 사우디: "SAR", 아랍에미리트: "AED",
    말레이시아: "MYR", 태국: "THB", 인도네시아: "IDR", 필리핀: "PHP", 폴란드: "PLN",
    헝가리: "HUF", 체코: "CZK", 칠레: "CLP", 콜롬비아: "COP",
    루마니아: "RON", 쿠웨이트: "KWD", 카타르: "QAR", 이집트: "EGP",
    파키스탄: "PKR", 베트남: "VND"
  }
  
  const ExchangeSelection = ref(["현찰 살 때", "현찰 팔 때"])
  const CountrySelection = ref("")
  const MoneySelection = ref("현찰 살 때")
  const changeratio = ref(1)
  const payment = ref(0)
  const KRW = ref(0)
  const rate = ref(null)
  const currencyUnit = ref(null)
  const currencyName = ref(null)
  const country = ref(null)
  const basePrice = ref(null)
  const change = ref(null)
  const changePrice = ref(null)
  const date = ref(null)
  const flagSrc = ref("")
  
  const flags = import.meta.glob('/src/assets/Flags/*.webp')
  
  watch([CountrySelection, MoneySelection], async ([CountryChanged, MoneySelectionChanged]) => {
    if (CountryChanged !== null && MoneySelectionChanged !== null) {
      try {
        const { data } = await axios.get(`https://corsproxy.io?https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW${CurrencyType[CountryChanged]}`)
  
        currencyUnit.value = data[0].currencyUnit  // 단위 기준치(ex) 엔:100)
        currencyName.value = data[0].currencyName  // 단위 이름
        country.value = data[0].country   // 나라
        basePrice.value = data[0].basePrice   // 기준 환율
        changePrice.value = data[0].changePrice // 변화값
        date.value = data[0].date // 날짜 
        if(currencyUnit.value == 100){
          changeratio.value = 100
        }
        else{
          changeratio.value = 1
        }
        if (data[0].change === "RISE") {
          change.value = "올랐습니다."
        }
        else {
          change.value = "내렸습니다."
        }
        if (MoneySelectionChanged == "현찰 살 때") {
          rate.value = data[0].cashBuyingPrice
        } else {
          rate.value = data[0].cashSellingPrice
        }
  
        // 이미지 경로 설정
        const flagKey = `/src/assets/Flags/${CurrencyType[CountryChanged]}.webp`
        if (flagKey in flags) {
          flagSrc.value = (await flags[flagKey]()).default
        }
  
        payment.value = 0
        KRW.value = 0
      } catch (err) {
        console.error(err)
      }
    }
  })
  
  const Paychanged = function (value) {
    payment.value = value
  }
  
  const KRWChanged = function (value) {
    KRW.value = value
  }
  </script>
  

<style scoped>
.converter {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
    text-align: center;
}

.converter select {
    padding: 10px;
    margin: 10px 0;
    font-size: 1.2em;
}

.converter button {
    background-color: #7ed321;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    cursor: pointer;
}

.converter .rate-info {
    margin: 10px 0;
    font-size: 1.2em;
}

.input-group {
    position: relative;
}

.input-text-addon {
    position: absolute;
    right: 40px;
    top: 50%;
    transform: translateY(-50%);
    font-weight: bold;
    font-size: 24px;
    pointer-events: none;
    /* This ensures that the text is not clickable and does not interfere with input */
}

.form-control {
    padding-right: 60px;
    /* Add some padding to the right to make space for the "원" text */
}

#refer p {
    margin-top: 0px;
    margin-bottom: 0px;
    font-size: 20px;
    font-weight: bold;
    text-underline-offset: 5px;
}

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

#board-search .search-window {
    padding: 15px 0;
    /* background-color: #f9f7f9; */
}

#board-search .search-window .search-wrap {
    position: relative;
    /*   padding-right: 124px; */
    margin: 0 auto;
    width: 80%;
    max-width: 700px;
    min-width: 500px;
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
</style>