<template>
  <div style="border: 1px solid black">
    <h1>This is a component from the <strong>events</strong> module</h1>
    <ul>
      <li style="display: list-item" v-for="event in myevents" v-bind:key="event.id">
        {{ event.name }} on {{ new Date(event.date).toUTCString() }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import format from 'date-format'

export default {
  name: 'Events',
  data () {
    return {
      myevents: []
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/myevents/')
      .then((response) => {
        this.myevents = response.data

      })
  },
  methods: {
    convertDate (dateString) {
      return format.parse(format.ISO8601_FORMAT, dateString).getMonth()
    }
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
