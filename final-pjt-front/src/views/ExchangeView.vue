<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/16.webp" alt="main_img"
    data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">환율 계산기</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">당일의 환율 정보를 통해</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">환율 계산 서비스를 제공합니다 !</h4>
  </section>
  <div class="container-content">
    <h1 class="fw-bold"> &nbsp;&nbsp;💲 &nbsp;환율 계산</h1>
    <hr>
    <ExchangeComponent />
  </div>
  
</template>

<script setup>
import ExchangeComponent from '@/components/ExchangeComponent.vue'

</script>

<style scoped>

</style>
<!-- [
    {
        "code": "FRX.KRWUSD",
        "currencyCode": "USD",
        "currencyName": "달러",
        "country": "미국",
        "name": "미국 (USD/KRW)",
        "date": "2024-05-17",
        "time": "23:58:04",
        "recurrenceCount": 378,
        "basePrice": 1355.5,
        "openingPrice": 1349.4,
        "highPrice": 1359.5,
        "lowPrice": 1348,
        "change": "RISE",
        "changePrice": 4.5,
        "cashBuyingPrice": 1379.22,
        "cashSellingPrice": 1331.78,
        "ttBuyingPrice": 1342.3,
        "ttSellingPrice": 1368.7,
        "tcBuyingPrice": null,
        "fcSellingPrice": null,
        "exchangeCommission": 7.1701,
        "usDollarRate": 1,
        "high52wPrice": 1399.9,
        "high52wDate": "2024-04-16",
        "low52wPrice": 1257.5,
        "low52wDate": "2023-07-18",
        "currencyUnit": 1,
        "provider": "하나은행",
        "timestamp": 1715978617755,
        "id": 79,
        "createdAt": "2016-10-21T06:13:34.000+00:00",
        "modifiedAt": "2024-05-17T20:43:38.000+00:00",
        "signedChangePrice": 4.5,
        "signedChangeRate": 0.003330866,
        "changeRate": 0.003330866
    }
] -->