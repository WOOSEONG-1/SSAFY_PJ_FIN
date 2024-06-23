import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useUserStore } from './user'
import { useRouter } from 'vue-router'

export const useCommunityStore = defineStore('community', () => {
  const API_URL = 'http://localhost:8000/api/v1/backend/communities'
  const articles = ref(null)
  const articleDetail = ref(null)
  const articleComment = ref(null)
  const isLike = ref(null)
  const likeCount = ref(null)
  const boards = ref(null)

  const store = useUserStore()
  const router = useRouter()
  // 게시판 전체 게시글 조회
  const getArticles = function (boardName) {
    axios({
      method: 'get',
      url: `${API_URL}/${boardName}/`,
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 게시글 생성
  const createArticle = function (boardName, payload) {
    axios({
      method: 'post',
      url: `${API_URL}/${boardName}/`,
      data: {
        title: payload.title,
        content: payload.content
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
      .then((res) => {
        // console.log("게시글 생성 완료")
        router.push({ name: 'community', params: { 'board': boardName } })        
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 게시글 수정
  const updateArticle = function (boardName, articleId, payload) {
    axios({
      method: 'put',
      url: `${API_URL}/${boardName}/${articleId}/`,
      data: {
        title: payload.title,
        content: payload.content
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
      .then(() => {
        router.push({ name: 'articleDetail', params: { 'board': boardName, 'articleId': articleId } })
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 게시글 상세 정보
  const getArticleDetail = function (boardName, articleId) {
    axios({
      method: 'get',
      url: `${API_URL}/${boardName}/${articleId}/`,
    })
      .then((res) => {
        articleDetail.value = res.data
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 게시글 삭제
  const deleteArticle = function (boardName, articleId) {
    axios({
      method: 'delete',
      url: `${API_URL}/${boardName}/${articleId}/`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
      .then((res) => {
        router.push({ name: 'community', params: { 'board': boardName } })
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 게시판 댓글 조회
  const getComments = function (boardName, articleId) {
    axios({
      method: 'get',
      url: `${API_URL}/${boardName}/${articleId}/comment/`,
    })
      .then((res) => {
        articleComment.value = res.data
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 댓글 생성
  const createComment = function (boardName, articleId, payload) {
    if (store.isLogin) {
      axios({
        method: 'post',
        url: `${API_URL}/${boardName}/${articleId}/comment/`,
        data: {
          content: payload.content
        },
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`
        }
      })
        .then(() => {
          getComments(boardName, articleId)
        })
        .catch((err) => {
          console.error(err.data)
        })
    }
    else {
      window.alert('로그인 한 사용자만 가능합니다 !')
      router.push({ name: 'login' })
    }
  }

  // 댓글 삭제
  const deleteComment = function (boardName, articleId, commentId, payload) {
    if (store.isLogin) {
      axios({
        method: 'delete',
        url: `${API_URL}/${boardName}/${articleId}/comment/${commentId}/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`
        }
      })
        .then(() => {
          getComments(boardName, articleId)
        })
        .catch((err) => {
          console.error(err.data)
        })
    }
    else {
      window.alert('로그인 한 사용자만 가능합니다 !')
      router.push({ name: 'login' })
    }
  }

  // 날짜 형식 변환
  const formatDateTime = (isoString) => {
    const pad = (number) => (number < 10 ? '0' + number : number);
    const date = new Date(isoString);

    const year = date.getFullYear();
    const month = pad(date.getMonth() + 1);
    const day = pad(date.getDate());
    const hours = pad(date.getHours());
    const minutes = pad(date.getMinutes());
    const seconds = pad(date.getSeconds());

    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
  }

  // 좋아요 요청
  const createLike = function (boardName, articleId) {
    axios({
      method: 'post',
      url: `${API_URL}/${boardName}/${articleId}/likes/`,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
      .then((res) => {
        getLike(boardName, articleId)
      })
      .catch((err) => {
        console.error(err.data)
      })
  }

  // 좋아요 판별
  const getLike = function (boardName, articleId) {
    if (store.isLogin) {
      axios({
        method: 'get',
        url: `${API_URL}/${boardName}/${articleId}/likes/`,
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`
        }
      })
        .then((res) => {
          isLike.value = res.data.isLike
          likeCount.value = res.data.like_count
        })
        .catch((err) => {
          console.error(err.data)
        })
    }
  }

  const getBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/boards/`
    })
    .then( (res) =>
      boards.value = res.data
    )
    .catch ( err => console.error(err) )
  }

  return {
    articles, articleDetail, articleComment, isLike, likeCount, boards,
    getArticles, getArticleDetail, createArticle, deleteArticle, updateArticle,
    getComments, createComment, deleteComment,
    createLike, getLike, getBoards,
    formatDateTime
  }
})
