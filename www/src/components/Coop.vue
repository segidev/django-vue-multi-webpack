<template>
  <div class="hello">
    Welcome to COOP website. Please choose your destiny
    <br>
    <ul>
      <li><router-link to="/person">To Person</router-link></li>
      <li><router-link to="/events">To Events</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Coop',
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
  display: block;
  margin: 10px 0;
}
a {
  color: #42b983;
}
</style>
