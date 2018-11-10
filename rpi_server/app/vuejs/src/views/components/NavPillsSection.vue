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
                <md-file v-model="local_image" />
              </md-field>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" @click="submitFile"><md-icon>flash_on</md-icon>Flash Firmware</md-button>
                </div>
              </div>

            </template>

            <template slot="tab-pane-2">
              Select an image to flash from tagged releases on github


              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" @click="submitFile"><md-icon>flash_on</md-icon>Flash Firmware</md-button>
                </div>
              </div>

            </template>

            <template slot="tab-pane-3">
              Select an image to upload from recently flashed images
              <p>Random number from backend: {{ randomNumber }}</p>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" @click="getRandom"><md-icon>flash_on</md-icon>Flash Firmware</md-button>
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
    local_image: null,
  }),
  components: {
    Tabs,
  },
  methods: {
    submitFile() {
      let formData = new FormData();
      console.log(this.local_image);
      formData.append('file', this.local_image);
      console.log(formData.getAll('file'));
      console.log('>> formData >> ', formData);

      axios
        .post('http://localhost:5000/api/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then(function() {
          console.log('SUCCESS!!');
        })
        .catch(function() {
          console.log('FAILURE!!');
        });
    },
    getRandom() {
      this.randomNumber = this.getRandomFromBackend();
    },
    getRandomFromBackend() {
      const path = `http://localhost:5000/api/random`;
      axios
        .get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber;
          console.log(this.randomNumber);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="css">
</style>
