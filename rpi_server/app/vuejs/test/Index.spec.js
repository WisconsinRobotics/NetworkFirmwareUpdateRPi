import { mount } from '@vue/test-utils'
import index from '@/components/Index.vue'

describe('Index.vue', () => {
  it('Checks its a vue instance', () => {
    const wrapper = mount(index)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })
})
