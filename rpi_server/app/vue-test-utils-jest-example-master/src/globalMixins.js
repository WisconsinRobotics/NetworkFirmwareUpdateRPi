/**
 * Adds a global mixin, which applies to every component, to add and remove
 * that component when its mounted and destroyed, respectively
 */

const GlobalMixins = {
  install (Vue) {
    Vue.mixin({
      mounted () {
        let { bodyClass } = this.$options
        if (bodyClass) {
          document.body.classList.add(bodyClass)
        }
      },
      beforeDestroy () {
        let { bodyClass } = this.$options
        if (bodyClass) {
          document.body.classList.remove(bodyClass)
        }
      }
    })
  }
}

export default GlobalMixins
