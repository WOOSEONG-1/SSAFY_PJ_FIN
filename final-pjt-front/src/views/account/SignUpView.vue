<template>
  <section style="position:relative;" class="mb-5">
    <img src="@/assets/signup.webp" alt="main_img" data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">Sign Up</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">사이트에 회원가입하시고</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">다양한 서비스를 누리세요 !</h4>
  </section>
  <div class="container-content d-flex justify-content-center align-items-center">
    <main>
      <div class="py-5 text-center" id="errorContainer">
        <img class="d-block mx-auto mb-4" src="@/assets/logo.png" width="150" height="150">
        <h2 class="fw-bold mb-5" style="font-size: 50px;">회원 가입</h2>
      </div>

      <div class="row g-5" style="margin-bottom: 100px; max-width: 1200px;">
        <div class="col-lg-12">
          <h4 class="mb-3">회원 정보 입력</h4>
          <p class="mb-3 text-muted">
            <span style="color:red; font-size: larger;">&nbsp;*</span>는 필수 입력 항목입니다.
          </p>
          <div v-if="errormsg" class="row">
            <p class="text-danger mb-2" v-for="err in errormsg">
              {{ err }}
            </p>
          </div>
          <hr>
          <form class="mt-5" @submit.prevent="submitEvent">
            <div class="row g-4">
              <div class="col-12">
                <label for="name" class="form-label">이름<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                <input type="text" class="form-control" id="name" placeholder="성함을 입력해주세요." required
                  v-model="inputName">
              </div>

              <div class="col-12">
                <label for="id" class="form-label">아이디<span style="color:red; font-size: larger;">&nbsp;*</span></label>
                <div class="input-group">
                  <input type="text" class="form-control" id="id" placeholder="ID" required v-model="inputId">
                </div>
              </div>

              <div class="col-12">
                <label for="password" class="form-label">비밀번호<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                <div class="input-group">
                  <input type="password" class="form-control" id="password" required v-model="inputPassword">
                </div>
              </div>

              <div class="col-12">
                <label for="password2" class="form-label">비밀번호 확인<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                <div class="input-group">
                  <input type="password" class="form-control" id="password2" required v-model="inputPassword2">
                </div>
              </div>

              <div class="col-12">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" placeholder="you@example.com" v-model="inputEmail">
              </div>

              <div class="col-12">
                <label for="age" class="form-label">나이 <span class="text-muted">( 0 ~ 100 사이의 값을 입력해주세요 )</span></label>
                <div class="input-group">
                  <input type="text" class="form-control" id="age" placeholder="25" v-model="inputAge">
                </div>
              </div>

              <div class="col-12">
                <label for="money" class="form-label">현재 보유금 <span class="text-muted">( 0 ~ 100000000 사이의 값을 입력해주세요.
                    )</span></label>
                <input type="text" class="form-control" id="money" placeholder="Ex) 1000000" v-model="inputMoney">
              </div>

              <div class="col-12">
                <label for="salary" class="form-label">연봉 <span class="text-muted">( 0 ~ 1500000000 사이의 값을 입력해주세요.
                    )</span></label>
                <input type="text" class="form-control" id="address2" placeholder="Ex) 연 3000만원 = 30000000"
                  v-model="inputSalary">
              </div>

              <div class="col-md-2">
                <label for="gender" class="form-label">성별<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                <select class="form-select" id="gender" required v-model="inputGender">
                  <option value="0">남성</option>
                  <option value="1">여성</option>
                </select>
              </div>
            </div>
            <hr class="my-5">
            <div class="text-center">
              <button class="w-50 btn btn-primary btn-lg fs-4 fw-bold" type="submit">회원 가입</button>
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';

const store = useUserStore()

const inputName = ref('')
const inputId = ref('')
const inputPassword = ref('')
const inputPassword2 = ref('')
const inputEmail = ref('')
const inputMoney = ref('')
const inputSalary = ref('')
const inputAge = ref('')
const inputGender = ref('')
const errormsg = ref([])

const submitEvent = function () {
  errormsg.value = []
  let isOK = true

  if (inputMoney.value.trim() === "") {
    inputMoney.value = "0"
  }
  if (inputAge.value.trim() === "") {
    inputAge.value = "0"
  }
  if (inputSalary.value.trim() === "") {
    inputSalary.value = "0"
  }
  if (inputEmail.value.trim() === "") {
    inputEmail.value = "defaultuser@email.com"
  }

  const payload = {
    nickname: inputName.value.trim(),
    username: inputId.value.trim(),
    password1: inputPassword.value.trim(),
    password2: inputPassword2.value.trim(),
    email: inputEmail.value.trim(),
    money: inputMoney.value.trim(),
    age: inputAge.value.trim(),
    salary: inputSalary.value.trim(),
    gender: inputGender.value.trim(),
  }

  if (payload.password1 !== payload.password2) {
    errormsg.value.push('비밀번호를 다시 확인해주세요 !')
    isOK = false
  }
  if (payload.password1.length < 8) {
    errormsg.value.push('비밀번호가 너무 짧습니다 !')
    isOK = false
  }

  if (payload.money && (isNaN(payload.money) || payload.money > 100000000 || payload.money < 0)) {
    errormsg.value.push('현재 보유금 항목을 다시 확인해주세요 !')
    isOK = false
  }

  if (payload.age && (isNaN(payload.age) || payload.age > 100 || payload.age < 0)) {
    errormsg.value.push('현재 나이 항목을 다시 확인해주세요 !')
    isOK = false
  }

  if (payload.salary && (isNaN(payload.salary) || payload.salary > 1500000000 || payload.salary < 0)) {
    errormsg.value.push('현재 연봉 항목을 다시 확인해주세요 !')
    isOK = false
  }

  if (errormsg.value.length > 0) {
    const errorElement = document.getElementById('errorContainer')
    if (errorElement) {
      errorElement.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  if (isOK) {
    store.signUpEvent(payload)
  }
}




</script>

<style scoped></style>