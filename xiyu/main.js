
// #ifndef VUE3
import Vue from 'vue'
import App from './App'
import {http} from '@/common/http.js'
import config from '@/common/config.js'

Vue.config.productionTip = false
Vue.prototype.$http = http
Vue.prototype.$config = config

App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
import App from './App.vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif