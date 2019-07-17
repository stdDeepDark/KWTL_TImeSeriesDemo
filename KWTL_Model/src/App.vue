<template>
  <div id="app">
    <router-view class="pages"></router-view>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
    
  }
}
</script>

<style lang="stylus">
html,body
  width:100%
  height:100%
  margin:0
  padding:0
  color:#fff
  font-family: sans-serif
  overflow: hidden
ul, ol 
  list-style:none
  margin:0
  padding:0
div, p, dl, dt, dd 
  margin: 0
  padding: 0
h1,h2,h3,h4,h5,h6 
  font-weight: normal
a
  text-decoration none

#app
  background linear-gradient(rgba(255,255,255,.5), #2c3e50)
  height 100%

  .pages
    height 100%
</style>