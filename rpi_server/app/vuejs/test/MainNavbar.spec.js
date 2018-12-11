import { mount } from '@vue/test-utils'
import Navbar from '@/layout/MainNavbar.vue'
import Vue from 'vue'
import jsdom from 'jsdom'

const renderer = require('vue-server-renderer').createRenderer()
describe('MainNavbar.vue', () => {
  it('Checks it is a Vue Instance', () => {
    const wrapper = mount(Navbar)
    expect(wrapper.isVueInstance()).toBeTruthy()
  }), 
  it('Checks Help Button is Displayed', () => {
    const wrapper = mount(Navbar)
    expect(wrapper.html()).toContain('Help')
  }),
  it('Checks Help Text is Displayed', () => {
    const wrapper = mount(Navbar)
    wrapper.find('md-list-item').trigger('click')
    expect(wrapper.html()).toContain('Have a wonderful day.')
  })
})
