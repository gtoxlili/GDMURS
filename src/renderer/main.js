import Vue from 'vue'
import request from 'request'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'
import db from '../datastore'
import App from './App'
import router from './router'
import store from './store'
Vue.use(Vuetify);

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = request
Vue.config.productionTip = false
Vue.db=Vue.prototype.$db = db
/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>'
}).$mount('#app')
