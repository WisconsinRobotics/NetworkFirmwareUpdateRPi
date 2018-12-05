<template>
  <md-card class="md-card-tabs"
    :class="[
      {'flex-column': flexColumn},
      {'nav-pills-icons': navPillsIcons},
      {'md-card-plain': plain}
    ]">
    <md-card-header slot="header-title">

    </md-card-header>

    <md-card-content class="md-layout md-alignment-top-center">
      <md-list class="nav-tabs">
        <md-list-item
          v-for="(item, index) in tabName"
          @click="switchPanel(tabName[index], tabFunction[index])"
          ref="tab"
          :key="item"
          :class="[
            {active: isActivePanel(tabName[index])},
            {[getColorButton(colorButton)]: isActivePanel(tabName[index])}]">
            {{tabName[index]}}
            <md-icon md-src="tabIcon[index]" v-if="navPillsIcons" />
        </md-list-item>
      </md-list>

      <transition name="fade" mode="out-in">
        <div class="tab-content">
          <div
            :class="getTabContent(index + 1)"
            v-for="(item, index) in tabName"
            style="width: 300px;"
            :key="item"
            v-if="isActivePanel(tabName[index])">
            <slot :name="getTabContent(index + 1)">
              This is the default text!
            </slot>
          </div>
        </div>
      </transition>
    </md-card-content>
  </md-card>
</template>

<script>
export default {
  props: {
    flexColumn: Boolean,
    navPillsIcons: Boolean,
    plain: Boolean,
    tabName: Array,
    tabIcon: Array,
    tabFunction: Array,
    colorButton: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      activePanel: this.tabName[0]
    };
  },
  methods: {
    switchPanel(panel, clickFunction) {
      this.activePanel = panel;
      if (clickFunction !== null) {
        clickFunction()
      }
    },
    isActivePanel(panel) {
      return this.activePanel == panel;
    },
    getColorButton: function(colorButton) {
      return "md-" + colorButton + "";
    },
    getTabContent: function(index) {
      return "tab-pane-" + index + "";
    }
  }
};
</script>

<style lang="css">
</style>
