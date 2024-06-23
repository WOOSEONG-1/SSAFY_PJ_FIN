<template>
    <section style="position:relative;" class="mb-5">
        <img src="@/assets/Login.webp" alt="main_img"
        data-aos="zoom-out" data-aos-duration="600">
        <h1 data-aos="fade-down" data-aos-duration="1500">Login In</h1>
        <h4 data-aos="fade-down" data-aos-duration="1500">아이디와 패스워드를</h4>
        <h4 data-aos="fade-down" data-aos-duration="1500">입력해주세요</h4>
    </section>
    <div class="container-content my-5" id="loginbox">
        <div class="py-5 text-center">
            <img class="d-block mx-auto mb-4" src="@/assets/logo.png" width="150" height="150">
            <h2 class="fw-bold mb-5" style="font-size: 50px;">Login</h2>
        </div>
        <main class="form-signin" style="min-height:500px;">
            <form class="row gy-5 justify-content-center d-flex flex-column align-items-center"
                @submit.prevent="userLoginEvent">
                <div class="form-floating" style="width: 70%;">
                    <input type="text" class="form-control" id="floatingInput" 
                    placeholder="아이디" v-model="inputName">
                    <label for="floatingInput" class="pl-30">아이디</label>
                </div>
                <div class="form-floating" style="width: 70%;">
                    <input type="password" class="form-control" id="floatingPassword" 
                    placeholder="패스워드" v-model="inputPassword">
                    <label for="floatingPassword" class="pl-30">비밀번호</label>
                </div>
                <button class="w-50 btn btn-lg btn-primary fw-bold" type="submit">로 그 인</button>
                <button class="w-50 btn btn-lg btn-danger fw-bold" @click="goSignUp">회 원 가 입</button>
            </form>
        </main>
    </div>

</template>

<script setup>
    import { ref } from 'vue';
    import { useUserStore } from '@/stores/user';
    import { useRouter } from 'vue-router';

    const store = useUserStore()
    const router = useRouter()

    const inputName = ref('')
    const inputPassword = ref('')

    const userLoginEvent = function() {
        const payload = {
            username: inputName.value,
            password: inputPassword.value,
        }
        store.loginEvent(payload)
    }
    const goSignUp = function() {
        router.push({name:'signup'})
    }
</script>

<style scoped>
    .pl-30 {
        padding-left: 30px !important;
    }
    .form-signin {
    width: 100%;
    max-width: 1200px;
    padding: 15px;
    margin: auto;
    }

    .form-signin .checkbox {
    font-weight: 400;
    }

    .form-signin .form-floating:focus-within {
    z-index: 2;
    }

    .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
    }

    .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    }

    /* #inputbox {
        max-width: 700px;
    }
    #inputbtn {
        max-width: 600px;
    } */
</style>