import Vue from 'vue'
import App from './App.vue'
import router from './router'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import '@/assets/scss/material-kit.scss'
import '@/assets/demo.css'
import globalMixins from './globalMixins'

Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(globalMixins)

const NavbarStore = {
  showNavbar: false
}

Vue.mixin({
  data () {
    return {
      NavbarStore
    }
  }
})



new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
