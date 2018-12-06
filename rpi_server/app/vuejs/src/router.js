/**
 * Does necessary routing to index and displays navbar and footer
 */

import Vue from 'vue'
import Router from 'vue-router'
import Index from './components/Index.vue'
import MainNavbar from './layout/MainNavbar.vue'
import MainFooter from './layout/MainFooter.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      components: { default: Index, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 100 },
        footer: { backgroundColor: 'black' }
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash }
    } else {
      return { x: 0, y: 0 }
    }
  }
})
