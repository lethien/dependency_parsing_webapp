<template>
  <div id="app">
    <HelloMessage />
    <InputForm v-on:parsed="OnParsed"/>
    <ParseResult v-bind:parsed_sentences="parsed_result"/>
  </div>
</template>

<script>
import HelloMessage from './components/HelloMessage.vue'
import InputForm from './components/InputForm.vue'
import ParseResult from './components/ParseResult.vue'

export default {
  name: 'App',
  components: {
    HelloMessage,
    InputForm,
    ParseResult
  },
  data: function() {
    return {
      parsed_result: ""
    }
  },
  methods: {
      OnParsed (value) {
          this.parsed_result = value
      }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: auto;
  width: 70%;
  padding: 20px
}
</style>
