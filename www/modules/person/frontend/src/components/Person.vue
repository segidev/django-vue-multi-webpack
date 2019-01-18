<template>
  <div style="border: 1px solid black">
    <h1>This is a component from the <strong>person</strong> module</h1>
    <ul>
      <li style="display: list-item" v-for="user in myusers" v-bind:key="user.id">
        {{ user.name }} (<a :href="'mailto:' + user.email">E-Mail</a>)
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Person',
  data () {
    return {
      myusers: []
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/myusers/')
      .then((response) => {
        this.myusers = response.data
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
