<template>
    <div>
      <div class="notice">
        <div class="page-title">
          <div class="container">
            <h3>{{ board }} 게시판</h3>
          </div>
        </div>

        <!-- board seach area -->
        <div id="board-search">
          <div class="container pt-0">
            <div class="search-window pt-0">
              <form @submit.prevent="clickEvent">
                <div class="serach_wrap text-end mb-2 pt-0">
                  <RouterLink type="submit"
                  class="btn btn-primary"
                  :to="{name:'createArticle'}"
                  >게시글 생성</RouterLink>
                </div>
              </form>
            </div>  
          </div>
        </div>
        
        <!-- board list area -->
        <div id="board-list">
          <div class="container">
            <table class="board-table">
              <thead>
                <tr>
                  <th scope="col" class="th-num">번호</th>
                  <th scope="col" class="th-title">제목</th>
                  <th scope="col" class="th-date">작성자</th>
                  <th scope="col" class="th-date">등록일</th>
                </tr>
              </thead>
              <tbody v-if="store.articles">

                <tr v-for="article in store.articles">
                  <td>{{ article.id }}</td>
                  <th>
                    <RouterLink :to="{name:'articleDetail', params:{'board':board, 'articleId':article.id }}">
                      {{ article.title }}
                    </RouterLink>
                  </th>
                  <td>{{ article.author.username }}</td>
                  <td>{{ store.formatDateTime(article.created_at) }}</td>
                </tr>

              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
  import { onMounted, ref } from 'vue';
  import { useCommunityStore } from '@/stores/community';
  import { useRoute } from 'vue-router';
  const route = useRoute()
  const store = useCommunityStore()
  
  // 게시판 이름
  const board = ref(route.params.board)

  onMounted ( () => {
    store.getArticles(board.value)
  })  

</script>

<style scoped>

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
/* 
.btn {
  display: inline-block;
  padding: 0 30px;
  font-size: 15px;
  font-weight: 400;
  background: transparent;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border: 1px solid transparent;
  text-transform: uppercase;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  -ms-transition: all 0.3s;
  -o-transition: all 0.3s;
  transition: all 0.3s;
} */

.btn-dark {
  background: #555;
  color: #fff;
}

.btn-dark:hover,
.btn-dark:focus {
  background: #373737;
  border-color: #373737;
  color: #fff;
}

.btn-dark {
  background: #555;
  color: #fff;
}

.btn-dark:hover,
.btn-dark:focus {
  background: #373737;
  border-color: #373737;
  color: #fff;
}

/* reset */

.clearfix:after {
  content: '';
  display: block;
  clear: both;
}

.blind {
  position: absolute;
  overflow: hidden;
  clip: rect(0 0 0 0);
  margin: -1px;
  width: 1px;
  height: 1px;
}
</style>