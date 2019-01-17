<template>
  <div id="app">
    <img src="./assets/logo.png">
    <person></person>
    <hr>
    <events></events>
  </div>
</template>

<script>
import Person from 'company-person-module/src/components/Person'
import Events from 'company-events-module/src/components/Events'

export default {
  name: 'App',
  components: {
    Events,
    Person
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
