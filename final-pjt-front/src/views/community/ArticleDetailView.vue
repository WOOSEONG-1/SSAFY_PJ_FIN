<template>
  <div>
    <div class="notice">
      <div class="container mt-4" style="margin-bottom: 150px;" v-if="store.articleDetail">
        
        <div class="post-container" >
          <div class="post-header mb-3">
            {{ store.articleDetail.title }}</div>
          <div class="post-meta pt-1">
            <span>{{ store.articleDetail.author.username }} &nbsp;|&nbsp; {{ store.formatDateTime(store.articleDetail.created_at) }}</span>
          </div>
          <div class="post-content pt-4" style="min-height: 200px;">
            {{ store.articleDetail.content }}
          </div>
          <div class="post-actions">
            <div v-if="userStore.isLogin">
              <button class="btn btn-primary pe-3" @click="likeEvent" v-if="store.isLike==='True'">
                👍 좋아요 &nbsp;{{ store.likeCount }}
              </button>
              <button class="btn btn-secondary pe-3" @click="likeEvent" v-if="store.isLike!=='True'">
                👍 좋아요 &nbsp;{{ store.likeCount }}
              </button>
            </div>
            <div>
              <button class="me-3 btn btn-secondary" @click="goBack">목록</button>
              <button class="btn btn-success me-3" 
                @click="updateArticleEvent"
                v-if="store.articleDetail.author.username === userStore.username">
                  글 수정
              </button>
              <button class="btn btn-danger" @click="deleteArticleEvent"
              v-if="store.articleDetail.author.username === userStore.username">
                글 삭제
              </button>
            </div>
          </div>
        </div>
        <div class="post-stats ps-3" v-if="store.articleComment">
          <span class="me-3">댓글 {{ store.articleComment.length }}</span>
        </div>
        <hr>
        <h5 class="ps-3 fw-bold">❤ &nbsp;&nbsp;댓글 보기</h5>
        <!-- 댓글 조회 -->
        <div v-if="store.articleComment" class="pt-2 ps-3" >
          <div v-for="comment in store.articleComment" class="border-top border-bottom" style="position: relative">
            <p class="py-3 mb-0">{{ comment.content }}</p>
            <p class="text-muted mb-2" style="font-size: 14px;">
              작성자 : {{ comment.author.username }} &nbsp; | &nbsp; {{ store.formatDateTime(comment.created_at) }}
            </p>
            <button 
              style="position: absolute; right:20px; top:10px; 
              border: none; width: 40px; height:40px; background-color: white;" 
              @click="deleteCommentEvent(comment.id)" v-if="userStore.username === comment.author.username">
              ❌
            </button>
            <!-- <button style="right: 0;">hi</button> -->
          </div>
        </div>

        <!-- 댓글 작성 -->
        <hr>
        <div>
          <h5 class="ps-3 fw-bold">🖊 &nbsp;&nbsp;댓글 작성</h5>
          <form class="pt-2 ps-3 input-group" @submit.prevent="createCommentEvent">
            <label for="comment"></label>
            <input type="text" class="form-control" id="comment" v-model="inputComment">
            <button class="ms-3 btn btn-success" style="border-radius: 10px;">작성</button>
          </form>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community';
import { useUserStore } from '@/stores/user';
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const store = useCommunityStore()
const userStore = useUserStore()
const inputComment = ref('')

const goBack = function () {
  router.back()
}

const deleteArticleEvent = function () {
  store.deleteArticle(route.params.board, route.params.articleId)
}

const updateArticleEvent = function () {
  router.push({ name: 'updateArticle', params: { 'board': route.params.board, 'articleId': route.params.articleId } })
}

const createCommentEvent = function () {
  store.createComment(route.params.board, route.params.articleId, {'content':inputComment.value})
  inputComment.value = ''
}

const deleteCommentEvent = function(commentId) {
  store.deleteComment(route.params.board, route.params.articleId, commentId)
}

const likeEvent = function() {
  store.createLike(route.params.board, route.params.articleId)
}

onMounted(() => {
  store.getArticleDetail(route.params.board, route.params.articleId)
  store.getComments(route.params.board, route.params.articleId)
  if ( userStore.isLogin){
    store.getLike(route.params.board, route.params.articleId)
  }
})

</script>

<style scoped>
.notice {
  padding: 20px 0;
}

.page-title {
  margin-bottom: 40px;
}

.page-title h3 {
  /* font-size: 28px; */
  font-size: 30px;
  color: #333333;
  font-weight: bold;
  text-align: start;
}

.post-container {
  border-top: 2px solid gray;
  border-bottom: 1px solid #ddd;
  padding: 20px;
  margin-bottom: 10px;
}

.post-header {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.post-meta {
  font-size: 14px;
  color: #666;
  margin-bottom: 20px;
}

.post-content {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 20px;
}

.post-stats {
  font-size: 14px;
  color: #666;
  display: flex;
  justify-content: start;
  margin-top: 15px;
}

.post-actions {
  display: flex;
  justify-content: space-between;
  font-size: 16px;
}
</style>