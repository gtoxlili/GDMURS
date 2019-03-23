import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing-page',
      component: require('@/components/Wecome').default
    },
    {
      path: '/chouti',
      name: 'chouti',
      component: require('@/components/chouti').default
    },
    {
      path: '/zhuowei',
      name: 'zhuowei',
      component: require('@/components/zhuowei').default
    },
    {
      path: '/Tiku',
      name: 'Tiku',
      component: require('@/components/Tiku').default
    },{
      path: '/floatbottom',
      name: 'floatbottom',
      component: require('@/components/floatbottom').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
