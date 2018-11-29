<template>
  <div class="wrapper">
    <div id="navigation-pills">
      <div class="title">
        <h3>Select Image Source</h3>
      </div>
      <div class="md-layout md-alignment-top-center">
        <div class="md-layout-item md-size-50 md-small-size-100">
          <tabs :tab-name="['Upload', 'GitHub', 'History']" :tab-icon="['folder_open', 'cloud_queue', 'history']" plain nav-pills-icons color-button="danger">
            
            <!-- Upload File Tab -->
            <template slot="tab-pane-1">
              Select an image to flash from your files

              <md-field>
                <label>Browse for Image</label>
                <md-file @change="onFileUpload($event)" v-model="filename" accept=".bin" />
              </md-field>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" :disabled="this.file == null" @click="submitFile">
                    <md-icon>flash_on</md-icon>Flash {{filename}}
                  </md-button>
                </div>
              </div>

            </template>

            <!-- Git Tab -->
            <template slot="tab-pane-2">
              Select an image to flash from tagged releases on github

            </template>

            <!-- History Tab -->
            <template slot="tab-pane-3">
              Select an image to upload from recently flashed images

              <div v-for="image of history">
                <md-radio v-model="radioImage" :value="image">{{ image }}</md-radio>
              </div>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" :disabled="this.radioImage == null">
                    <md-icon>flash_on</md-icon>Flash {{radioImage}}
                  </md-button>
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
import Tabs from './Tabs';
import axios from 'axios';

export default {
  data: () => ({
    randomNumber: 0,
    filename: null,
    file: null,
    history: null,
    radioImage: null,
    host: location.hostname,
    port: 5000
  }),
  components: {
    Tabs,
  },
  methods: {
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);

      let url = 'http://' + this.host + ':' + this.port + '/api/upload'
      axios.post(url, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      this.file = null
      this.filename = ''

      this.getHistory()
    },
    onFileUpload(event) {
      this.file = event.target.files[0];
      this.filename = this.file.name
    },
    getHistory() {
      let url = 'http://' + this.host + ':' + this.port + '/api/history'
      axios
        .get(url)
        .then((historyJSON) => {
          // handle success
          this.history = []
          for (var key in historyJSON.data) {
            this.history.push(historyJSON.data[key].name)
          }
          console.log(historyJSON);
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        });
    },
    selectHistory() {
      let url = 'http://' + this.host + ':' + this.port + '/api/selectHistory'
      axios.post(url, radioImage, {
        headers: {
          'Content-Type': 'text/plain',
        },
      });
    },
    removeNotify(e, notifyClass) {
      var target = e.target;
      while (target.className.indexOf(notifyClass) === -1) {
        target = target.parentNode;
      }
      return target.parentNode.removeChild(target);
    },
  },
  created(){
    this.getHistory()
  },
};
</script>

<style lang="css">
</style>
