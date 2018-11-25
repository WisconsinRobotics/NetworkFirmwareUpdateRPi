import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import '@/assets/scss/material-kit.scss'
import '@/assets/demo.css'
import globalMixins from './globalMixins'

export default {
  install (Vue) {
    Vue.use(VueMaterial)
    Vue.use(globalMixins)
  }
}
