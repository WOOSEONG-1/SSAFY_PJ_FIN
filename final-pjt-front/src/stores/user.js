import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useUserStore = defineStore('user', () => {
  const AUTH_API_URL = 'http://localhost:8000/accounts'
  const API_URL = 'http://localhost:8000/api/v1/backend/accounts'
  const router = useRouter()
  const token = ref(null)
  const refreshToken = ref(null)
  const username = ref(null)
  const profile = ref(null)
  const deposit = ref(null)
  const saving = ref(null)

  // 로그인 판별용 변수
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // 회원가입
  const signUpEvent = function (payload) {
    axios({
      method: 'post',
      url: `${AUTH_API_URL}/signup/`,
      data: {
        "username": payload.username,
        "email": payload.email,
        "password1": payload.password1,
        "password2": payload.password2,
        "gender": payload.gender,
        "age": payload.age,
        "nickname": payload.nickname,
        "money": payload.money,
        "salary": payload.salary,
      }
    })
      .then((res) => {
        loginEvent({
          username: payload.username,
          password: payload.password1
        })
      })
      .catch((err) => {
        if (err.response && err.response.status === 400) {
          window.alert('이미 존재하는 회원입니다.')
        }
        else {
          console.log(err)

        }
      })
  }

  // 유저 로그인
  const loginEvent = function (payload) {
    axios({
      method: 'post',
      url: `${AUTH_API_URL}/api/token/`,
      data: {
        username: payload.username,
        password: payload.password,
      }
    })
      .then((res) => {
        token.value = res.data.access
        refreshToken.value = res.data.refresh
        username.value = payload.username
        localStorage.setItem('access_token', res.data.access);
        // localStorage.setItem('refresh_token', res.data.refresh);

      })
      .then(() => {
        router.push({ name: 'home' })
      })
      .catch((err) => {
        window.alert("로그인에 실패했습니다. 아이디와 비밀번호를 확인하세요.");
      })
  }

  // JWT 토큰 리프레쉬
  const refreshTokenEvent = function () {
    const refresh = localStorage.getItem('refresh_token');
    axios({
      method: 'post',
      url: `${AUTH_API_URL}/api/token/refresh/`,
      data: {
        refresh: refresh,
      }
    })
      .then((res) => {
        token.value = res.data.access;
        localStorage.setItem('access_token', res.data.access);
      })
      .catch((err) => {
        console.error("토큰 갱신 오류:", err.response.data);
        logoutEvent(false);
      });
  };

  // 유저 로그아웃
  const logoutEvent = function (showAlert = true) {
    axios({
      method: 'post',
      url: `${API_URL}/logout/`,
    })
      .then((res) => {
        isLogin.value = false;
        token.value = null;
        localStorage.removeItem('access_token'); // Access Token 제거
        localStorage.removeItem('refresh_token'); // Refresh Token 제거
        username.value = null;
        if (showAlert) {
          window.alert("로그아웃 처리되었습니다!");
        }
      })
      .then(() => {
        router.push({ name: 'login' })
      })
      .catch((err) => {
        if (err.response && err.response.status === 400) {
          window.alert('이미 존재하는 회원입니다.')
        }        
        console.error(err)
      })
  }

  // 유저 프로필 조회
  const getProfile = function (name) {
    axios({
      method: 'get',
      url: `${API_URL}/profile/${name}/`,
      data: {
        "username": name
      }
    })
      .then((res) => {
        profile.value = res.data
      })
      .catch(
        (err) => {
          console.log(`${API_URL}/profile/${name}/`)
        }
      )
  }

  // 차트 데이터 가져오기
  const depositchart = function (name) {
    axios({
      method: 'get',
      url: `${API_URL}/${name}/subdeposits/`,
      data: {
        "username": name
      }
    })
      .then((res) => {
        deposit.value = res.data
      })
      .catch(
        (err) => {
          console.log(`${API_URL}/profile/${name}/`)
        }
      )
  }

  // 차트 저장
  const savingchart = function (name) {
    axios({
      method: 'get',
      url: `${API_URL}/${name}/subsavings/`,
      data: {
        "username": name
      }
    })
      .then((res) => {
        saving.value = res.data
      })
      .catch(
        (err) => {
          console.log(`${API_URL}/profile/${name}/`)
        }
      )
  }

  // 유저 프로필 수정
  const updateProfile = function (name, payload) {
    axios({
      method: 'put',
      url: `${API_URL}/profile/${name}/`,
      data: {
        "email": payload.email,
        "gender": payload.gender,
        "age": payload.age,
        "nickname": payload.nickname,
        "money": payload.money,
        "salary": payload.salary,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
      .then((res) => {
        console.log(res.data)
        router.push({ name: 'profile', params: { username: name } })
      })
      .catch(err => console.log(err))
  }

  return {
    AUTH_API_URL, API_URL, username, profile,
    signUpEvent, getProfile, updateProfile, depositchart, savingchart, deposit, saving,
    loginEvent, logoutEvent, token, isLogin, refreshTokenEvent, refreshToken
  }
}, {
  persist: {
    paths: ['token', 'username'],
  }
})