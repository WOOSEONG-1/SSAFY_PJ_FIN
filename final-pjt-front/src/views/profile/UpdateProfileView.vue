<template>
  <div class="container-content d-flex justify-content-center align-items-center">
    <main v-if="store.profile">

      <div class="py-5 text-center" id="errorContainer">
        <img class="d-block mx-auto mb-4" src="@/assets/logo.png" width="150" height="150">
        <h2 class="fw-bold mb-5" style="font-size: 50px;">정보 수정</h2>
      </div>

      <div class="row g-5" style="margin-bottom: 100px; max-width: 1200px;">
        <div class="col-lg-12">
          <h4>회원 정보 수정</h4>
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
                <input type="text" class="form-control" id="name" required v-model="inputName" disabled>
              </div>

              <div class="col-12">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" v-model="inputEmail">
              </div>

              <div class="col-12">
                <label for="age" class="form-label">나이<span class="text-muted">( 0 ~ 100 사이의 값을 입력해주세요 )</span></label>
                <div class="input-group">
                  <input type="text" class="form-control" id="age" v-model="inputAge">
                </div>
              </div>

              <div class="col-12">
                <label for="money" class="form-label">현재 보유금<span class="text-muted">( 0 ~ 100000000 사이의 값을 입력해주세요.
                    )</span></label>
                <input type="text" class="form-control" id="money" v-model="inputMoney">
              </div>

              <div class="col-12">
                <label for="salary" class="form-label">연봉<span class="text-muted">( 0 ~ 1500000000 사이의 값을 입력해주세요.
                    )</span></label>
                <input type="text" class="form-control" id="address2" v-model="inputSalary">
              </div>

              <div class="col-md-2">
                <label for="gender" class="form-label">성별<span
                    style="color:red; font-size: larger;">&nbsp;*</span></label>
                <select class="form-select" id="gender" required v-model="inputGender" disabled>
                  <option value="0">남성</option>
                  <option value="1">여성</option>
                  <option value="2">0</option>
                </select>
              </div>
            </div>
            <hr class="my-5">
            <div class="text-center">
              <button class="w-50 btn btn-primary btn-lg fs-4 fw-bold" type="submit">정보 수정</button>
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useUserStore } from '@/stores/user';

const store = useUserStore()

const inputName = ref(store.profile.nickname)
const inputEmail = ref(store.profile.email)
const inputMoney = ref(store.profile.money)
const inputSalary = ref(store.profile.salary)
const inputAge = ref(store.profile.age)
const inputGender = ref(store.profile.gender)
const errormsg = ref([])

const submitEvent = function () {
  errormsg.value = []
  let isOK = true

  const moneyValue = String(inputMoney.value).trim()
  const ageValue = String(inputAge.value).trim()
  const salaryValue = String(inputSalary.value).trim()
  const emailValue = String(inputEmail.value).trim()

  if (moneyValue === "") {
    inputMoney.value = "0"
  }
  if (ageValue === "") {
    inputAge.value = "0"
  }
  if (salaryValue === "") {
    inputSalary.value = "0"
  }
  if (emailValue === "") {
    inputEmail.value = "defaultuser@email.com"
  }

  const payload = {
    nickname: String(inputName.value).trim(),
    email: emailValue,
    money: moneyValue,
    age: ageValue,
    salary: salaryValue,
    gender: String(inputGender.value).trim(),
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
  console.log(emailValue)
  if (isOK) {
    store.updateProfile(store.username, payload)
  }
}


onMounted(() => {
  store.getProfile(store.username)
})



</script>

<style scoped></style>