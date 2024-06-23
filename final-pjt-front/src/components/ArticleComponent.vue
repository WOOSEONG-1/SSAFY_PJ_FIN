<template>
    <div class="row justify-content-center">

        <!-- left -->
        <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false" style="padding-top: 0px;">
            <div class="row justify-content-between">
                <div class="col-7">
                    <h1 class="my-3 fw-bold">예금 / 적금 조회 및</h1>
                    <h1 class="my-3 fw-bold">비교 서비스</h1>
                    <br>
                    <div class="my-3">
                        <h4>
                            한국 금융 거래소 API를 통해 조회한 데이터를
                        </h4>
                        <h4>
                            이용하여 원하는 상품을 손쉽게 비교할 수
                        </h4>
                        <h4>
                            있도록 서비스를 제공합니다.
                        </h4>
                    </div>
                </div>
                <div class="col-5" style="margin: auto 0;">
                    <img src="../assets/6.webp" alt="home_img" style="width:100%;">
                </div>
            </div>
        </article>
        
        <!-- up -->
        <!-- <article class="container-up" data-aos="fade-up" data-aos-duration="700" data-aos-once="false">
            <div class="row gy-3">
                <h1 class="fw-bold pb-3">국가 간 환율 계산 서비스</h1>
                <img src="@/assets/5.webp" alt="home_img" style="width:100%">
                <div>
                    <h2 class="my-3 fw-bold"><u>원화뿐만 아닌 타 국가 화폐간 환율 계산 지원</u></h2>
                    <div class="mt-3 mt-4 mb-0 pb-0 ps-3">
                        
                        <h4>
                            다양한 국가의 원화 기준 환율을 계산하여 <br>
                        </h4>
                        <h4>
                            국가간 환율 계산 서비스를 제공합니다.
                        </h4>
                    </div>
                </div>
            </div>
        </article> -->

        
        <!-- left -->
        <article class="container justify-content-start"
        data-aos="fade-left" data-aos-duration="700" data-aos-once="false"
        >
        <div class="row justify-content-between">
            <div class="col-5" style="margin: auto 0;">
                <img src="../assets/bank.webp" alt="home_img" style="width:100%;">
            </div>
            <div class="col-6">
                <h1 class="my-3 fw-bold">주변 은행 찾기 서비스</h1>
                <br>
                <div class="my-3">
                        <h4>
                            카카오 맵 API를 통해 조회한 데이터를
                        </h4>
                        <h4>
                            이용하여 주변 지역의 은행 위치를
                        </h4>
                        <h4>
                            확인하는 서비스를 제공합니다.
                        </h4>
                    </div>
                </div>
            </div>
        </article>
        
        <!-- left -->
        <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false" style="padding-top: 0px;">
            <div class="row justify-content-between">
                <div class="col-7">
                    <h1 class="my-3 fw-bold">국가 간 환율 계산 서비스</h1>
                    <br>
                    <div class="my-3">
                        <h3>
                            <u>원화뿐만 아닌 타 국가 화폐간 환율 계산 지원</u>
                        </h3>
                        <h4 class="mt-4">
                            다양한 국가의 원화 기준 환율을 계산하여
                        </h4>
                        <h4>
                            국가간 환율 계산 서비스를 제공합니다.
                        </h4>
                    </div>
                </div>
                <div class="col-5" style="margin: auto 0;">
                    <img src="../assets/5.webp" alt="home_img" style="width:100%;">
                </div>
            </div>
        </article>
        
        <!-- right -->
        <article class="container justify-content-start"
        data-aos="fade-right" data-aos-duration="700" data-aos-once="false"
        >
        <div class="row justify-content-between">
            <div class="col-5" style="margin: auto 0;">
                    <img src="../assets/8.webp" alt="home_img" style="width:100%;">
                </div>
                <div class="col-6">
                    <h1 class="my-3 fw-bold">예금 / 적금 추천</h1>
                    <h2 class="my-3 fw-bold">알고리즘 서비스</h2>
                    <br>
                    <div class="my-3">
                        <h4>
                            빅데이터와 AI를 통해
                        </h4>
                        <h4>
                            사용자에게 가장 적합한 상품들을
                        </h4>
                        <h4>
                            추천할 수 있도록 서비스합니다.
                        </h4>
                    </div>
                </div>
            </div>
        </article>

    </div>
</template>

<script setup>
</script>

<style scoped>
    h1, h2, h3, h4, h5 {
        text-wrap: wrap;
    }
    article {
        height: 500px;
        min-width:500px;
        max-width:1200px;
        width:100%;
        align-items: center;
        padding-top: 50px;
        padding-bottom: 50px;
        /* display: flex; */
        justify-content: space-between;
        margin-top: 50px;
        margin-bottom: 30px;
        overflow: visible;
        box-sizing: border-box
    }
    article img {
        width: 370px;
        max-width: 100%;
        height: 350px;
        object-fit: fill;
        border-radius: 40px;
    }
    .container-up {
        min-height: 750px;
        max-height: 800px;
        margin-top: 50px;
        margin-bottom: 0px;
        padding-bottom: 50px;        
    }
    .container-up img {
        width: 100%;
        min-height: 100%;
        height: 400px;
        min-width:100%;
        margin-top: 0px;
    }
    .container-up h1,
    .container-up h2,
    .container-up h5 {
        word-wrap: break-word;
    }
    
</style>