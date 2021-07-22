import Vue from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueTree from '@ssthouse/vue-tree-chart'

Vue.use(VueAxios, axios)
Vue.config.productionTip = false
Vue.component('vue-tree', VueTree)

new Vue({
  render: h => h(App),
}).$mount('#app')
