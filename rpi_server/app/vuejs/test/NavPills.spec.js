import { mount } from '@vue/test-utils'
import NavPills from '@/components/NavPillsSection.vue'
import Vue from 'vue'
import jsdom from 'jsdom'

const renderer = require('vue-server-renderer').createRenderer()
describe('NavPillsSection.vue', () => {
  it('Checks its a vue instance', () => {
    const wrapper = mount(NavPills)
    expect(wrapper.isVueInstance()).toBeTruthy()
  }), 
  it('Checks History images are displayed ', () => {
    const ClonedComponent = Vue.extend(NavPills)
    const wrapper = new ClonedComponent({
      data() {
        return {
          history: ['image1', 'image2'],
        }
      }
    }).$mount()
    renderer.renderToString(wrapper, (err, str) => {
      // const dom = new jsdom.JSDOM(str)
      // wrapper.find('md-list-item-button').trigger('click')
      // const image = dom.window.document.getElementById('image')
      expect(str).toContain('image1')
    }) 
  })
})
