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
            :tab-function="[null, getGit, getHistory]"
            plain
            nav-pills-icons
            color-button="danger">

            <!-- Upload File Tab -->
            <template slot="tab-pane-1">

              <h6 style="text-align: center">
                Select an image to flash from your files
              </h6>

              <md-field>
                <label>Browse for Image</label>
                <md-file @change="onFileUpload($event)" v-model="filename" accept=".bin" />
              </md-field>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" :disabled="this.file == null" @click="postFile">
                    <md-icon>flash_on</md-icon>Flash {{filename}}
                  </md-button>
                </div>
              </div>

            </template>

            <!-- Git Tab -->
            <template slot="tab-pane-2">

              <h6 style="text-align: center">
                Select an image to flash from tagged releases on github
              </h6>

              <div v-for="image of gitImages">
              </div>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" :disabled="this.gitRadio == null" @click="postGit">
                    <md-icon>flash_on</md-icon>Flash {{gitRadio}}
                  </md-button>
                </div>
              </div>

            </template>

            <!-- History Tab -->
            <template slot="tab-pane-3">
              <h6 style="text-align: center">
                Select an image to upload from recently flashed images
              </h6>

              <div v-for="image of history">
                <md-radio v-model="historyRadio" :value="image">{{ image }}</md-radio>
              </div>

              <div class="md-layout md-alignment-top-center">
                <div class="md-layout-item md-size-100">
                  <md-button class="md-danger md-block" :disabled="this.historyRadio == null" @click="postHistory">
                    <md-icon>flash_on</md-icon>Flash {{historyRadio}}
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
import Tabs from './Tabs.vue';
import axios from 'axios';

export default {
  data: () => ({
    randomNumber: 0,
    filename: null,
    file: null,
    history: null,
    historyRadio: null,
    gitRadio: null,
    gitImages: null,
    gitReleaseIDs: null,
    host: location.hostname,
    port: 5000
  }),
  components: {
    Tabs,
  },
  methods: {
    postFile() {
      let url = 'http://' + this.host + ':' + this.port + '/api/upload'
      let formData = new FormData();
      formData.append('file', this.file);
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data',
        }
      }

      axios.post(url, formData, config);

      this.file = null
      this.filename = ''
    },
    postGit() {
      let url = 'http://' + this.host + ':' + this.port + '/api/uploadGit'
      let data = {
        id: this.gitReleaseIDs[this.gitRadio]
      }
      let config = {
        headers: {
          'Access-Control-Allow-Headers': '*',
          'Content-Type': 'application/json',
        }
      }
      axios.post(url, data, config);

      this.gitRadio = null
    },
    postHistory() {
      let url = 'http://' + this.host + ':' + this.port + '/api/uploadHistory'
      let data = {
        file: this.historyRadio
      }
      let config = {
        headers: {
          'Access-Control-Allow-Headers': '*',
          'Content-Type': 'application/json',
        }
      }
      axios.post(url, data, config);

      this.historyRadio = null
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
    getGit() {
      let url = 'http://' + this.host + ':' + this.port + '/api/github'
      axios
        .get(url)
        .then((gitJSON) => {
          // handle success
          console.log(gitJSON);
          this.gitImages = []
          this.gitReleaseIDs = {}
          for (var key in gitJSON.data) {
            this.gitImages.push(gitJSON.data[key].name)
            this.gitReleaseIDs[gitJSON.data[key].name] = gitJSON.data[key].id
          }
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
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
