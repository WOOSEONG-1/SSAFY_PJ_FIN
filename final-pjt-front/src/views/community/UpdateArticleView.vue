<template>
  <div v-if="store.articleDetail">
    <div class="notice">
      <div class="row mt-4">
        <h3>게시글 생성</h3>
        <form class="post-container">
          <div class="mb-4 input-group align-items-center">
            <label class="form-label mb-0 pe-3 fw-bold" for="title">
              제목
            </label>
            <input type="text" id="form" class="form-control" v-model="inputTitle">
          </div>
          <hr>
          <div class="mb-4 input-group align-items-center">
            <label class="form-label mb-0 pe-3 fw-bold" for="content">
              내용
            </label>
            <textarea name="content" id="content" class="form-control" rows="15" v-model="inputContent">
                        </textarea>
          </div>
        </form>
      </div>
      <div class="text-end">
        <button class="mt-3 btn btn-secondary" @click="updateArticleEvent">글 수정</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCommunityStore } from '@/stores/community';
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useCommunityStore()

const inputTitle = ref(`${store.articleDetail.title}`)
const inputContent = ref(`${store.articleDetail.content}`)

const updateArticleEvent = function () {
  store.updateArticle(route.params.board, route.params.articleId,
    { 'title': inputTitle.value, 'content': inputContent.value })
}

onMounted(() => {
  store.getArticleDetail(route.params.board, route.params.articleId)
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
</style>