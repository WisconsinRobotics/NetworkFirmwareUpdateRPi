import { mount } from '@vue/test-utils'
import NavPills from '@/components/NavPillsSection.vue'

describe('NavPillsSection.vue', () => {
  it('Checks its a vue instance', () => {
    const wrapper = mount(NavPills)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
