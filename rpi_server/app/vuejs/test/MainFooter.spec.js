import { mount } from '@vue/test-utils'
import Footer from '@/layout/MainFooter.vue'
import Vue from 'vue'
import jsdom from 'jsdom'

const renderer = require('vue-server-renderer').createRenderer()
describe('MainFooter.vue', () => {
  it('Checks its a vue instance', () => {
    const wrapper = mount(Footer)
    expect(wrapper.isVueInstance()).toBeTruthy()
  }), 
  it('Checks Links are Present', () => {
    const wrapper = mount(Footer)

    expect(wrapper.html()).toContain('GitHub')
    expect(wrapper.html()).toContain('About Us')
    expect(wrapper.html()).toContain('Wisconsin Robotics')

  })
})
