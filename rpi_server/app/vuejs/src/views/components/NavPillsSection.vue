<template>
  <div class="wrapper">
    <div id="navigation-pills">
      <div class="title">
        <h3>Select Image Source</h3>
      </div>
      <div class="md-layout md-alignment-top-center">
        <div class="md-layout-item md-size-50 md-small-size-100">
          <tabs
            :tab-name="['Upload', 'GitHub', 'History']"
            :tab-icon="['folder_open', 'cloud_queue', 'history']"
            plain
            nav-pills-icons
            color-button="danger">

            <template slot="tab-pane-1">
              Select an image to flash from your files
              
              <md-field>
                <label>Browse for Image</label>
                <md-file @change="onFileUpload($event)" v-model="filename" accept=".bin"/>
              </md-field>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" @click="submitFile"><md-icon>flash_on</md-icon>Flash {{filename}}</md-button>
                </div>
              </div>

            </template>

            <template slot="tab-pane-2">
              Select an image to flash from tagged releases on github

            </template>

            <template slot="tab-pane-3" @click="getHistory">
              Select an image to upload from recently flashed images
              <div v-for="image of history">
                <md-radio v-model="radioImage" :value="image">{{ image }}</md-radio>
              </div>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" @click="selectHistory"><md-icon>flash_on</md-icon>Flash {{radioImage}}</md-button>
                </div>
              </div>

            </template>
            
          </tabs>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Tabs } from '@/components';
import axios from 'axios';

export default {
  data: () => ({
    randomNumber: 0,
    filename: null,
    file: null,
    history: ["option 1", "option 2", "option 3"],
    radioImage: null
  }),
  components: {
    Tabs,
  },
  methods: {
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);

      axios
        .post('http://localhost:5000/api/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
    },
    onFileUpload(event) {
      this.file = event.target.files[0];
    },
    getHistory() {
      console.log("This will call history api")
      this.history = ["option 1", "option 2", "option 3"]
    },
    selectHistory() {
      axios
        .post('http://localhost:5000/api/selectHistory', radioImage, {
          headers: {
            'Content-Type': 'text/plain',
          },
        })
    }
  },
};
</script>

<style lang="css">
</style>
