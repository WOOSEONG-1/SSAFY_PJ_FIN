import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import CommunityView from '@/views/community/CommunityView.vue'
import ProductView from '@/views/product/ProductView.vue'
import NearBankView from '@/views/NearBankView.vue'
import LoginView from '@/views/account/LoginView.vue'
import SignUpView from '@/views/account/SignUpView.vue'
import ArticleDetailView from '@/views/community/ArticleDetailView.vue'
import BoardView from '@/views/community/BoardView.vue'
import CreateArticleView from '@/views/community/CreateArticleView.vue'
import UpdateArticleView from '@/views/community/UpdateArticleView.vue'
import ProfileView from '@/views/profile/ProfileView.vue'
import UpdateProfileView from '@/views/profile/UpdateProfileView.vue'
import ProfileHomeView from '@/views/profile/ProfileHomeView.vue'
import { useUserStore } from '@/stores/user'
import ProductSearchView from '@/views/product/ProductSearchView.vue'
import ProductDetailView from '@/views/product/ProductDetailView.vue'
import RecommendView from '@/views/recommend/RecommendView.vue'
import RecommendCosineView from '@/views/recommend/RecommendCosineView.vue'
import RecommendAiView from '@/views/recommend/RecommendAiView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/product/:type/:bank/:trm',
      component: ProductView,
      children: [
        {
          path: '',
          name: 'product',
          component: ProductSearchView
        },
        {
          path: 'detail/:productId',
          name: 'productDetail',
          component: ProductDetailView
        }
      ]
    },
    {
      path:'/exchange',
      name:'exchange',
      component:ExchangeView
    },
    {
      path:'/bank',
      name:'bank',
      component:NearBankView
    },
    {
      path:'/community',
      component:CommunityView,
      children:[
        {path:':board/', name:'community', component:BoardView},
        {path:':board/:articleId', name:'articleDetail', component:ArticleDetailView},
        {path:':board/create', name:'createArticle', component:CreateArticleView},
        {path:':board/:articleId/update', name:'updateArticle', component:UpdateArticleView},
      ]
    },
    {
      path:'/profile',
      component:ProfileView,
      children:[
        {path:':username/', name:'profile', component:ProfileHomeView},
        {path:':username/update', name:'updateProfile', component:UpdateProfileView},
      ]
    },
    {
      path:'/recommend',
      component:RecommendView,
      children:[
        {path:'cosine', name:'cosine', component:RecommendCosineView},
        {path:'ai/', name:'ai', component:RecommendAiView},
      ]
    },
    {
      path:'/login',
      name:'login',
      component:LoginView
    },
    {
      path:'/signup',
      name:'signup',
      component:SignUpView
    },
  ]
})


router.beforeEach((to, from) => {
  const store = useUserStore()
  if ( (to.name === 'createArticle' || to.name === 'updateArticle' || to.name === 'cosine' || to.name === 'ai') && !store.isLogin ) {
    window.alert('로그인이 필요합니다')
    return {name:'login'}
  }
})

export default router