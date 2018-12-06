<template>
  <div class="wrapper">
    <div class="page-header header-filter" :style="headerStyle">
      <div class="md-layout">
        <div class="md-layout-item">
          <div class="image-wrapper">
            <div class="brand">
              <h3>Wisconsin Robotics</h3>
              <h1>Robot Image Programmer</h1>
            </div>
            <div class="title">       
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="main main-raised">
      <div class="section section-white">
        <div class="container">
          <nav-pills></nav-pills>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
import NavPills from './NavPillsSection.vue';

export default {
  components: {
    NavPills,
  },
  name: 'index',
  bodyClass: 'index-page',
  props: {
    image: {
      type: String,
      default: require('@/assets/img/vue-mk-header.jpg'),
    },
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.image})`,
      };
    },
  },
};
</script>
<style lang="scss">
.section-download {
  .md-button + .md-button {
    margin-left: 5px;
  }
}

@media all and (min-width: 991px) {
  .btn-container {
    display: flex;
  }
}
</style>
